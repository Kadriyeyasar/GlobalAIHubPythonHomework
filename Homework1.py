#Kullanıcıdan 5 değer alınıp, alınan değerler ekrana yazdırılacak.
#Değerlerin türü ekrana yazdırılacak.
#f-string ve format kullanılacak.

isim = input("Adınız: ")
soyIsim = input("Soyadınız: ")
yas = int(input("Yaşınız: "))
kilo = float(input("Kilonuz: "))
boy = float(input("Boyunuz: "))

liste = [isim,soyIsim,yas,kilo,boy]
print(liste)

print(f"Adınız: {isim}" + " ",type(isim))
print(f"Soyadınız: {soyIsim}" + " ",type(soyIsim))
print(f"Yaşınız: {str(yas)}" + " ",type(yas))
print(f"Kilonuz: {str(kilo)}" + "kg" + " ",type(kilo))
print(f"Boyunuz: {str(boy)}" + "m" + " ",type(boy))