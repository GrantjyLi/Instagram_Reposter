#pip install instaloader

import instaloader # GOAT!!!!!!
import os
import json

class Content_Downloader:
    def __init__(self, options):
        # Initialize Instaloader
        self.loader = instaloader.Instaloader()

        self.victimData = {}
        self.downloadLim = 0
        self.victims = []

        with open('Victim_Data.json') as victimFile: # getting victim data folder
            self.victimData = json.load(victimFile)
        
        self.victims = options['victims']

        self.downloadLim = self.victimData["downloadLimit"]

        if not options['ecoMode']:
            try:
                self.loader.login(options["username"], options["password"])  # Avoid rate limit
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
        self.victimData['victims'] = list(set(self.victimData['victims']).union(options['victims']))



    def downloadAllAccounts(self):
        saveFolder = 'Media'
        os.makedirs(saveFolder, exist_ok=True)
        os.chdir(saveFolder)# making the working directory /Media for downloads

        for victim in self.victims:
            print("downloading from " + victim)
            self.downloadAccountMedia(victim)
            print("===========================================\n")

        os.chdir("../") # making the working directory back to the main

        #updating victimData with new data from posts
        with open('Victim_Data.json', 'w') as victimFile:
            json.dump(self.victimData, victimFile, indent=4)


    def downloadAccountMedia(self, account):
        profile = instaloader.Profile.from_username(self.loader.context, account)

        downloadCount = 0
        latestPostDate = None
        oldestPostGot = None

        for post in profile.get_posts():
            if downloadCount >= self.downloadLim:
                oldestPostGot = post.date.strftime('%Y-%m-%d %H:%M:%S')
                break
            elif downloadCount == 0:
                latestPostDate = post.date.strftime('%Y-%m-%d %H:%M:%S')

            self.downloadFromShortCode(post.shortcode)
            downloadCount +=1

        postStolenData = {}
        postStolenData["postsStolen"] = downloadCount
        postStolenData["lastestPostStolen"] = latestPostDate
        postStolenData["oldestPostStolen"] = oldestPostGot

        self.victimData["stolenVictimData"][account] = postStolenData


    #https://www.instagram.com/p/{SHORT_CODE_HERE}/
    def downloadFromShortCode(self, shortcode):

        # Load + download the post
        post = instaloader.Post.from_shortcode(self.loader.context, shortcode)
        self.loader.download_post(post, shortcode)

        print("https://www.instagram.com/p/"+ shortcode +"/ downloaded")