from tkinter import *
from tkinter import messagebox
from socket import *
import _thread
largefont=("berdana",12)
root = Tk()
root.title("Remote File Sharing System")
root.geometry("900x630")
root.minsize(width=500 , height=500)
topFrame = Frame(root)
bottomFrame = Frame(root)
theLabel = Label(root, text="Remote File Sharing System (User Interface)",bg="black",fg="white",font="Times 22",width=70)
theLabel.grid(row=0, column=0, columnspan=2, padx=8, pady=8, sticky="NSNESWSE")
#theLabel2 = Label(root, text="Server",fg="blue",font="Time 25",width=10,height=2)
#theLabel2.grid()

topFrame.grid(row=50,column=50)
bottomFrame.grid(row=10,column=10)
#root.configure(width=600,height=800)

import socket
s= socket.socket()
host = socket.gethostname()
port= 8080
s.bind((host,port))
s.listen(1)

label = Label(root, text="Server Software ", font=",16",bg="blue",fg="White",width=30)
label.grid(row=1, column=0,columnspan=2, padx=8, pady=8, sticky="NSNESWSE")

l_host=Label(root,text="Enter Host NAME")
l_host.grid(row=2, column=0, padx=8, pady=8, sticky="NSNESWSE")

e_host=Entry(root)
e_host.grid(row=2, column=1, columnspan=2, padx=8, pady=8, sticky="NSNESWSE")
e_host.insert(END,'127.0.0.1')


l_port=Label(root,text="Enter Port")
l_port.grid(row=3, column=0, padx=8, pady=8, sticky="NSNESWSE")

e_port=Entry(root)
e_port.grid(row=3, column=1, columnspan=2, padx=8, pady=8, sticky="NSNESWSE")
e_port.insert(END,12121)

message_label=Label(root,text="Client Message",font=("Arial,12"))
message_label.grid(row=4,column=0,columnspan=3,padx=10,pady=10,sticky="NSEW")


scrollbar_y = Scrollbar(root)
scrollbar_y.grid(row=5, column=3,rowspan=6)

show_1=Text(root,height=8, width=35, yscrollcommand=scrollbar_y.set,
                       bg="Grey",fg="White")
show_1.grid(row=5, column=0,rowspan=3,columnspan=3,sticky="NSEW")

b_connect=Button(root,text=" Connect")
b_connect.grid(row=14,column=0,padx=10,pady=10,sticky="nsew")

b_disconnect=Button(root,text=" disconnect")
b_disconnect.grid(row=14,column=1,padx=10,pady=10,sticky="nsew")
def connect():
            # CONNECT COM PORT
            print(e_host.get())
            e_host_v=e_host.get()
            e_port_v=int(e_port.get())
            _thread.start_new_thread(my_server,(show_1,e_host_v,e_port_v))
            #start_new_thread(my_server,(show_1,e_host_v,e_port_v))
            global secs
            secs = 0
            #runner()  # start repeated checking

root.mainloop()