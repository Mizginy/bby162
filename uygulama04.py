__author__ = "Mizgin Yıldırım"
#Şarkı sözü yazdırma

kadinismi = input("Bir kadın adı giriniz :")
print(kadinismi)
erkekismi = input("Bir erkek adı giriniz :")
print(erkekismi)
mısra= int(input("Mısra sayısı giriniz :"))


sarki = [erkekismi + "Ben ask nedir bilmem "+ kadinismi +" eski kafalıyım ", "bir seni bilirim, bir de adın geçince sıkışan kalbimi" + kadinismi ,"Ben seni bir okyanusun derinliğinde buldum da sevdim ","Parlak bir inciydin benim için.", erkekismi + "paha biçilmez bir inci" + kadinismi + " ben seni soğuk ve yağmurlu bir günde", "Seni düşünürken gülüşündeki sıcaklığın içinde dolup ta" +kadinismi + ",Beni sardığı bir anda sevdim","Seni sadece selvi boyun, siyah saçların ya da kara gözlerin", "Güzel bir yüzün var diye değil" + kadinismi + "Fikirlerinle, konuşmandaki güzelliğin ve benim o kor halde yanan",erkekismi + "yüreğimle sevdim" + kadinismi + "Ben seni derinden" + kadinismi + "hissederek sevdim.."]

for olusturulacak_sarki in sarki[:mısra]:
    print(olusturulacak_sarki)

    if mısra > 10:
        print("geçerli bir mısra sayısı giriniz:")

