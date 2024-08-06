import tkinter as tk
HEADER_SIZE = 15
TEXT_SIZE = 12

class GUI:

    def isInteger(self, keyInput):
        return keyInput.isdigit() or keyInput == ""

    def __init__(self, initRepost, setupData):

        self.initRepost = initRepost # call back function to main

        root = tk.Tk()
        root.geometry("700x700")
        root.title("Instagram Reposter")

        self.nameslabel = tk.Label(root, text = "Victim Account Names:", font = ('Arial', HEADER_SIZE))
        self.accNames = tk.Text(root, font = ('Arial', TEXT_SIZE))
        self.accNames.insert(tk.END, "\n".join(setupData['victims']))

        self.unlabel = tk.Label(root, text = "Enter Account Username:", font = ('Arial', HEADER_SIZE))
        self.pwlabel = tk.Label(root, text = "Enter Account Password:", font = ('Arial', HEADER_SIZE))

        self.unEntry = tk.Entry(root, font = ('Arial', TEXT_SIZE), 
            textvariable = tk.StringVar(value = setupData['username'])
        )
        self.pwEntry = tk.Entry(root, font = ('Arial', TEXT_SIZE), 
            textvariable = tk.StringVar(value = setupData['password'])
        )

        vcmd = (root.register(self.isInteger), '%P') # to only let integer input keys
        self.limitLabel = tk.Label(root, text = "Download Limit (from each Account):", font = ('Arial', TEXT_SIZE))
        self.downloadLim = tk.Entry(root, font = ('Arial', TEXT_SIZE), 
            validate='key', 
            validatecommand=vcmd, 
            textvariable = tk.StringVar(value = setupData['downloadLim'])
        )

        self.saveLogin = tk.IntVar(value = setupData['saveLogin'])

        self.saveLoginCBTN = tk.Checkbutton(root, 
            text = "Save Login", 
            variable = self.saveLogin, 
            font = ('Arial', TEXT_SIZE))

        self.nameslabel.place(x = 10, y = 10)
        self.accNames.place(x = 10, y = 35, width = 300, height = 150)
        self.unlabel.place(x = 10, y = 195)
        self.unEntry.place(x = 10, y = 225)
        self.saveLoginCBTN.place(x = 200, y = 220)
        self.pwlabel.place(x = 10, y = 250)
        self.pwEntry.place(x = 10, y = 280)
        self.limitLabel.place(x = 10, y = 305)
        self.downloadLim.place(x = 10, y = 335)

        self.postDescLabel = tk.Label(root, text = "Automated Post Description:", font = ('Arial', HEADER_SIZE))
        self.postDesc = tk.Text(root, font = ('Arial', TEXT_SIZE))
        self.postDesc.insert(tk.END, setupData['postDesc'])

        self.grabContent = tk.IntVar(value = setupData['grabContent'])
        self.autoUpload = tk.IntVar(value = setupData['autoUpload'])
        self.ecoMode = tk.IntVar(value = setupData['ecoMode'])

        self.grabContentCBTN = tk.Checkbutton(root, 
            text = "Grab Content", 
            variable = self.grabContent, 
            font = ('Arial', TEXT_SIZE))
        self.autoUploadCBTN = tk.Checkbutton(root, 
            variable = self.autoUpload, 
            text = "Automated Upload", 
            font = ('Arial', TEXT_SIZE))
        self.ecoModeCBTN = tk.Checkbutton(root, 
            variable = self.ecoMode, 
            text = "Economy Mode", 
            font = ('Arial', TEXT_SIZE))

        self.startBTN = tk.Button(root, text = "Start", command = self.start, font = ('Arial', HEADER_SIZE))

        self.postDescLabel.place(x = 335, y= 10)
        self.postDesc.place(x = 335, y = 35, width = 350, height = 175)
        self.grabContentCBTN.place(x = 335, y = 210)
        self.autoUploadCBTN.place(x = 335, y = 235)
        self.ecoModeCBTN.place(x = 335, y = 260)
        self.startBTN.place(x = 520, y = 230, width = 125, height = 50)

        self.outputLabel = tk.Label(root, text = "Program Output", font = ('Arial', HEADER_SIZE))
        self.output = tk.Text(root, font = ('Arial', TEXT_SIZE))
        self.output.config(state = tk.DISABLED)

        self.outputLabel.place(x = 290, y = 360)
        self.output.place(x = 10, y = 390, width = 680, height = 170)

        root.mainloop()


    def start(self):
        data = {
            'victims' : self.accNames.get('1.0', tk.END).strip().split('\n'),
            'username' : self.unEntry.get(),
            'password' : self.pwEntry.get(),
            'postDesc' : self.postDesc.get('1.0', tk.END).strip(),
            'downloadLim' : self.downloadLim.get(),
            'saveLogin' : self.saveLogin.get() == 1,
            'grabContent' : self.grabContent.get() ==  1,
            'autoUpload' : self.autoUpload.get() ==  1,
            'ecoMode' : self.ecoMode.get() ==  1,
        }

        self.guiOut("Running...")
        self.initRepost(data, self)
        
    
    def guiOut(self, message):
        self.output.config(state=tk.NORMAL)
        self.output.insert(tk.END, message)
        self.output.insert(tk.END, '\n')
        self.output.config(state=tk.DISABLED)
        self.output.see(tk.END)