#pip install selenium
#pip install webdriver-manager

import json
import os
import sys
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, TimeoutException

#loading files
tagData = {}
accData = {}
options = None
driver = None
waitTime = 0
gui = None
data = {}

def chromeActionsInit(postData, gui_instance):
    global tagData, accData, options, driver, waitTime, data, gui

    data = postData
    gui = gui_instance

    with open('Insta_Tag_Names.json') as tagFile:
        tagData = json.load(tagFile)

    with open('Host_Account.json') as accFile:
        accData = json.load(accFile)

    #setting up Web Driver
    options = Options()
    options.add_experimental_option("detach", True) #leaves window open when done
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    waitTime = tagData["elementWaitTime"] # seconds

    if not os.path.exists('Media'):
        gui.guiOut("No Downloaded Content")
        return

    #ADD a check for contents in /Media
    #REMOVE UNECESSARY FILE ACCESS for this


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
    else:
        sys.exit(0)

    #================THEY SUSPECT AUTOMATED BEHAVIOR=============
    #dismiss button
    dismissBTN = waitElementCSS(tagData["dismissBTN"], "1) Didn't have to dismiss")
    if dismissBTN:
        dismissBTN.click()
    #============================================================

    # "not-now" info pop-up might happen
    notNowNotifBTN = waitElementCSS(tagData["notNowNotifBTN"], "1) No Notification Pop-up")
    if notNowNotifBTN:
        notNowNotifBTN.click()

    # "not-now" info pop-up might happen
    dontSaveLoginBTN = waitElementCSS(tagData["dontSaveLoginBTN"], "1) Don't Save Login")
    if dontSaveLoginBTN:
        dontSaveLoginBTN.click()


def uploadMedia():
    print("Uploading...") # get upload button
    uploadBTN = waitElementCSS(tagData["postUploadSVG"], "1) Cannot Find upload button")

    for postName in os.listdir("Media"): # looping through each post in /Media
        print(postName)
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

    fileUpload = waitElementCSS(tagData["fileINPUT"], "Couldn't upload file")

    print("Files:")
    # if there are videos, it ignores all photos
    if len(videos) > 0:
        print(videos)
        fileUpload.send_keys("\n".join(videos))
    else:
        print(images)
        fileUpload.send_keys("\n".join(images))

    driver.implicitly_wait(3)
    # =============POSTING PROCESS =========================
    reelsBTN = waitElementCSS(tagData["postedAsReelsBTN"], "1) No Reel Informatics Pop-up") # if it is a reel
    if reelsBTN:
        reelsBTN.click()


    for i in range(3):
        driver.implicitly_wait(3)
        time.sleep(1)
        buttons = driver.find_elements(By.CSS_SELECTOR, tagData["uploadNextBTN"])

        for button in buttons:
            if button.text == 'Next' or (i == 2 and button.text == 'Share'):
                button.click()
                i += 1
                break


    print("Uploaded")

    closeSVG = waitElementCSS(tagData["closeUploadSVG"], "Couldn't exit upload")
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