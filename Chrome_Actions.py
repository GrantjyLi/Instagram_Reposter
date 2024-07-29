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
def waitElementXPATH(tag, errorMessage):
    try:
        return WebDriverWait(driver, waitTime).until(
                EC.presence_of_element_located((By.XPATH, tag))
            )
    except TimeoutException or NoSuchElementException:
        print(errorMessage)
        return None

def loginInstagram():
    print("Logging in...")
    instagramURL = tagData["instagramURL"]
    driver.get(instagramURL) # opening up instagram

    #entering credentials and logging in
    unInput = waitElementXPATH(tagData["unINPUT"], "1) Cannot Load Instagram Login")
    if unInput:

        pwInput = driver.find_element(By.XPATH, tagData["pwINPUT"])
        loginBTN = driver.find_element(By.XPATH, tagData["loginBTN"])

        unInput.send_keys(accData["accUsername"])
        pwInput.send_keys(accData["accPassword"])
        loginBTN.click()
        print("0) Logged In")
    else:
        sys.exit(0)

    #================THEY SUSPECT AUTOMATED BEHAVIOR=============
    #dismiss button
    dismissBTN = waitElementXPATH(tagData["dismissBTN"], "1) Didn't have to dismiss")
    if dismissBTN:
        dismissBTN.click()
        print("0) Dismissed Automated behavior")
    #============================================================

    # "save login" info pop-up might happen
    notNowBTN = waitElementXPATH(tagData["notNowloginBTN"], "1) Login Already Saved")
    if notNowBTN:
        notNowBTN.click()
        print("0) No save Login")

    # "not-now" info pop-up might happen
    notNowNotifBTN = waitElementXPATH(tagData["notNowNotifBTN"], "1) No Notification Pop-up")
    if notNowNotifBTN:
        notNowNotifBTN.click()
        print("0) No notifications please")


def uploadMedia():
    print("Uploading...") # get upload button
    uploadBTN = waitElementXPATH(tagData["postIconSVG"], "1) Cannot Find upload button")

    for postName in os.listdir("Media"): # looping through each post in /Media
        print(postName + "===========")
        uploadBTN.click()

        uploadPost(postName)
def uploadPost(name):
    filePath = os.path.join(os.getcwd(), "Media", name)  # getting file path
    images = []  # collecting images and videos of the post
    videos = []

    # looping through each file from the post
    for file in os.listdir(os.path.join("Media", name)):
        fileType = os.path.splitext(file)[1]
        if fileType == '.mp4':
            videos.append(os.path.join(filePath, file))
        elif fileType == '.jpg':
            images.append(os.path.join(filePath, file))

    fileUpload = waitElementXPATH(tagData["fileINPUT"], "Couldn't upload file")

    # if there are videos, it ignores all photos
    if len(videos) > 0:
        print(videos)
        fileUpload.send_keys("\n".join(videos))
    else:
        print(images)
        fileUpload.send_keys("\n".join(images))

    # =============POSTING PROCESS =========================
    reelsBTN = waitElementXPATH(tagData["postedAsReelsBTN"], "Couldn't process Reel") # if it is a reel
    if reelsBTN:
        reelsBTN.click()

    i = 0
    driver.implicitly_wait(5)
    while i < 3:
        uploadBTN = waitElementXPATH(tagData["uploadNextBTN"], "Cannot upload: phase #" + str(i))
        if uploadBTN:
            uploadBTN.click()
            i += 1
            driver.implicitly_wait(3)
        driver.refresh()

    print("Uploaded")

    closeSVG = waitElementXPATH(tagData["closeUploadSVG"], "Couldn't exit upload")
    if closeSVG:
        closeSVG.click()
    # ========================================================

"""
getting each post and distinguishing it as a:
    image               1 x jpg
    image carousel      multiple jpg
    video               1 x mp4
    video carousel      multiple mp4

my code will manuall loop through all files to figure out which type of post it is
but instaloader does can return the post types: image, video, sidecar(carousel)

since i need to distinguish between image and video carousel, I made my own filter method
"""