from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("message box")
root.geometry("400x400")
def msg():
    messagebox.askquestion("question box","do you want to scan for virus?")
button = Button(root,text = "scan for virus",command = msg)
button.pack()
root.mainloop()