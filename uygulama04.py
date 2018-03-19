__author__ = "Mizgin Yıldırım"

kadinismi = input("Bir kadın adı giriniz...:")
erkekismi = input("Bir erkek adı giriniz...:")
mısra    = int(input("Mısra sayısı giriniz...Maksimum 10 mısra yazdırılabilir.."))


import random

sarki = [erkekismi + "Ben ask nedir bilmem "+ kadinismi +" eski kafalıyım ", "bir seni bilirim, bir de adın geçince sıkışan kalbimi" + kadinismi ,"Ben seni bir okyanusun derinliğinde buldum da sevdim ","Parlak bir inciydin benim için.", erkekismi + "paha biçilmez bir inci" + kadinismi + " ben seni soğuk ve yağmurlu bir günde", "Seni düşünürken gülüşündeki sıcaklığın içinde dolup ta" +kadinismi + ",Beni sardığı bir anda sevdim","Seni sadece selvi boyun, siyah saçların ya da kara gözlerin", "Güzel bir yüzün var diye değil" + kadinismi + "Fikirlerinle, konuşmandaki güzelliğin ve benim o kor halde yanan",erkekismi + "yüreğimle sevdim" + kadinismi + "Ben seni derinden" + kadinismi + "hissederek sevdim.."]

for olusturulacak_sarki in sarki[:mısra]:
    print(random.choice(sarki))


if mısra > 10:
    print("Geçerli bir mısra sayısı girmediniz..")
    print("Yazdırılan mısra sayısı: 10")

else:
    print("Yazdırılan mısra sayısı:", mısra)