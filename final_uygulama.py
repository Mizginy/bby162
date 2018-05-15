import tkinter
from random import choice


class Simon() :
    def __init__(self, master):

        self.master = master
        self.master.minsize(450, 550)
        self.master.title("Simon & Simon")
        self.master.update()


        self.simon_canvas = tkinter.Canvas(self.master, width=self.master.winfo_width(), height=self.master.winfo_height(), highlightthickness=6)
        self.simon_canvas.pack()


        self.ana_renkler = ("red", "blue", "green", "yellow")
        self.yanan_renkler = ("white", "white", "white", "white")
        self.renkler = [color for color in self.ana_renkler]
        self.dikdortgenler = []


        self.sira = [choice(self.ana_renkler)]
        self.sira_yeri = 0
        self.canvas_ciz()
        self.sirayi_goster()
        self.master.mainloop()


    def sirayi_goster(self):

        self.doldur(self.sira[self.sira_yeri])
        if(self.sira_yeri < len(self.sira) - 1):
            self.sira_yeri += 1
            self.master.after(1500, self.sirayi_goster)
        else :
            self.sira_yeri = 0

    def doldur(self, color):
        index = self.ana_renkler.index(color)
        if self.renkler[index] == self.ana_renkler[index] :
            self.renkler[index] = self.yanan_renkler[index]
            self.master.after(1250, self.doldur, color)
        else :
            self.renkler[index] = self.ana_renkler[index]
        self.canvas_ciz()


    def kontrol_choice(self):
        dikdortgen_kimligi = self.simon_canvas.find_withtag("current")[0]
        dikdortgen_index = self.dikdortgenler.index(dikdortgen_kimligi)
        color = self.ana_renkler[dikdortgen_index]
        if color == self.sira[self.sira_yeri]:
            if self.sira_yeri < len(self.sira) - 1:
                self.sira_yeri += 1
            else :
                self.master.title("Simon Oyunu - Skor: {}".format(len(self.sira)))
                self.sira.append(choice(self.ana_renkler))
                self.sira_yeri = 0
                self.sirayi_goster()
        else :
            self.master.title("Simon Oyunu - Oyun Bitti! | Skorun: {}".format(len(self.sira)))
            self.sira[:] = []
            self.sira.append(choice(self.ana_renkler))
            self.sira_yeri = 0
            self.sirayi_goster()

    def canvas_ciz(self):
        self.dikdortgenler[:] = []
        self.simon_canvas.delete("all")
        for index, color in enumerate(self.renkler):
            if index <= 1:
                rectangle = self.simon_canvas.create_rectangle(
                                          index * self.master.winfo_width(),
                                          0, self.master.winfo_width() / 2,
                                          self.master.winfo_height() / 2,
                                          fill = color, outline = color)
            else:
                rectangle = self.simon_canvas.create_rectangle(
                                        (index - 2) * self.master.winfo_width(),
                                        self.master.winfo_height(),
                                        self.master.winfo_width() / 2,
                                        self.master.winfo_height() / 2,
                                        fill = color, outline = color)
            self.dikdortgenler.append(rectangle)
        for id in self.dikdortgenler:
            self.simon_canvas.tag_bind(id, '<ButtonPress-1>', lambda e : self.kontrol_choice())

def main():
    root = tkinter.Tk()
    gui = Simon(root)

if __name__ == "__main__" : main()