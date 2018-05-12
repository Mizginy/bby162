from tkinter import *
from PIL import Image, ImageTk
album = Tk()
album.title("Danimarka'nın Turistik Yerleri Fotoğraf Albümü")


foto1 = ImageTk.PhotoImage(Image.open("foto1.jpg"))
foto2 = ImageTk.PhotoImage(Image.open("foto2.jpg"))


etiket = Label(album, text="Danimarka'nın Turistik Yerleri Fotoğraf Albümü")
etiket.pack()

def ileri():
    if display == foto1:
        panel1.configure(image=foto2)
    else:
        panel1.configure(image= foto1)

ileributon = Button(album, text="İleri", font = ("Arial Black", 22), command=ileri)
ileributon.pack(side="right")

def geri():
    if display2 == foto2:
        panel1.configure(image = foto1)
    else:
        panel1.configure(image = foto2)

geributon = Button(album, text="Geri", font = ("Arial Black", 22), command=geri)
geributon.pack(side="left")

panel1 = Label(album, image=foto1)
display = foto1
panel1.pack(side="top")

panel2 = Label(album, image=foto2)
display2 = foto2


album.mainloop()