from tkinter import *
from tkinter import messagebox
from socket import *
import _thread

root = Tk()
root.title("Remote File Sharing System")
root.geometry("1030x600")
root.minsize(width=500 , height=500)
topFrame = Frame(root)
bottomFrame = Frame(root)
theLabel = Label(root, text="Remote File Sharing System (User Interface)",bg="black",fg="white",font="Times 22",width=60)
theLabel.grid(row=0, column=0, padx=8, pady=8, sticky="NSNESWSE")
topFrame.grid(row=50,column=50)
bottomFrame.grid(row=10,column=10)
root.configure(width=600,height=800)
import socket
s= socket.socket()
host = socket.gethostname()
port= 8080
s.bind((host,port))
s.listen(1)

label = Label(root, text="Server Software ", font=",16",bg="blue",fg="White",width=10)
label.grid(row=1, column=0, padx=8, pady=8, sticky="NSNESWSE")
l_host=Label(root,text="Enter Host NAME")
l_host.grid(row=2, column=0, padx=3, pady=2, sticky="NSNESWSE")

e_host=Entry(root)
e_host.place(x=550,y=100)
e_host.insert(END,'127.0.0.1')


l_port=Label(root,text="Enter Port")
l_port.grid(row=3, column=0, padx=8, pady=8, sticky="NSNESWSE")

e_port=Entry(root)
e_port.place(x=550,y=125)
e_port.insert(END,12121)

message_label=Label(root,text="Client Message",font="Arial,12",width=100)
message_label.grid(row=4 , column=0, padx=8, pady=8,sticky="NSEW")


scrollbar_y = Scrollbar(root)
scrollbar_y.grid(row=5, column=3,rowspan=6)
show_1=Text(root,height=8, width=100, yscrollcommand=scrollbar_y.set,
                       bg="Grey",fg="White")
show_1.grid(row=5, column=0,rowspan=3,columnspan=2,sticky="NSEW")

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