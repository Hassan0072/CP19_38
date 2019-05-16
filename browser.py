import tkinter  
import tkinter.filedialog

root = tkinter.Tk()


def print_path():  
    f = tkinter.filedialog.askopenfilename(
        parent=root, initialdir='C:/Tutorial',
        title='Choose file',
        filetypes=[('png images', '.png'),
                   ('gif images', '.gif')]
        )
 
    print(f)
 
b1 = tkinter.Button(root, text='Print path', command=print_path)  
b1.pack(fill='x')
 
root.mainloop()