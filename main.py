from Chrome_Actions import *
from downloaderV2 import *
from GUI import GUI

import os
import json

#callback function passing to GUI
def initRepost(data, gui):
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
        elif downloaderInit(downloadData, gui):
            downloadAllAccounts()

    #if data['autoUpload']:
        #chromeActionsInit(repostData, gui)
        # loginInstagram()
        # uploadMedia()
    
    #saving menu options for next time
    with open('Save_Data.json', 'w') as hostFile:
        json.dump(data, hostFile, indent=4)


#check for previous data entered into GUI and load it
setupData = {
    'victims': [], 
    'username': '', 
    'password': '', 
    'postDesc': '', 
    'downloadLim': '', 
    'saveLogin': True, 
    'grabContent': False, 
    'autoUpload': False, 
    'ecoMode': False
}
if os.path.exists("Save_Data.json"):
    with open('Save_Data.json') as saveData:
        setupData = json.load(saveData)
else:
    with open('Save_Data.json', 'w') as setupFile:
        json.dump(setupData, setupFile, indent= 4)

gui = GUI(initRepost, setupData)

