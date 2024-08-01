#from Chrome_Actions import *
#from Content_Downloader import *

from GUI import GUI

#loginInstagram()
#downloadAllAccounts()
#uploadMedia()

#callback function passing to GUI
def initRepost(options):
    print(options)

gui = GUI(initRepost)
