__author__ = "Mizgin Yıldırım"
#Türkçe-İngilizce renkler ve anlamlarını gösteren sözlük

renkler= ["Mavi", "Mor", "Yeşil", "Siyah"]

print(renkler)

renkler_dict  = {"Mavi" : "Blue", "Mor" : "Purple", "Yeşil" : "Green", "Siyah" : "Black"}

print(renkler_dict)

print("Kırmızı" in renkler_dict)

print(renkler_dict.values())

print(renkler_dict[input("Türkçe renk yazınız(ilk harf büyük):")])
