from tkinter import *
root= Tk()
root.geometry("400x400")
T = Text(root, height=400, width=400)
T.pack()
T.insert(END,root)
root.mainloop()
