
isim = input("Adınız: ")
soyIsim = input("Soyadınız: ")
yas = int(input("Yaşınız: "))
dogumYılı = int(input("Doğum Yılınız: "))

liste = [isim,soyIsim,yas,dogumYılı]


for i in liste:
    print(i)

if yas < 18:
    print("Yaşınız 18'den küçük olduğu için dışarı çıkmanız tehlikelidir!")
else:
    print("Dışarı çıkabilirsiniz.")






