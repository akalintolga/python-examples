# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Welcome to GeekForGeeks")
# Set geometry (widthxheight)
root.geometry('500x500')
lbl = Label(root, text = "Butona Tıklayın")
lbl.grid()

def clicked():
    lbl.configure(text="birinci buton tıklandı")

btn = Button(root, text= "birinci buton" , fg = "red", command=clicked)
btn.grid(column=1, row=0)

def clicked2():
    lbl.configure(text="ikinci buton tıklandı")

btn2 = Button(root, text="ikinci buton", fg ="green", command=clicked2)
btn2.grid(column=3, row=0)

txt = Entry(root, width=5)
txt.grid(column=10, row=1)




# all widgets will be here
# Execute Tkinter
root.mainloop()
