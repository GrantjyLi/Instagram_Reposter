#pip install instaloader

import instaloader # GOAT!!!!!!
import os
import json

with open('Victim_Data.json') as victimFile: # getting victim data folder
    victimData = json.load(victimFile)

with open('Host_Account.json') as accFile: # getting victim data folder
    accData = json.load(accFile)

# Initialize Instaloader
loader = instaloader.Instaloader()
loader.login(accData["accUsername"], accData["accPassword"]) # note necessary, but good to avoid rate limit

downloadLim = victimData["downloadLimit"]

def downloadAllAccounts():
    saveFolder = 'Media'
    os.makedirs(saveFolder, exist_ok=True)# making the working directory /Media for downloads
    os.chdir(saveFolder)

    victims = victimData["victimNames"]
    for victim in victims:
        print("downloading from " + victim)
        downloadAccountMedia(victim)
        print("===========================================\n")

    os.chdir("../") # making the working directory the main

    #updating victimData with new data from posts
    with open('Victim_Data.json', 'w') as victimFile:
        json.dump(victimData, victimFile, indent=2)


def downloadAccountMedia(account):
    profile = instaloader.Profile.from_username(loader.context, account)

    downloadCount = 0
    latestPostDate = None
    oldestPostGot = None

    for post in profile.get_posts():
        if downloadCount >= downloadLim:
            oldestPostGot = post.date.strftime('%Y-%m-%d %H:%M:%S')
            break
        elif downloadCount == 0:
            latestPostDate = post.date.strftime('%Y-%m-%d %H:%M:%S')

        downloadFromShortCode(post.shortcode)
        downloadCount +=1

    postStolenData = {}
    postStolenData["postsStolen"] = downloadCount
    postStolenData["lastestPostStolen"] = latestPostDate
    postStolenData["oldestPostStolen"] = oldestPostGot

    victimData[account] = postStolenData


#https://www.instagram.com/p/{SHORT_CODE_HERE}/
def downloadFromShortCode(shortcode):

    # Load + download the post
    post = instaloader.Post.from_shortcode(loader.context, shortcode)
    loader.download_post(post, shortcode)

    print("https://www.instagram.com/p/"+ shortcode +"/ downloaded")