_author_ = "Mizgin Yıldırım"

#saniyeyi dk,sa,gun vs çeviren
#1 yıl 365 gün olarak alındı
#1 ay 30 gün olarak alındı

zaman = float(input("Saniye cinsinden zamanı gir: "))
yıl = zaman // (8760 * 3600)
zaman = zaman % (8760 * 3600)

ay = zaman // (720 * 3600)
zaman = zaman % (720 * 3600)

hafta = zaman // (168 * 3600)
zaman = zaman % (168 * 3600)

gun = zaman // (24 * 3600)
zaman = zaman % (24 * 3600)

saat = zaman // 3600
zaman %= 3600

dakika = zaman // 60
zaman %= 60

saniye = zaman
print("%d yıl, %d ay, %d hafta, %d gun, %d saat, %d dakika, %d saniye. " % (yıl, ay, hafta, gun, saat, dakika, saniye))