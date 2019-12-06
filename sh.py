from tkinter import *
import pyperclip
rows = 1
column = 0
#Window
window = Tk()
window.title("Schowek")
window.geometry('700x200')

#Clicked function
def clicked(text):
    pyperclip.copy(text)
    pyperclip.paste()

#Add function
def add():
    global rows , column
    for i in range(rows):
        btn = Button(window, text=txt.get())
        btn.configure(command=lambda j=i+1: clicked(btn.cget("text")))
        btn.grid(column=column, row=rows)
    rows += 1
    if rows == 5:
        rows = 0
        column += 1

#Text
lbl = Label(window, text="Witaj w schowku!")
lbl.grid(column=0,row=0)

txt = Entry(window,width=50)
txt.grid(column=1, row=0)

btn = Button(window, text="Dodaj", command=add)
btn.grid(column=2, row=0)




window.mainloop()
