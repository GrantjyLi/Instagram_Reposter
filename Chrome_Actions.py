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

accUsername = "justgrantnow"
accPassword = "mypw4Grant4GradeRep"

options = Options()
options.add_experimental_option("detach", True) #leaves window open when done

#part of setup
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

with open('Insta_Tag_Names.json') as file:
    tagData = json.load(file)

def loginInstagram():

    instagramURL = tagData["instagramURL"]
    driver.get(instagramURL)

    try:
        unInput = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, tagData["UNInputIdentifier"]))
        )
        pwInput = driver.find_element(By.CSS_SELECTOR, tagData["PWInputIdentifier"])
        loginBTN = driver.find_element(By.CSS_SELECTOR, tagData["loginBTNIdentifier"])

        unInput.send_keys(accUsername)
        pwInput.send_keys(accPassword)
        loginBTN.click()

        print("Loggin in")
    except NoSuchElementException:
        print("Cannot Load Instagram Login")

    try: # save login info pop-up might happen
        saveLoginBTN = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, tagData["saveBTNIdentifier"]))
        )
        print("Not saving Login")


    except NoSuchElementException:
        print("Login Already Saved")






