from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

URL = "https://www.facebook.com/profile.php?id=100093576190292"
EMAIL = "vreal7505@gmail.com"
PASSWORD = "scrapekaruisaccountse123@"

driver = webdriver.Firefox()
driver.get("http://facebook.com")
wait = WebDriverWait(driver, 30)
email_field = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
email_field.send_keys(EMAIL)
pass_field = wait.until(EC.visibility_of_element_located((By.NAME, "pass")))
pass_field.send_keys(PASSWORD)
pass_field.send_keys(Keys.RETURN)

time.sleep(5)
driver.get(URL)
time.sleep(5)


texts = set()
SCROLL_PAUSE_TIME = 2
last_height = driver.execute_script("return document.body.scrollHeight")
while 1:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    div_els = driver.find_elements(By.CSS_SELECTOR, 'div[dir="auto"]')
    texts.update([el.text for el in div_els if el.text])
print(texts)

driver.quit()
