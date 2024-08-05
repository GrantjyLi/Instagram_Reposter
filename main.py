from Chrome_Actions import *
from downloaderV2 import *
from GUI import GUI

#callback function passing to GUI
def initRepost(data, gui):
    print(data)
    downloadData = {
        "victims" : data['victims'],
        "username" : data['username'],
        "password" : data['password'],
        "ecoMode" : data['ecoMode']
    }

    repostData = {
        "username" : data['username'],
        "password" : data['password'],
        "postDesc" : data['postDesc']
    }

    if data['grabContent']:
        if data['victims'] == ['']:
            gui.guiOut("Enter victim Names")
            return
        
        if not downloaderInit(downloadData, gui):
            return
        
        downloadAllAccounts()

    if data['autoUpload']:
        chromeActionsInit(repostData, gui)
        # loginInstagram()
        # uploadMedia()
    
    #saving menu options for next time
    with open('Save_Data.json', 'w') as hostFile:
        json.dump(data, hostFile, indent=4)

setupData = {}
with open('Victim_Data.json') as victimFile: # getting previous victim data folder
    setupData = json.load(victimFile)

gui = GUI(initRepost)

