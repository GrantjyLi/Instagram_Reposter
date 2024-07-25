#pip install selenium
#pip install webdriver-manager

import json
import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, TimeoutException

#loading files
with open('Insta_Tag_Names.json') as tagFile:
    tagData = json.load(tagFile)

with open('Host_Account.json') as accFile:
    accData = json.load(accFile)

#setting up Web Driver
options = Options()
options.add_experimental_option("detach", True) #leaves window open when done
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

waitTime = tagData["elementWaitTime"] # seconds
#helper function to get elements that have to be waited
def waitElementCSS(tag, errorMessage):
    try:
        return WebDriverWait(driver, waitTime).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, tag))
            )
    except TimeoutException or NoSuchElementException:
        print(errorMessage)
        return None

def loginInstagram():
    print("Logging in...")
    instagramURL = tagData["instagramURL"]
    driver.get(instagramURL) # opening up instagram

    #entering credentials and logging in
    unInput = waitElementCSS(tagData["unINPUT"], "1) Cannot Load Instagram Login")
    if unInput:

        pwInput = driver.find_element(By.CSS_SELECTOR, tagData["pwINPUT"])
        loginBTN = driver.find_element(By.CSS_SELECTOR, tagData["loginBTN"])

        unInput.send_keys(accData["accUsername"])
        pwInput.send_keys(accData["accPassword"])
        loginBTN.click()
        print("0) Logged In")
    else:
        print("1) Cannot load Instagram")
        sys.exit(0)

    #================THEY SUSPECT AUTOMATED BEHAVIOR=============
    #dismiss button
    dismissBTN = waitElementCSS(tagData["dismissBTN"], "1) Didn't have to dismiss")
    if dismissBTN:
        dismissBTN.click()
        print("0) Dismissed Automated behavior")
    #============================================================

    # "save login" info pop-up might happen
    notNowBTN = waitElementCSS(tagData["notNowloginBTN"], "1) Login Already Saved")
    if notNowBTN:
        notNowBTN.click()
        print("0) No save Login")

    # "not-now" info pop-up might happen
    notNowNotifBTN = waitElementCSS(tagData["notNowNotifBTN"], "1) No Notification Pop-up")
    if notNowNotifBTN:
        notNowNotifBTN.click()
        print("0) No notifications please")


def uploadMedia():
    print("Uploading...") # get upload button
    uploadBTN = driver.find_element(By.CSS_SELECTOR, tagData["postIconSVG"])

    for name in os.listdir("Media"): # looping through each post in /Media
        filePath = os.path.join(os.getcwd(), "Media", name) # getting file path
        print(name + "===========")
        images = [] # collecting images and videos of the post
        videos = []

        uploadBTN.click()

        # looping through each file from the post
        for file in os.listdir(os.path.join("Media", name)):
            fileType = os.path.splitext(file)[1]
            if fileType == '.mp4':
                videos.append(os.path.join(filePath, file))
            elif fileType == '.jpg':
                images.append(os.path.join(filePath, file))

        fileUpload = waitElementCSS(tagData["fileINPUT"], "Couldn't upload file")

        #if there are videos, it ignores all photos
        if len(videos) > 0:
            print(videos)
            fileUpload.send_keys("\n".join(videos))
        else:
            print(images)
            fileUpload.send_keys("\n".join(images))

        #=============POSTING PROCESS =========================
        reelsBTN = waitElementCSS(tagData["postedAsReelsBTN"], "Couldn't process Reel")
        if reelsBTN:
            reelsBTN.click()

        for i in range(3):
            uploadBTN = waitElementCSS(tagData["uploadNextBTN"], "Cannot upload: phase #" + str(i))
            if uploadBTN:
                uploadBTN.click()

        print("Uploaded")

        closeSVG = waitElementCSS(tagData["closeUploadSVG"], "Couldn't exit upload")
        if closeSVG:
            closeSVG.click()
        #========================================================

"""
getting each post and distinguishing it as a:
    image               1 x jpg
    image carousel      multiple jpg
    video               1 x mp4
    video carousel      multiple mp4
"""