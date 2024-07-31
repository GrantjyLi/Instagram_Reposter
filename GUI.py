import tkinter as tk

window = tk.Tk()
window.geometry("700x500")
window.title("Instagram Reposter")

HEADER_SIZE = 15
TEXT_SIZE = 12

nameslabel = tk.Label(window, text = "Victim Account Names:", font=('Arial', HEADER_SIZE))
nameslabel.place(x=10, y=10)

accNames = tk.Text(window, font=('Arial', TEXT_SIZE))
accNames.place(x=10, y = 35, width= 300, height=150)

# unEntry = tk.Entry(window, text = "Profile Account Names:", font=('Arial', HEADER_SIZE))
# pwEntry = tk.Entry(window, text = "Profile Account Names:", font=('Arial', HEADER_SIZE))
# unEntry.pack()
# pwEntry.pack()


window.mainloop()