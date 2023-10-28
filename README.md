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

# To Do:
- [x] App Logo
- [x] UI interface
- [x] Welcome Page, Registration Page
- [x] Push data to Realtime firebase
- [ ] Questions
- [ ] Score Calculation

# Purpose:
We built an app, that can be used for **personality based classification** and qualification criteria for job interviews. The final results are 
calculated in a model trained with ML.
This app has a basic **puzzle based test**, which is used for personality classification. The output of this test is sent to the database, where 
other phases of this **virtual interview**, based on **social media analysis** is calculated.

# Overview:
While building this app we've used **Android Studio** platform in **Kotlin** language.
