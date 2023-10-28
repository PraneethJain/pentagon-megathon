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

texts = set()
for _ in range(5):
    driver.find_element(By.TAG_NAME, "html").send_keys(Keys.END)
    time.sleep(2)
    res = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="tweetText"]')
    texts.update(stripped for el in res if (stripped:=el.text.strip()))

print(texts)
driver.close()
