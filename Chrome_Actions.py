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

def loginInstagram():
    file = open('Insta_Tag_Names.json')
    tagData = json.load(file)

    instagramURL = "https://www.instagram.com/"
    driver.get(instagramURL)

    unInput = driver.find_element(By.CSS_SELECTOR, '[aria-label="Phone number, username, or email"]')
    pwInput = driver.find_element(By.CSS_SELECTOR, '[aria-label="Password"]')
    loginBTN = driver.find_element(By.CSS_SELECTOR, 'button._acap._acas._aj1-._ap30')

    unInput.send_keys(accUsername)
    pwInput.send_keys(accPassword)
    loginBTN.click()

    try: # save login info pop-up might happen
        saveLoginBTN = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button._acap._acas._aj1-._ap30"))
        )
        print("Not saving Login")


    except NoSuchElementException:
        print("Login Already Saved")


    file.close()



