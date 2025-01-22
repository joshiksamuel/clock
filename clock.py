#mylist=["car","bike"]
#mylist.len()
#print(mylist)


from tkinter import *
from tkinter.ttk import *

from time import strftime


root=Tk()
root.title("clock")
def time():
    string = strftime('%H,%M,%S %p')
    label.config(text=string)
    label.after(1000,time)

label=Label(root, font=("ds-digital",90),background = "#ffcccc",foreground="blue")
label.pack(anchor='center')

time()
mainloop()
