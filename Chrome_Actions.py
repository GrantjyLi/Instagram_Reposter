#pip install selenium
#pip install webdriver-manager

import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

#loading files
with open('Insta_Tag_Names.json') as tagFile:
    tagData = json.load(tagFile)

with open('Host_Account.json') as accFile:
    accData = json.load(accFile)

#setting up Web Driver
options = Options()
options.add_experimental_option("detach", True) #leaves window open when done
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def loginInstagram():
    print("Logging in...")
    instagramURL = tagData["instagramURL"]
    driver.get(instagramURL) # opening up instagram

    try: # entering credentials and logging in
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

    #================THEY SUSPECT AUTOMATED BEHAVIOR=============
    try:
        dismissBTN = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, tagData["dismissBTNCSS"]))
        )
        dismissBTN.click()
    except NoSuchElementException:
        print("Didn't have to dismiss")
    #============================================================

    try:  # "save login" info pop-up might happen
        notNowBTN = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, tagData["notNowLoginBTNCSS"]))
        )
        notNowBTN.click()

    except NoSuchElementException:
        print("Login Already Saved")

    try: # "not-now" info pop-up might happen
        notNowNotifBTN = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, tagData["notNowNotifBTNCSS"]))
        )
        notNowNotifBTN.click()
    except NoSuchElementException:
        print("No Notification Pop-up")

    print("Logged In")

def uploadMedia():
    print("Uploading...")
    uploadBTN = driver.find_element(By.CSS_SELECTOR, tagData["postIcon"])

    for name in os.listdir("Media"):
        filePath = os.path.join(os.getcwd(), "Media", name)
        print(name + "===========")
        images = []
        videos = []

        uploadBTN.click()

        for file in os.listdir(os.path.join("Media", name)):
            fileType = os.path.splitext(file)[1]
            if fileType == '.mp4':
                videos.append(filePath + file)
            elif fileType == '.jpg':
                images.append(filePath + file)

        fileUpload = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, tagData["fileInput"]))
        )

        if len(videos) > 0:
            print(videos)

            fileUpload.send_keys("\n".join(videos))
        else:
            print(images)
            fileUpload.send_keys("\n".join(images))

        return

"""
getting each post and distinguishing it as a:
    image               1 x jpg
    image carousel      multiple jpg
    video               1 x mp4
    video carousel      multiple mp4
"""
# def getMedia():
#
#     for name in os.listdir("Media"):
#         print(name + "===========")
#         images = []
#         videos = []
#
#         for file in os.listdir(os.path.join("Media", name)):
#             fileType = os.path.splitext(file)[1]
#             if fileType == '.mp4':
#                 videos.append(file)
#             elif fileType == '.jpg':
#                 images.append(file)
#
#         if len(videos) > 0:
#             print(videos)
#         else:
#           print(images)