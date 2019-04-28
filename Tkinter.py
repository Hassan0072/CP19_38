import tkinter
from tkinter import messagebox 
root = tkinter.Tk()


def ab():
	messagebox.showinfo("My Title","My Message")

B = tkinter.Button(root , text ="Hello" , command=ab)
B.pack()