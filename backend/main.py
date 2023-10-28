from googleapiclient import discovery
import json

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
