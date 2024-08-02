#pip install instaloader

import instaloader # GOAT!!!!!!
import os
import json

victimData = {}
downloadLim = 0
victims = []
loader = None

def downloaderInit(options):
    global victimData, victims, loader, downloadLim

    # Initialize Instaloader
    loader = instaloader.Instaloader()

    with open('Victim_Data.json') as victimFile: # getting victim data folder
        victimData = json.load(victimFile)
    
    victims = options['victims']
    downloadLim = victimData["downloadLimit"]

    if not options['ecoMode']:
        try:
            loader.login(options["username"], options["password"])  # Avoid rate limit
        except instaloader.exceptions.LoginException as e:
            print("Login failed - Check:")
            print("- Username/Password")
            print("- Instagram Availability")

    #updating victimData with new data from posts
    with open('Host_Account.json', 'w') as hostFile:
        json.dump({'username': options["username"], 
                'password': options["password"]}, 
                hostFile, indent=4)
    
    #combining the list of victims from the file with the new ones
    victimData['victims'] = list(set(victimData['victims']).union(options['victims']))



def downloadAllAccounts():

    saveFolder = 'Media'
    os.makedirs(saveFolder, exist_ok=True)
    os.chdir(saveFolder)# making the working directory /Media for downloads

    for victim in victims:
        print("downloading from " + victim)
        downloadAccountMedia(victim)
        print("===========================================\n")

    os.chdir("../") # making the working directory back to the main

    #updating victimData with new data from posts
    with open('Victim_Data.json', 'w') as victimFile:
        json.dump(victimData, victimFile, indent=4)


def downloadAccountMedia(account):
    #global victimData

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

    victimData["stolenVictimData"][account] = postStolenData


#https://www.instagram.com/p/{SHORT_CODE_HERE}/
def downloadFromShortCode( shortcode):

    # Load + download the post
    post = instaloader.Post.from_shortcode(loader.context, shortcode)
    loader.download_post(post, shortcode)

    print("https://www.instagram.com/p/"+ shortcode +"/ downloaded")