import json

setupData = {}
with open('Victim_Data.json') as victimFile: # getting previous victim data folder
    setupData = json.load(victimFile)

print(setupData)