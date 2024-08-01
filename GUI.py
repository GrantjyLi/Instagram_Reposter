import tkinter as tk

class GUI:
    def __init__(self):

        window = tk.Tk()
        window.geometry("700x500")
        window.title("Instagram Reposter")

        HEADER_SIZE = 15
        TEXT_SIZE = 12

        nameslabel = tk.Label(window, text = "Victim Account Names:", font=('Arial', HEADER_SIZE))

        accNames = tk.Text(window, font=('Arial', TEXT_SIZE))

        unEntry = tk.Entry(window, font=('Arial', TEXT_SIZE))
        pwEntry = tk.Entry(window, font=('Arial', TEXT_SIZE))

        unlabel = tk.Label(window, text = "Enter Account Username:", font=('Arial', HEADER_SIZE))
        pwlabel = tk.Label(window, text = "Enter Account Password:", font=('Arial', HEADER_SIZE))

        nameslabel.place(x = 10, y=10)
        accNames.place(x = 10, y = 35, width= 300, height=150)
        unlabel.place(x = 10, y = 195)
        unEntry.place(x = 10, y = 230)
        pwlabel.place(x = 10, y = 250)
        pwEntry.place(x = 10, y = 270)


        postDescLabel = tk.Label(window, text = "Automated Post Description:", font=('Arial', HEADER_SIZE))
        postDesc = tk.Text(window, font=('Arial', TEXT_SIZE))

        grabContent = tk.Checkbutton(window, text = "Grab Content", font=('Arial', TEXT_SIZE))
        autoUpload = tk.Checkbutton(window, text = "Automated Upload", font=('Arial', TEXT_SIZE))
        ecoMode = tk.Checkbutton(window, text = "Economy Mode", font=('Arial', TEXT_SIZE))

        autoUpload.select()
        grabContent.select()
        ecoMode.select()

        startBTN = tk.Button(window, text = "Start", font=('Arial', HEADER_SIZE))

        postDescLabel.place(x = 335, y=10)
        postDesc.place(x = 335, y = 35, width= 350, height=175)
        grabContent.place(x = 335, y = 215)
        autoUpload.place(x = 335, y = 240)
        ecoMode.place(x = 335, y = 265)
        startBTN.place(x = 520, y = 230, width = 125, height = 50)

        outputLabel = tk.Label(window, text = "Program Output", font=('Arial', HEADER_SIZE))
        output = tk.Text(window, font=('Arial', TEXT_SIZE))

        outputLabel.place(x = 290, y = 290)
        output.place(x = 10, y = 320, width = 680, height = 170)

        window.mainloop()