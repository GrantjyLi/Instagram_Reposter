#pip install instaloader

import instaloader
import os

# Initialize Instaloader
loader = instaloader.Instaloader()

# Extract the shortcode from the URL
# shortcode = post_url.split('/')[-2]

#https://www.instagram.com/p/{SHORT_CODE_HERE}/
def downloadFromShortCode(shortcode):
    saveFolder = 'Media'
    os.makedirs(saveFolder, exist_ok=True)
    os.chdir(saveFolder)

    # Load the post
    post = instaloader.Post.from_shortcode(loader.context, shortcode)
    loader.download_post(post, target= shortcode)

    print("https://www.instagram.com/p/"+ shortcode +"/ downloaded")

