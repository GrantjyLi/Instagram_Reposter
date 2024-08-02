#from Chrome_Actions import *
from downloaderV2 import *
from GUI import GUI

#callback function passing to GUI
def initRepost(options, gui):

    if options['grabContent']:
        if not downloaderInit(options, gui):
            return
        downloadAllAccounts()

    # if options['autoUpload']:
    #     loginInstagram()
    #     uploadMedia()


gui = GUI(initRepost)

