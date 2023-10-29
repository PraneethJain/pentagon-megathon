import json

with open('result.json', 'r') as json_file:
    data = json.load(json_file)
print(data)

roles = {
    "Sales Representative": 0,
    "Front-End developer": 0,
    "Back-End developer": 0,
    "Human resource manager (HR)": 0,
    "Researcher (R&D)": 0,
    "Project Manager": 0,
    "Customer Service": 0,
}

# extraversion
extraversion = data["extraversion"]*100
if extraversion > 80:
    roles["Sales Representative"] += 1
elif extraversion > 70: 
    roles["Customer Service"] += 1
    roles["Human resource manager (HR)"] += 1
elif extraversion > 60: 
    roles["Projet Manager"] += 1
elif extraversion < 40:
    roles["Researcher (R&D)"] += 1

# agreeableness
agr = data["agreeableness"]*100
if agr > 80: 
    roles["Human resource manager (HR)"] += 1
elif agr > 60: 
    roles["Sales Representative"] += 1
elif agr < 40:
    roles["Project Manager"] += 1
    roles["Researcher (R&D)"] += 1

# Neuroticism
neu = data["neuroticism"]*100
if neu > 80:
    roles["Customer Service"] += 1
elif neu > 70:
    roles["Human resource manager (HR)"] += 1
elif neu < 30:
    roles["Back-End developer"] += 1
elif neu < 15:
    roles["Sales Representative"] += 1

# Conscientiousness 
con = data["conscientiousness"]*100
if con > 80:
    roles["Front-End developer"] += 1
elif con > 70:
    roles["Researcher (R&D)"] += 1

# Openness
op = data["openness"]*100
if op > 75:
    roles["Front-End developer"] += 1
    roles["Back-End developer"] += 1
elif op > 60:
    roles["Project Manager"] += 1

offered_jobs = sorted(roles, key=roles.get, reverse=True)[:2]
print(offered_jobs)
