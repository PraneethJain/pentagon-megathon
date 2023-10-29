from googleapiclient import discovery
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from scrapers.facebook import facebook_scraper
from scrapers.linkedin import linkedin_scraper
from scrapers.twitter import twitter_scraper
from mynltk.tost import do_classify

# cred = credentials.Certificate("/home/praneeth/Downloads/service-account-file.json")
# firebase_admin.initialize_app(
#     cred,
#     {
#         "databaseURL": "https://pentagon-megathon-default-rtdb.asia-southeast1.firebasedatabase.app"
#     },
# )

# ref = db.reference()
# data = ref.get()["Users"]
# # process the data
# current_user_data = data["current_user_app"]
# all_texts: set[str] = set()
# if current_user_data["facebook"]:
#     all_texts.update(facebook_scraper(current_user_data["facebook"]))
# if current_user_data["linkedin"]:
#     all_texts.update(linkedin_scraper(current_user_data["linkedin"]))
# if current_user_data["twitter"]:
#     all_texts.update(twitter_scraper(current_user_data["twitter"]))
# # remove the ref


# with open("temp.txt", "w") as f:
#     for text in all_texts:
#         f.write(text)

all_texts: set[str] = set()
with open("temp.txt", "r") as f:
    all_texts.update(line.strip() for line in f.readlines())


API_KEY = "AIzaSyD0Ky_uXkK_L1f2yzZkOWNdv8fxPgHM3Ns"

client = discovery.build(
    "commentanalyzer",
    "v1alpha1",
    developerKey=API_KEY,
    discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
    static_discovery=False,
)

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
#print(json.dumps(response, indent=2))

#toxicity_index = response["attributeScores"]["TOXICITY"]["summaryScore"]["value"]
#if toxicity_index > 0.8:
#    # reject
#    print("REJECTED!")
#    raise SystemExit
#elif toxicity_index > 0.5:
#    # maybe
#    print("Manual Review Needed!")
#else:
#    print("First layer of screening passed!")

reject_attributes = []
total_index = 0
for attribute in analyze_request["requestedAttributes"].keys():
    attribute_index = response["attributeScores"][attribute]["summaryScore"]["value"]
    if attribute_index > 0.8:
        # reject
        reject_attributes.append(attribute)
    else:
        total_index += attribute_index

average_index = total_index / len(analyze_request["requestedAttributes"])
if len(reject_attributes):
    print("REJECTED! because the following were found by analysing your social media: {}", *reject_attributes, sep = ',' )
elif average_index > 0.5:
    print("You are selected for the next phase of hiring but we have noticed some sensitive content in your public social",
          "media. But don't worry we will have an in depth discussion where you get to explain yourself.")
else:
    print("Congratulations, You have passed the first phase of the interview")


# phase 2 
final_res: dict[str, int] = {}
for text in all_texts:
    if not final_res:
        final_res = do_classify(text)
    else:
        cur_res = do_classify(text)
        for k, v in cur_res.items():
            final_res[k] += v

for key in final_res.keys():
    final_res[key] /= len(all_texts)

with open('result.json', 'w') as fp:
    json.dump(final_res, fp)

