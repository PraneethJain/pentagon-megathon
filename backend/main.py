from googleapiclient import discovery
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from scrapers.facebook import facebook_scraper
from scrapers.linkedin import linkedin_scraper
from scrapers.twitter import twitter_scraper

cred = credentials.Certificate("/home/praneeth/Downloads/service-account-file.json")
firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": "https://pentagon-megathon-default-rtdb.asia-southeast1.firebasedatabase.app"
    },
)

ref = db.reference()
data = ref.get()["Users"]
# process the data
current_user_data = data["current_user_app"]
all_texts: set[str] = set()
if current_user_data["facebook"]:
    all_texts.update(facebook_scraper(current_user_data["facebook"]))
if current_user_data["linkedin"]:
    all_texts.update(linkedin_scraper(current_user_data["linkedin"]))
if current_user_data["twitter"]:
    all_texts.update(twitter_scraper(current_user_data["twitter"]))
print(all_texts)
# remove the ref

raise SystemExit


API_KEY = "AIzaSyD0Ky_uXkK_L1f2yzZkOWNdv8fxPgHM3Ns"

client = discovery.build(
    "commentanalyzer",
    "v1alpha1",
    developerKey=API_KEY,
    discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
    static_discovery=False,
)

analyze_request = {
    "comment": {"text": input()},
    "requestedAttributes": {"TOXICITY": {}},
}

response = client.comments().analyze(body=analyze_request).execute()
print(json.dumps(response, indent=2))


# send the mail
