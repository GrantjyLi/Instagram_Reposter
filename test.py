import instaloader

# Initialize Instaloader
L = instaloader.Instaloader()

# URL or shortcode of the Instagram post
post_url = 'https://www.instagram.com/p/CpQGUYWJQN1/'

# Extract the shortcode from the URL
shortcode = post_url.split('/')[-2]

# Load the post
post = instaloader.Post.from_shortcode(L.context, shortcode)

# Print the URL of the video
if post.is_video:
    print(f"Video URL: {post.video_url}")
else:
    print("The post is not a video")