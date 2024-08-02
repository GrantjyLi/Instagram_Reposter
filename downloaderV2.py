#pip install instaloader

import instaloader # GOAT!!!!!!
import os
import json

#global variables
victimData = {} # data about all victims
downloadLim = 0 # number of posts to download from each victim
victims = []    # list of victim accounts
loader = None   #instaloader object
gui = None

def downloaderInit(repostData, gui_instance):
    global victimData, victims, loader, downloadLim, gui
    gui = gui_instance

    # Initialize Instaloader
    loader = instaloader.Instaloader()

    with open('Victim_Data.json') as victimFile: # getting previous victim data folder
        victimData = json.load(victimFile)
    
    victims = repostData['victims']
    downloadLim = victimData["downloadLimit"]

    #log in with instaloader
    if not repostData['ecoMode']:
        try:
            loader.login(repostData["username"], repostData["password"])  # Avoid rate limit
            gui.guiOut("Instaloader Loggin in")
            gui.guiOut(json.dumps(repostData, indent=4, sort_keys=True))
        except instaloader.exceptions.LoginException:
            gui.guiOut("Login failed - Check:")
            gui.guiOut("- Username/Password")
            gui.guiOut("- Instagram Availability")
            gui.guiOut("\nLog in with specified account to resolve disturbances")
            return False

    #updating victimData with new data from posts
    with open('Host_Account.json', 'w') as hostFile:
        json.dump({'username': repostData["username"], 
                'password': repostData["password"]}, 
                hostFile, indent=4)
    
    #combining the list of victims from the file with the new ones
    victimData['victims'] = list(set(victimData['victims']).union(repostData['victims']))

    return True



def downloadAllAccounts():
    saveFolder = 'Media'
    os.makedirs(saveFolder, exist_ok=True)
    os.chdir(saveFolder)# making the working directory /Media for downloads

    for victim in victims:
        gui.guiOut("Stealing from " + victim + ":")
        downloadAccountMedia(victim)
        gui.guiOut("===========================================\n")

    os.chdir("../") # making the working directory back to the main

    #updating victimData with new data from posts
    with open('Victim_Data.json', 'w') as victimFile:
        json.dump(victimData, victimFile, indent=4)


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

    victimData["stolenVictimData"][account] = postStolenData


#https://www.instagram.com/p/{SHORT_CODE_HERE}/
def downloadFromShortCode( shortcode):
    # Load + download the post
    post = instaloader.Post.from_shortcode(loader.context, shortcode)
    loader.download_post(post, shortcode)

    gui.guiOut("Downloaded: https://www.instagram.com/p/"+ shortcode)