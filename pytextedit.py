from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)
    print("New File Made")

def openFile():
    f = filedialog.askopenfile(mode="r")
    t = f.read()
    text.delete(0.0,END)
    text.insert(0.0,t)
    print("Nothing....")

def saveFile():
    global filename
    t = text.get(0.0, END)
    f = open(filename, "w")
    f.write(t)
    f.close()
    print("Nothing....")

def saveasFile():
    f = filedialog.asksaveasfile(mode="w",defaultextension=".txt")
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        messagebox.showerror(title="Oops!", message="Unable to save the file...")
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

scrollbar_y = Scrollbar(text)
text.configure(yscrollcommand=scrollbar_y.set)
scrollbar_y.config(command=text.yview)
scrollbar_y.pack(side=RIGHT, fill=Y)

root.mainloop()
