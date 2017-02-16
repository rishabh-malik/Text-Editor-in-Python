from tkinter import *
import pyautogui as pg
def doNothing():
    print("Ok")
root= Tk()
root.title("Notepad By Rishabh")
root.geometry("400x400")

def about():
    str="this is a test editor made by Rishabh"
    T.insert(END,str)

def cut():
    pg.hotkey('ctrl','x')

def paste():
    pg.hotkey('ctrl', 'v')

def copy():
    pg.hotkey('ctrl', 'c')

def save():
    file= open("file","w")
    file.write(T.get("1.0",END))
    file.close()


def new():
    T.delete(0.0,20.0)
menubar = Menu(root)

# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Save", command=save)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# create more pulldown menus
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut",command=cut)
editmenu.add_command(label="Copy",command=copy)
editmenu.add_command(label="Paste",command=paste)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About",command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
root.config(menu=menubar)

T = Text(root, height=400, width=400)
T.pack()
T.insert(END,root)



root.mainloop()
