from tkinter import *
from PIL import ImageTk,Image
class Kutuphane:
    def __init__(self,anaSayfa):
        global kitapIsbn, ısbnAlanı
        global  kitapadıAlanı, kadıAlanı
        global yadıAlanı, yazaradıAlanı
        global yadı_Alanı, yadı__Alanı
        self.anasayfa = anaSayfa
        anaSayfa.title("Kütüphane Otomasyonu")

        anaSayfa.configure(background="lightblue")
        anaSayfa.geometry("800x650")
        kitapIsbn = [ "123", "321", "432"]
        kitapadıAlanı = ["yüreğim seni çok sevdi","açlık oyunları","olasılıksız"]
        yazaradıAlanı = ["canan tan", "suzanne collins","adam fawer"]
        yadı__Alanı = ["1","2","3"]

        hosGel = Label(anaSayfa, text="Katalog Tarama Arayüzüne Hoşgeldiniz..\n Lütfen bir kategori seçin ve tarama yapın..", bg="lightblue", fg="black",font=("calibri", 12)).grid(columnspan=1,  sticky=E)


        istek = Label(anaSayfa, text="Lütfen ISBN Giriniz:", bg="lightblue", fg="red", font=("calibri italic", 12)).grid(row=1, sticky=W)
        ısbnAlanı = Entry()
        ısbnAlanı.grid(row=2, sticky=W)
        taraBut = Button(anaSayfa,text="TARA", bg="white", fg="black", font=("calibri", 12), command=self.gir).grid(row=3, sticky=W)


        istek = Label(anaSayfa, text="Lütfen Kitap Adı Giriniz:", bg="lightblue", fg="red",
                      font=("calibri italic", 12)).grid(row=1, column=5, sticky=E)
        kadıAlanı = Entry()
        kadıAlanı.grid(row=2, column=5, sticky=E)
        taraBut = Button(anaSayfa, text="TARA", bg="white", fg="black", font=("calibri", 12), command=self.gir1).grid(
            row=3, column=5, sticky=E)


        istek = Label(anaSayfa, text="Lütfen Yazar Adı Giriniz:", bg="lightblue", fg="red",
                      font=("calibri italic", 12)).grid(row=4, column=0, sticky=W)
        yadıAlanı = Entry()
        yadıAlanı.grid(row=5, column=0, sticky=W)
        taraBut = Button(anaSayfa, text="TARA", bg="white", fg="black", font=("calibri", 12), command=self.gir2).grid(
            row=6, column=0, sticky=W)



        istek = Label(anaSayfa, text="Lütfen İkinci Yazar Adı Giriniz:", bg="lightblue", fg="red",
                      font=("calibri italic", 12)).grid(row=4, column=5, sticky=E)
        yadı_Alanı = Entry()
        yadı_Alanı.grid(row=5, column=5, sticky=E)
        taraBut = Button(anaSayfa, text="TARA", bg="white", fg="black", font=("calibri", 12), command=self.gir3).grid(
            row=6, column=5, sticky=E)



    def gir3(self):
        ayad= yadı_Alanı.get()
        if ayad==yadı__Alanı[0]:

            ab=Label(root,text="KİTAP ADI: YÜREĞİM SENİ ÇOK SEVDİ \n YAZAR ADI:CANAN TAN \n TÜR:ROMAN \n RAF NUMARASI:A56", bg="lightblue",fg="black" , font=("calibri",12)).grid()

            self.fotoGP = Image.open("foto1.png")
            self.tkGP = ImageTk.PhotoImage(self.fotoGP)
            self.resimGP = Label(root, image=self.tkGP)
            self.resimGP.grid()

        elif  ayad==yadı__Alanı[1]:
            bb = Label(root,text="KİTAP ADI: AÇLIK OYUNLARI \n YAZAR ADI:SUZANNE COLLİNS \n TÜR:ROMAN \n RAF NUMARASI:A55", bg="lightblue",fg="black", font=("calibri", 12)).grid()

            self.fotoGP = Image.open("foto2.png")
            self.tkGP = ImageTk.PhotoImage(self.fotoGP)
            self.resimGP = Label(root, image=self.tkGP)
            self.resimGP.grid()

        elif  ayad==yadı__Alanı[2]:
            cb = Label(root,text="KİTAP ADI: OLASILIKSIZ \n YAZAR ADI: ADAM FAWER \n TÜR:ROMAN \n RAF NUMARASI:A67",bg="lightblue", fg="black", font=("calibri", 12)).grid()

            self.fotoGP = Image.open("foto3.png")
            self.tkGP = ImageTk.PhotoImage(self.fotoGP)
            self.resimGP = Label(root, image=self.tkGP)
            self.resimGP.grid()

        else :
            db = Label(root,text="Maalesef aradığınız kitap koleksiyonumuzda yok..." , bg="lightblue",fg="black", font=("calibri", 12)).grid()


















    def gir2(self):
        yad= yadıAlanı.get()
        if yad==yazaradıAlanı[0]:

            ab=Label(root,text="KİTAP ADI: YÜREĞİM SENİ ÇOK SEVDİ \n YAZAR ADI:CANAN TAN \n TÜR:ROMAN \n RAF NUMARASI:A56", bg="lightblue",fg="black" , font=("calibri",12)).grid()

            self.fotoGP = Image.open("foto1.png")
            self.tkGP = ImageTk.PhotoImage(self.fotoGP)
            self.resimGP = Label(root, image=self.tkGP)
            self.resimGP.grid()

        elif yad==yazaradıAlanı[1]:
            bb = Label(root,text="KİTAP ADI: AÇLIK OYUNLARI \n YAZAR ADI:SUZANNE COLLİNS \n TÜR:ROMAN \n RAF NUMARASI:A55", bg="lightblue",fg="black", font=("calibri", 12)).grid()

            self.fotoGP = Image.open("foto2.png")
            self.tkGP = ImageTk.PhotoImage(self.fotoGP)
            self.resimGP = Label(root, image=self.tkGP)
            self.resimGP.grid()

        elif yad== yazaradıAlanı[2]:
            cb = Label(root,text="KİTAP ADI: OLASILIKSIZ \n YAZAR ADI: ADAM FAWER \n TÜR:ROMAN \n RAF NUMARASI:A67",bg="lightblue", fg="black", font=("calibri", 12)).grid()

            self.fotoGP = Image.open("foto3.png")
            self.tkGP = ImageTk.PhotoImage(self.fotoGP)
            self.resimGP = Label(root, image=self.tkGP)
            self.resimGP.grid()

        else :
            db = Label(root,text="Maalesef aradığınız kitap koleksiyonumuzda yok..." , bg="lightblue",fg="black", font=("calibri", 12)).grid()










    def gir1(self):
        ad= kadıAlanı.get()

        if ad==kitapadıAlanı[0]:

            ab=Label(root,text="KİTAP ADI: YÜREĞİM SENİ ÇOK SEVDİ \n YAZAR ADI:CANAN TAN \n TÜR:ROMAN \n RAF NUMARASI:A56", bg="lightblue",fg="black" , font=("calibri",12)).grid()

            self.fotoGP = Image.open("foto1.png")
            self.tkGP = ImageTk.PhotoImage(self.fotoGP)
            self.resimGP = Label(root, image=self.tkGP)
            self.resimGP.grid()

        elif ad==kitapadıAlanı[1]:
            bb = Label(root,text="KİTAP ADI: AÇLIK OYUNLARI \n YAZAR ADI:SUZANNE COLLİNS \n TÜR:ROMAN \n RAF NUMARASI:A55", bg="lightblue",fg="black", font=("calibri", 12)).grid()

            self.fotoGP = Image.open("foto2.png")
            self.tkGP = ImageTk.PhotoImage(self.fotoGP)
            self.resimGP = Label(root, image=self.tkGP)
            self.resimGP.grid()

        elif ad == kitapadıAlanı[2]:
            cb = Label(root,text="KİTAP ADI: OLASILIKSIZ \n YAZAR ADI: ADAM FAWER \n TÜR:ROMAN \n RAF NUMARASI:A67",bg="lightblue", fg="black", font=("calibri", 12)).grid()

            self.fotoGP = Image.open("foto3.png")
            self.tkGP = ImageTk.PhotoImage(self.fotoGP)
            self.resimGP = Label(root, image=self.tkGP)
            self.resimGP.grid()

        else :
            db = Label(root,text="Maalesef aradığınız kitap koleksiyonumuzda yok..." , bg="lightblue",fg="black", font=("calibri", 12)).grid()






    def gir(self):
        ısbn= ısbnAlanı.get()

        if (ısbn==kitapIsbn[0]):

            a=Label(root,text="KİTAP ADI: YÜREĞİM SENİ ÇOK SEVDİ \n YAZAR ADI:CANAN TAN \n TÜR:ROMAN \n RAF NUMARASI:A56", bg="lightblue",fg="black" , font=("calibri",12)).grid()

            self.fotoGP = Image.open("foto1.png")
            self.tkGP = ImageTk.PhotoImage(self.fotoGP)
            self.resimGP = Label(root, image=self.tkGP)
            self.resimGP.grid()

        elif ısbn==kitapIsbn[1]:
            b = Label(root,text="KİTAP ADI: AÇLIK OYUNLARI \n YAZAR ADI:SUZANNE COLLİNS \n TÜR:ROMAN \n RAF NUMARASI:A55", bg="lightblue",fg="black", font=("calibri", 12)).grid()

            self.fotoGP = Image.open("foto2.png")
            self.tkGP = ImageTk.PhotoImage(self.fotoGP)
            self.resimGP = Label(root, image=self.tkGP)
            self.resimGP.grid()

        elif ısbn == kitapIsbn[2]:
            c = Label(root,text="KİTAP ADI: OLASILIKSIZ \n YAZAR ADI: ADAM FAWER \n TÜR:ROMAN \n RAF NUMARASI:A67",bg="lightblue", fg="black", font=("calibri", 12)).grid()

            self.fotoGP = Image.open("foto3.png")
            self.tkGP = ImageTk.PhotoImage(self.fotoGP)
            self.resimGP = Label(root, image=self.tkGP)
            self.resimGP.grid()

        else :
            e = Label(root,text="Maalesef aradığınız kitap koleksiyonumuzda yok.." , bg="lightblue",fg="black", font=("calibri", 12)).grid()




root = Tk()
yeniPencere = Kutuphane(root)
root.mainloop()