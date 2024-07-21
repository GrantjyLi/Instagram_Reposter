#pip install instaloader

import instaloader # GOAT!!!!!!
import os
import json

with open('Victim_Accounts.json') as victimFile: # getting victim data folder
    victimData = json.load(victimFile)

with open('Host_Account.json') as accFile: # getting victim data folder
    accData = json.load(accFile)

saveFolder = 'Media'
os.makedirs(saveFolder, exist_ok=True) # making the default download folder Media
os.chdir(saveFolder)

# Initialize Instaloader
loader = instaloader.Instaloader()
loader.login(accData["accUsername"], accData["accPassword"]) # note necessary, but good to avoid rate limit

downloadLim = 2

def downloadAllAccounts():
    victims = victimData["victimNames"]
    for victim in victims:
        print("downloading from " + victim)
        downloadAccountMedia(victim)

def downloadAccountMedia(account):
    profile = instaloader.Profile.from_username(loader.context, account)

    downloadCount = 0

    for post in profile.get_posts():
        if downloadCount >= downloadLim:
            break

        downloadFromShortCode(post.shortcode)
        downloadCount +=1

#https://www.instagram.com/p/{SHORT_CODE_HERE}/
def downloadFromShortCode(shortcode):

    # Load + download the post
    post = instaloader.Post.from_shortcode(loader.context, shortcode)
    loader.download_post(post, shortcode)

    print("https://www.instagram.com/p/"+ shortcode +"/ downloaded")