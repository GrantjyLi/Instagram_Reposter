#from Chrome_Actions import *
from Content_Downloader import *

from GUI import GUI

#loginInstagram()

#uploadMedia()

#callback function passing to GUI
def initRepost(options):
    downloader = Content_Downloader(options)
    print(options)
    downloader.downloadAllAccounts()

gui = GUI(initRepost)
