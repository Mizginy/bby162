__author__ = "Mizgin Yıldırım"
import random

kalanHak = 6
i = 0

kelimeler = random.choice(['elma', 'armut', 'ayna', 'silgi', 'elbise', 'dolap', 'araba', 'helikopter', 'karpuz'])
harfHavuzu = []
print("Adam Asmaca Oyununa hoşgeldiniz!")
for islem in kelimeler:
    harfHavuzu.append("_")
print(harfHavuzu)

while kalanHak > 0:
    girilenHarf = input("Lütfen bir harf giriniz: ").lower()
    if girilenHarf in kelimeler:
        for kontrol in kelimeler:
            if kelimeler[i] == girilenHarf:
                harfHavuzu[i] = girilenHarf
            i += 1
        print(harfHavuzu)
        print("Tebrikler, doğru harf!")
        i = 0
    else:
        i = 0
        kalanHak -= 1
        print("Kalan can " + str(kalanHak) )

if kalanHak == 0:
    print('Oyunu kaybettiniz. Doğru kelime "{}".\n'.format(kelimeler))
