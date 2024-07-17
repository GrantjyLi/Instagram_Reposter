#pip install selenium
#pip install webdriver-manager

import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

with open('Insta_Tag_Names.json') as tagFile:
    tagData = json.load(tagFile)

with open('Accounts.json') as accFile:
    accData = json.load(accFile)

options = Options()
options.add_experimental_option("detach", True) #leaves window open when done

#part of setup
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def loginInstagram():
    print("Logging in")
    instagramURL = tagData["instagramURL"]
    driver.get(instagramURL)

    try:
        unInput = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, tagData["UNInputCSS"]))
        )
        pwInput = driver.find_element(By.CSS_SELECTOR, tagData["PWInputCSS"])
        loginBTN = driver.find_element(By.CSS_SELECTOR, tagData["loginBTNCSS"])

        unInput.send_keys(accData["accUsername"])
        pwInput.send_keys(accData["accPassword"])
        loginBTN.click()

    except NoSuchElementException:
        print("Cannot Load Instagram Login")
        return

    try:  # save login info pop-up might happen
        notNowBTN = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, tagData["notNowLoginBTNCSS"]))
        )
        notNowBTN.click()

    except NoSuchElementException:
        print("Login Already Saved")

    try:
        notNowNotifBTN = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, tagData["notNowNotifBTNCSS"]))
        )
        notNowNotifBTN.click()
    except NoSuchElementException:
        print("No Notification Pop-up")

    print("Logged In")


def downloadContent():
    print("Stealing Content...")

    for account in accData["victimAccounts"]:
        accURL = accData["accURLPrefix"] + account

        driver.get(accURL)