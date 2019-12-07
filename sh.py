from tkinter import *
import pyperclip

window = Tk()
window.title("Schowek")
window.resizable(width=False, height=False)
top = 0

def all_children (window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list

def clear():
    widget_list = all_children(window)
    for item in widget_list:
        item.pack_forget()
    run()

def clicked(text):
    pyperclip.copy(text)
    pyperclip.paste()

frame = Frame(window)
def add():
    for i in range(1):
        btn = Button(window, text=txt.get(), wraplength=150, justify=LEFT , command=lambda j=i+1: clicked(btn.cget("text")))
        btn.pack(side=BOTTOM, expand=True)
    txt.delete(0,END)

def top():
    global top
    if top == 0:
        window.call('wm', 'attributes', '.', '-topmost', '0')
        top = 1
    else:
        window.call('wm', 'attributes', '.', '-topmost', '1')
        top = 0
        
def run():
    btntop = Button(window, text="Top", command=top)
    btntop.pack(side=RIGHT)

    lbl = Label(window, text="Witaj w schowku!")
    lbl.pack()

    txt = Entry(window, width=50)
    txt.pack()

    btn = Button(window, text="Dodaj", command=add)
    btn.pack()

    btn2 = Button(window, text="Wyczyść", command=clear)
    btn2.pack()
    
    lbl2 = Label(window, text=" ")
    lbl2.pack()
    


btntop = Button(window, text="Top", command=top)
btntop.pack(side=RIGHT)

lbl = Label(window, text="Witaj w schowku!")
lbl.pack()

txt = Entry(window, width=50)
txt.pack()

btn = Button(window, text="Dodaj", command=add)
btn.pack()

btn2 = Button(window, text="Wyczyść", command=clear)
btn2.pack()

lbl2 = Label(window, text=" ")
lbl2.pack()

window.mainloop()
