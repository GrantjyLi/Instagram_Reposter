import tkinter as tk
import json
HEADER_SIZE = 15
TEXT_SIZE = 12

class GUI:

    def __init__(self, initRepost):
        self.initRepost = initRepost # call back function to main

        self.window = tk.Tk()
        self.window.geometry("700x500")
        self.window.title("Instagram Reposter")

        self.nameslabel = tk.Label(self.window, text = "Victim Account Names:", font = ('Arial', HEADER_SIZE))
        self.accNames = tk.Text(self.window, font = ('Arial', TEXT_SIZE))

        self.unEntry = tk.Entry(self.window, font = ('Arial', TEXT_SIZE))
        self.pwEntry = tk.Entry(self.window, font = ('Arial', TEXT_SIZE))

        self.unlabel = tk.Label(self.window, text = "Enter Account Username:", font = ('Arial', HEADER_SIZE))
        self.pwlabel = tk.Label(self.window, text = "Enter Account Password:", font = ('Arial', HEADER_SIZE))

        self.nameslabel.place(x = 10, y = 10)
        self.accNames.place(x = 10, y = 35, width = 300, height = 150)
        self.unlabel.place(x = 10, y = 195)
        self.unEntry.place(x = 10, y = 225)
        self.pwlabel.place(x = 10, y = 250)
        self.pwEntry.place(x = 10, y = 280)


        self.postDescLabel = tk.Label(self.window, text = "Automated Post Description:", font = ('Arial', HEADER_SIZE))
        self.postDesc = tk.Text(self.window, font = ('Arial', TEXT_SIZE))

        self.grabContent = tk.IntVar()
        self.autoUpload = tk.IntVar()
        self.ecoMode = tk.IntVar()

        self.grabContentCBTN = tk.Checkbutton(self.window, 
            text = "Grab Content", 
            variable = self.grabContent, 
            font = ('Arial', TEXT_SIZE))
        self.autoUploadCBTN = tk.Checkbutton(self.window, 
            variable = self.autoUpload, 
            text = "Automated Upload", 
            font = ('Arial', TEXT_SIZE))
        self.ecoModeCBTN = tk.Checkbutton(self.window, 
            variable = self.ecoMode, 
            text = "Economy Mode", 
            font = ('Arial', TEXT_SIZE))

        self.grabContentCBTN.select()
        self.autoUploadCBTN.select()
        self.ecoModeCBTN.select()

        self.startBTN = tk.Button(self.window, text = "Start", command = self.start, font = ('Arial', HEADER_SIZE))

        self.postDescLabel.place(x = 335, y= 10)
        self.postDesc.place(x = 335, y = 35, width = 350, height = 175)
        self.grabContentCBTN.place(x = 335, y = 210)
        self.autoUploadCBTN.place(x = 335, y = 235)
        self.ecoModeCBTN.place(x = 335, y = 260)
        self.startBTN.place(x = 520, y = 230, width = 125, height = 50)

        self.outputLabel = tk.Label(self.window, text = "Program Output", font = ('Arial', HEADER_SIZE))
        self.output = tk.Text(self.window, font = ('Arial', TEXT_SIZE))
        self.output.config(state = tk.DISABLED)

        self.outputLabel.place(x = 290, y = 290)
        self.output.place(x = 10, y = 320, width = 680, height = 170)

        self.window.mainloop()


    def start(self):
        self.GUIoutput("Running")

        options = {
            'victims' : self.accNames.get('1.0', tk.END).strip().split('\n'),
            'username' : self.unEntry.get(),
            'password' : self.pwEntry.get(),
            'postDesc' : self.postDesc.get('1.0', tk.END).strip(),
            'grabContent' : self.grabContent.get() ==  1,
            'autoUpload' : self.autoUpload.get() ==  1,
            'ecoMode' : self.ecoMode.get() ==  1,
        }
        

        self.GUIoutput(json.dumps(options, indent=4, sort_keys=True))

        self.initRepost(options)
    
    def GUIoutput(self, message):
        self.output.config(state=tk.NORMAL)
        self.output.insert(tk.END, message)
        self.output.insert(tk.END, '\n')
        self.output.config(state=tk.DISABLED)
        self.output.see(tk.END)