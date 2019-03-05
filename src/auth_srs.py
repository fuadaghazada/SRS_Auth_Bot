import sys
import time

import config

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Opening the website of stars
driver = webdriver.Chrome()
driver.get("https://stars.bilkent.edu.tr/srs")

# Filling the ID field
id = driver.find_element_by_id("LoginForm_username")
id.clear()
id.send_keys(config.ID)
id.send_keys(Keys.TAB)

# Filling the Passfield
password = driver.find_element_by_css_selector("[id^='LoginForm-']")
password.send_keys(config.PASS)
password.send_keys(Keys.TAB)

# Finding the button for sign in
btn = driver.find_element_by_name("yt0")
btn.click()

time.sleep(2)
import auth_mail
print(auth_mail.code)

if(auth_mail.code):
    verf_field = driver.find_element_by_name("EmailVerifyForm[verifyCode]")
    verf_field.send_keys(auth_mail.code)
    v_btn = driver.find_element_by_name("yt0")
    v_btn.click()


#driver.close()
