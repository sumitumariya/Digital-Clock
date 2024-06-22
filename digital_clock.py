import tkinter as tk
# tkinter is used to make graphical interface 
# as tk is used bcoz we can use tkinter with the name tk
from time import strftime

root=tk.Tk()
root.title("Digital Clock")

def time():
    string = strftime('%H : %M : %S %p \n%D')
    label.config(text=string)
    label.after(1000,time)

label = tk.Label(root, font=('calibri',50 ,'bold'),background='yellow', foreground ='black')
label .pack(anchor='center')

time()
root.mainloop()