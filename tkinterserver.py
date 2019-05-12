from tkinter import *

root = Tk()


topFrame= Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
# label_1=Label(root, text="IP")
# label_2=Label(root, text="Port")
# entry_1=Entry(root)
# entry_2=Entry(root)

# label_1.grid(row=0)
# label_2.grid(row=1)

# entry_1.grid(row=0,column=1)
# entry_2.grid(row=1,column=1)



button1 = Button(topFrame, text="Button 1", fg="blue")
button2 = Button(topFrame, text="Button 2", fg="red")
button3 = Button(topFrame, text="Button 3", fg="green")
button4 = Button(bottomFrame, text="Button 4", fg="red")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()