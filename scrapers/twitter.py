from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

URL = "https://twitter.com/LisaTalia"
USERNAME = "bhaskarsqusre"
PASSWORD = "scrapekaruisaccountse123@"

driver = webdriver.Firefox()
driver.get("https://twitter.com/i/flow/login")
wait = WebDriverWait(driver, 30)
email_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input")))
email_field.send_keys(USERNAME)
email_field.send_keys(Keys.RETURN)
pass_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
pass_field.send_keys(PASSWORD)
pass_field.send_keys(Keys.RETURN)

time.sleep(5)
driver.get(URL)
time.sleep(5)

for _ in range(5):
    driver.find_element(By.TAG_NAME, "html").send_keys(Keys.END)
    time.sleep(2)

raise SystemExit





SCROLL_PAUSE_TIME = 1
driver.find_element(By.CSS_SELECTOR, 'html').send_keys(Keys.END)
last_height = driver.execute_script("return document.body.scrollHeight")
while 1:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element(By.CSS_SELECTOR, "button.artdeco-button.artdeco-button--muted.artdeco-button--1.artdeco-button--full.artdeco-button--secondary.ember-view.scaffold-finite-scroll__load-button").click()
        except:
            break
    last_height = new_height


res = driver.find_elements(By.CSS_SELECTOR, 'span[dir="ltr"]')
num_posts = len(res)
original_posts = []
reposts = []
for i in range(0, num_posts, 2):
    posted_by = res[i].text.splitlines()[0].strip()
    if posted_by == profile_name:
        original_posts.append(res[i + 1].text.strip())
    else:
        reposts.append(res[i + 1].text.strip())

print(original_posts)
print(reposts)
driver.close()
