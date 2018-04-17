__author__ = "Mizgin Yıldırım"

import random
from tkinter import Tk, Label, Button

class StefanZweigınYazdıgıKitaplar:
    def __init__(self, master):
        self.master = master
        master.title("Stefan Zweig'ın Yazdığı Kİtaplar")
        master.configure(background="yellow")

        self.label = Label(master, text="Stefan Zweig'ın Yazdığı Kİtaplar", font=("Arial", 14), bg="Blue")
        self.label.pack()

        self.kitaplar = Button(master, text="Kitap isimlerini göster", font=("arial", 11), command=self.kitaplar, bg="pink")
        self.kitaplar.pack()

        self.cıkıs=Button(master, text="Kapat",font=("Arial",11),command= master.quit,bg="grey")
        self.cıkıs.pack()

    def kitaplar(self):
        kitapİsimleri=("Satranç", "Dünün Dünyası", "Bilinmeyen Bir Kadının Mektubu", "Korku", "Olağanüstü Bir Gece", "Yakıcı Sır", "Ay Işığı Sokağı")
        kitapSec=random.choice(kitapİsimleri)

        self.kitaplar=Label(self.master, text=kitapSec)
        self.kitaplar.pack()

root = Tk()
kitaplar=StefanZweigınYazdıgıKitaplar(root)
root.mainloop()