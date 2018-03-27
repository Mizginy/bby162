__author__ = "Mizgin Yıldırım"
import random

kelimeler = random.choice(['elma', 'armut', 'ayna', 'silgi', 'elbise', 'dolap', 'araba', 'helikopter', 'karpuz'])
harfhavuzu = []
kalanhak = 6
harfsayısınıgosterencizgi = '_'

gosterimyazisi = list(harfsayısınıgosterencizgi * len(kelimeler))

dongu = 1


while dongu:
    print(' '.join(gosterimyazisi), end='\n\n')

    girilenharf = input('Bir harf giriniz: ').lower()

    try:
        int(girilenharf)
        print('Doğru bir şeyler girdiğinden emin ol.\n')
    except:
        if len(girilenharf) > 1:
            print('Harf giriniz!\n')
        else:
            if girilenharf in harfhavuzu:
                print('Bu harfi zaten girdiniz.\n')
            else:
                bulduk = None
                for i in range(len(kelimeler)):
                    if girilenharf == kelimeler[i]:
                        bulduk = True
                        gosterimyazisi[i] = girilenharf
                        harfhavuzu.append(girilenharf)

                        if harfsayısınıgosterencizgi not in gosterimyazisi:

                            print(' '.join(gosterimyazisi))
                            print('\nTebrikler kelimeyi buldunuz!')
                            dongu = 0

                else:

                    if bulduk != True:
                        kalanhak -= 1
                        print('Yanlış harf. Kalan hakkınız: {}\n'.format(kalanhak))
                        harfhavuzu.append(girilenharf)

                if kalanhak == 0:
                    print('Kaybettin. Doğru kelime "{}" idi.\n'.format(kelimeler))

                    break
