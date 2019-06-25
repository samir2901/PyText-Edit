from sys import *
import os
from tkinter import *
from tkinter import filedialog

filename = None

def newFile():
    print("Nothing....")

def openFile():
    global filename
    filename = filedialog.askopenfile(initialdir="/", title="Open", filetype=((("Text Files"),".txt"),(("All Files"),"*.*")))
    if filename == " ":
        filename = None
    else:
        root.title("PyText Edit-"+str(os.path.basename(filename)))
        text.delete(1.0,END)
        fp = open(filename,"r")
        text.insert(1.0,fp.read())
        fp.close()

def saveFile():
    print("Nothing....")

def saveasFile():
    print("Nothing....")

def exitEditor():
    exit()


def viewHelp():
    print("Nothing....")

def viewAbout():
    print("Nothing....")

#creating main window
root = Tk()
root.title("PyText Edit")
root.geometry("540x560")

#creating menu bar
menubar=Menu(root)
root.config(menu=menubar)

#creating file menu
file_menu=Menu(menubar)
file_menu.add_command(label="New", accelerator='Ctrl+N', command=newFile)
file_menu.add_command(label="Open", accelerator='Ctrl+O', command=openFile)
file_menu.add_command(label="Save", accelerator='Ctrl+S', command=saveFile)
file_menu.add_command(label="Save As", accelerator='Ctrl+Shift+N', command=saveasFile)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exitEditor)
menubar.add_cascade(label="File",menu=file_menu)

root.bind('<Control_L><N>', lambda event: newFile())
root.bind('<Control_L><o>', lambda event: openFile())
root.bind('<Control_L><s>', lambda event: saveFile())

#creating help menu
help_menu=Menu(menubar)
help_menu.add_command(label="View Help", command=viewHelp)
help_menu.add_separator()
help_menu.add_command(label="About", command=viewAbout)
menubar.add_cascade(label="Help", menu=help_menu)

text=Text(root)
text.pack(expand=True, fill=BOTH)
scrollbar = Scrollbar(text)
text.configure(yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview)
scrollbar.pack(side=RIGHT, fill=Y)

root.mainloop()
