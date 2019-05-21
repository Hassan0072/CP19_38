from tkinter import *
from PIL import Image, ImageTk
from time import ctime
import time
h_root=Tk()

#Geometry (width x height) 
h_root.geometry("400x400")



#width , height
# minimum size
h_root.minsize(400,400)


#maximum size
h_root.maxsize(0,400)

# Label
# bg : background color
# fg : foreground color
# font
# border style:
# 1) SUNKEN
# 2) GROOVE
# 3) RAISED
# 4) RIDGE

label=Label(text="GUI of Remote System File Viewer", bg="dark blue", fg="white", font="comicsansms 12 bold", borderwidth=3 , relief=GROOVE)

# Important pack option

# (anchor = "ne")
# (anchor = "nw")
# side = bottom , top , right , left
# label.pack(side=BOTTOM , anchor="ne")

# fill=X or fill=Y
# pad x
# pad y
# padding x axis or y axis 





label.pack(fill=X)
label =Label( text="Server Software ", font="comicsanms 12 bold",bg="black",fg="White" , borderwidth=3 , relief=GROOVE)
label.pack(side=LEFT , anchor="nw" , pady=5 , padx=5)

#______________________________________________________________________________________________________________





#_____________________________ENTRY WIDGET & GRID LAYOUT_______________________________________________________



    
    



#______________________ENTRY WIDGET________________________________________________________________________________________

userentry = StringVar()
passentry = StringVar()

userentry = Entry(h_root, textvariable = userentry)
passentry = Entry(h_root, textvariable = passentry)
userentry.pack()
passentry.pack()


#_____________________BUTTONS________________________________________________________

f1=Frame(h_root, borderwidth=3   , relief=SUNKEN)
f1.pack(side=LEFT , anchor="se", padx=5, pady=20)

f2=Frame(h_root, borderwidth=3   , relief=SUNKEN)
f2.pack(side=LEFT , anchor="se", padx=5, pady=20)

f3=Frame(h_root, borderwidth=3   , relief=SUNKEN)
f3.pack(side=LEFT , anchor="se", padx=5, pady=20)

b1=Button(f1 , fg="black" , text="Connect" , font="comicsansms 10 bold ")
b1.pack()

b2=Button(f2 , fg="black" , text="Disconnect" , font="comicsansms 10 bold ")
b2.pack()

b3=Button(f3 , fg="black" , text="Browse" , font="comicsansms 10 bold ")
b3.pack()







h_root.title("Server")

h_root.mainloop()