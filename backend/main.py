from googleapiclient import discovery
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from scrapers.facebook import facebook_scraper
from scrapers.linkedin import linkedin_scraper
from scrapers.twitter import twitter_scraper
from mynltk.tost import do_classify
from roles import get_roles
from send_mail import send_mail
from rich import print

def bias(final_res: dict[str, float], current_ocean_data: dict[str, int]):
    print(final_res)
    print(current_ocean_data)
    for k, v in currrent_ocean_data:
        final_res[k] += v

def listener(event):
    path_updated = event.path
    print(f"{path_updated} updated.")

    userData = userRef.get()
    oceanData = oceanRef.get()
    if "current_user_app" in path_updated:
        current_user_data = userData["current_user_app"]
        current_ocean_data = oceanData["current_user_app"]
    elif "current_user_web" in path_updated:
        current_user_data = userData["current_user_web"]
        current_ocean_data = oceanData["current_user_web"]
    else:
        return

    # all_texts = set()
    # if current_user_data["facebook"]:
    #     all_texts.update(facebook_scraper(current_user_data["facebook"]))
    # if current_user_data["linkedin"]:
    #     all_texts.update(linkedin_scraper(current_user_data["linkedin"]))
    # if current_user_data["twitter"]:
    #     all_texts.update(twitter_scraper(current_user_data["twitter"]))

    all_texts = set()
    with open("temp.txt", "r") as f:
        all_texts.update(line.strip() for line in f.readlines())

    analyze_request = {
        "comment": {"text": " ".join(all_texts)},
        "requestedAttributes": {
            "TOXICITY": {},
            "SEVERE_TOXICITY": {},
            "IDENTITY_ATTACK": {},
            "INSULT": {},
            "PROFANITY": {},
            "THREAT": {},
        },
    }

    response = client.comments().analyze(body=analyze_request).execute()

    reject_attributes = []
    total_index = 0
    for attribute in analyze_request["requestedAttributes"].keys():
        attribute_index = response["attributeScores"][attribute]["summaryScore"][
            "value"
        ]
        if attribute_index > 0.8:
            reject_attributes.append(attribute)
        else:
            total_index += attribute_index

    average_index = total_index / len(analyze_request["requestedAttributes"])
    if len(reject_attributes):
        send_mail(current_user_data["email"], f"""
Sorry to inform you, {current_user_data['name']}, you have failed our initial social media toxicity screening.
These points might help you to analyze why we made this decision.
{reject_attributes}
Regards,
Company XYZ
              """)
        return
    elif average_index > 0.5:
        print(
            "You are selected for the next phase of hiring but we have noticed some sensitive content in your public social",
            "media. But don't worry we will have an in depth discussion where you get to explain yourself.",
        )
    else:
        print("Congratulations, You have passed the first phase of the interview")

    final_res = {}
    for text in all_texts:
        if not final_res:
            final_res = do_classify(text)
        else:
            cur_res = do_classify(text)
            for k, v in cur_res.items():
                final_res[k] += v


    for key in final_res.keys():
        final_res[key] /= len(all_texts)
        final_res[key] *= 100

    bias(final_res, current_ocean_data)

    with open("result.json", "w") as fp:
        json.dump(final_res, fp)

    role1, role2 = get_roles(final_res)
    print(f"Most Suitable Job: {role1}")
    print(f"Alternative Job: {role2}")
    send_mail(current_user_data["email"], f"""
Congratulations {current_user_data['name']}! You have passed both rounds of Psyche-Screener.
We have selected the following roles for you:
1. {role1}
2. {role2}
We look forward to seeing you in our interview process. Best of luck!

Regards,
Company XYZ
              """)


if __name__ == "__main__":
    cred = credentials.Certificate("/home/praneeth/Downloads/service-account-file.json")
    firebase_admin.initialize_app(
        cred,
        {
            "databaseURL": "https://pentagon-megathon-default-rtdb.asia-southeast1.firebasedatabase.app"
        },
    )

    userRef = db.reference("Users")
    oceanRef = db.reference("Oceans")

    API_KEY = "AIzaSyD0Ky_uXkK_L1f2yzZkOWNdv8fxPgHM3Ns"

    client = discovery.build(
        "commentanalyzer",
        "v1alpha1",
        developerKey=API_KEY,
        discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
        static_discovery=False,
    )

    oceanRef.listen(listener)
