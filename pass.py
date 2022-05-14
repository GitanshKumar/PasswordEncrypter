import tkinter as tk
from tkinter.font import Font
from tkinter.constants import END
from tkinter import DISABLED, NORMAL
import pyperclip as pc
from os import getcwd

def menu():
    win = tk.Tk()
    win.geometry("450x150+500+300")
    win.iconphoto(False, tk.PhotoImage(file= (getcwd() + "/icon.png")))
    win.resizable(False, False)
    win.title("Password Encypter")

    def Show():
        if(v1.get()==1):
            e1.config(show='')
        else:
            e1.config(show='*')

    font = Font(win, family= "Arial", size= 10)
    font2 = Font(win, family= "Arial", size= 8)

    text0 = tk.StringVar()
    text1 = tk.StringVar()
    v1 = tk.IntVar(value= 0)

    tk.Label(win, text= 'Enter Password', font= font, pady= 5).place(x = 35, y = 20)
    e1 = tk.Entry(win, textvariable= text0, show= "*", width= 30, font= ("bold", 10))
    e1.place(x= 180, y= 25)

    c1 = tk.Checkbutton(win, text='Show Password', borderwidth= 1, variable= v1, onvalue=1, offvalue=0, font= font2, command= Show)
    c1.place(x= 250, y= 48)

    tk.Label(win, text= 'Enrypted Password', font= font, pady= 5).place(x = 35, y = 70)
    e2 = tk.Entry(win, textvariable= text1, state= DISABLED, width= 30, font= ("bold", 10))
    e2.place(x= 180, y= 75)

    copy = tk.Button(win, text='Copy', borderwidth= 1, state= DISABLED, font= font2, command= lambda: pc.copy(text1.get()))
    copy.place(x= 400, y= 73)

    SUB = tk.Button(win, text='Confirm', borderwidth= 1, font= font, command= lambda: encrypt(text0.get(), 2, e2, copy))
    SUB.place(x= 200, y= 120)

    win.update()
    win.mainloop()

def encrypt(pas:str, passes:int, entry:tk.Entry, copy_button:tk.Button):
    final = ""
    code = {"a":"@", "b":"|}", "c":"{", "d":"c", "e":"@5", "f":":", "g":"|0", "h":"|-|", "i":"!",
            "j":">", "k":"|<", "l":"7", "m":"|*|", "n":"@14", "o":"oh", "p":"|o", "q":"(|", "r":"re",
            "s":"3|", "t":"|7", "u":"_", "v":"e", "w":"uu", "x":"?", "y":"|??", "z":"et"}
    
    for _ in range(passes):
        temp = ""
        for i in pas:
            if not i.isalpha():
                temp += i
                continue
            if i.isupper():
                temp += "^" + code[i.lower()]
            else:
                temp += code[i]
        final += temp
        pas = temp
    
    entry["state"] = NORMAL
    entry.delete(0, END)
    entry.insert(0, final)
    entry["state"] = DISABLED
    copy_button["state"] = NORMAL

menu()