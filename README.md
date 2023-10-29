# Overview

Psyche-Screener is a tool that emulates an interview screening process, which has the following rounds in it

- Round 1: Using social handles
    - Pass 1: Sanity test (Perspective API)
    - Pass 2: Social media check (NLTK)
- Round 2: Personality test
    - ‘OCEAN’ mapper
    - Sitation-based Interview
    - Puzzles
    - Lifestyle Choices
 
# Presentation

[Link](https://www.canva.com/design/DAFymxQKgcs/4a007JTePaNkvv6ApfhyLQ/edit?utm_content=DAFymxQKgcs&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

# Installation Instructions

## Backend

- `cd backend`
= (Optional) Create a virtual environment for this project. `python3 -m venv venv`
- (Optional) Activate the virtual environment. `source venv/bin/activate` on linux.
- Install dependencies. `pip install -r requirements.txt`
- Add your GCP Service API JSON file in `main.py`
- Run the server using `python3 main.py`

This will listen to requests from the clients (the web and android apps). Upon
receiving one, it will scrape the social media links and send a mail to the
client regarding the response.


# Mid Report

We are scraping three social media sites:
- LinkedIn
- Twitter
- Facebook

We collect all recent posts by the user and merge them. In the first pass, we
use **Perspective API** to assign each applicant a `toxicity_index`, which is
a float between 0 and 1. If this value is greater than 0.8, we directly reject
the applicant. If it is between 0.5 and 0.8, we ask the employer for manual
checking. Otherwise, the applicant is good to go for further screening. Then,
in the second pass, we are dividing the applicant's personality into the Big 5
classification (OCEAN classification). We use the outputs of these results to
find a suitable role.

# Purpose:

We built an app, that can be used for **personality based classification** and qualification criteria for job interviews. The final results are 
calculated in a model trained with the Naïve Bayes classifier.
This app has a basic **puzzle based test**, which is used for personality classification. The output of this test is sent to the database, where 
other phases of this **virtual interview**, based on **social media analysis** is calculated.

# To Do:
- [x] App Logo
- [x] UI interface
- [x] Welcome Page, Registration Page
- [x] Push data to Realtime firebase
- [x] Questions
- [x] Score Calculation
- [x] Presentation
- [x] Email sending through GCP
- [x] Make a good requirements.txt so that it can be run by testers
- [x] Installation Documentation


