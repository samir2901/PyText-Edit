'''
PyText Exit ver 1.0
Developed by Samiruddin Thunder.
June 25, 2019
'''
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

filename = None

def newFile():
    text.delete(0.0, END)
    print("New File Made")

def openFile():
    global filename
    filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Files","*.txt")])
    if filename == " ":
        filename = None
    else:
        f = open(filename,"r")
        t = f.read()
        text.delete(0.0,END)
        text.insert(0.0,t)
        print("File Opened")

def saveFile():
    global filename
    try:
        f = open(filename, "w")
        t = text.get(0.0, END)
        f.write(t)
        f.close()
        print("File Saved")
    except:
        saveasFile()

def saveasFile():
    f = filedialog.asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Files","*.txt")])
    t = text.get(0.0, END)
    try:
        fh = open(f,"w")
        fh.write(t.rstrip())
        fh.close()
        print("File Saved")
    except:
        messagebox.showerror(title="Oops!", message="Unable to save the file...")
        print("Unable to Save.")


def exitEditor():
    exit()


def viewHelp():
    helpWindow=Toplevel()
    helpWindow.title("Help-PyText Edit")
    helpWindow.geometry("300x110")
    helpWindow.config(background="yellow")
    helpLabel = Label(helpWindow,text="Help", font=("Britannic Bold", 20), bg="yellow").pack()
    details_help = Label(helpWindow,
        text="In this PyText Edit you can type anything\nSave it in any format\nOpen files in any format.",
        font=("Helvetica",12),
        bg="yellow",
    ).pack()
    print("Help Window Opened")

def viewAbout():
    aboutWindow=Toplevel()
    aboutWindow.title("About-PyText Edit")
    aboutWindow.geometry("300x190")
    aboutWindow.config(background="yellow")
    aboutLabel = Label(aboutWindow,text="About", font=("Britannic Bold", 20), bg="yellow").pack()
    details1_about = Label(aboutWindow,
        text="PyText Edit ver 1.0",
        font=("Helvetica",9),
        bg="yellow"
    ).pack()
    details2_about = Label(aboutWindow,
        text="PyText Edit is made using Python\nand its tkinter library.\nDeveloped by Samiruddin Thunder.\n\nAll of its source code is available at\n\'https://github.com/samir2901/PyText-Edit'.",
        font=("Helvetica",12),
        bg="yellow"
    ).pack()
    print("About Window Opened")


#creating main window
root = Tk()
root.title("PyText Edit")
root.geometry("540x560")

#creating menu bar
menubar=Menu(root)
root.config(menu=menubar)

#creating file menu
file_menu=Menu(menubar)
file_menu.add_command(label="New", command=newFile)
file_menu.add_command(label="Open", command=openFile)
file_menu.add_command(label="Save", command=saveFile)
file_menu.add_command(label="Save As", command=saveasFile)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exitEditor)
menubar.add_cascade(label="File",menu=file_menu)

#creating help menu
help_menu=Menu(menubar)
help_menu.add_command(label="View Help", command=viewHelp)
help_menu.add_separator()
help_menu.add_command(label="About", command=viewAbout)
menubar.add_cascade(label="Help", menu=help_menu)

text=Text(root)
text.pack(expand=True, fill=BOTH)

scrollbar_y = Scrollbar(text, orient='vertical')
text.configure(yscrollcommand=scrollbar_y.set)
scrollbar_y.config(command=text.yview)
scrollbar_y.pack(side=RIGHT, fill=Y)

root.mainloop()
