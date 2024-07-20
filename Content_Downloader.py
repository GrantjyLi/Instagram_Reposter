#pip install instaloader

import instaloader # GOAT!!!!!!
import os

# Initialize Instaloader
loader = instaloader.Instaloader()
loader.login("justgrantnow", "mypw4Grant4GradeRep") # note necessary, but good to avoid rate limit

#https://www.instagram.com/p/{SHORT_CODE_HERE}/
def downloadFromShortCode(shortcode):
    saveFolder = 'Media'
    os.makedirs(saveFolder, exist_ok=True)
    os.chdir(saveFolder)

    # Load the post
    post = instaloader.Post.from_shortcode(loader.context, shortcode)
    loader.download_post(post, target= shortcode)

    print("https://www.instagram.com/p/"+ shortcode +"/ downloaded")

def downloadAccountMedia(account):
    profile = instaloader.Profile.from_username(loader.context, account)

    for post in profile.get_posts():
        print(post)
        print(post.date)