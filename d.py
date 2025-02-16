from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("500x500")
root.title("picture")

upload = Image.open("img.jpg")
image = ImageTk.PhotoImage(upload)

l1 = Label(root, image=image, height=350, width=300)
l1.place(x=50, y=0)


root.mainloop()
