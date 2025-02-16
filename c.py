from tkinter import *

window= Tk()
window.title("codingal")
window.geometry("300x300")

g = Label(text="Hello User",fg="black",bg="orange")
g.pack()

b = Button(text="Click Me",bg="black",fg="white")
b.pack()

e = Entry(width=50)
e.pack()

f = Frame(master=window,borderwidth=5)
f.pack()

window.mainloop()