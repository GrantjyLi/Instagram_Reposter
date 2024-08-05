import json
import os

if os.path.exists("Save_Data.json"):
    with open('Save_Data.json') as saveData: # getting previous victim data folder
        setupData = json.load(saveData)
else:
    f = open("Save_Data.json", "a")
    f.close()

print(setupData)