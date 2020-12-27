# Öğrenci Yönetim Sistemi

isim = "Kadriye"
soyIsim = "YAŞAR"

sayac = 3
while True:
    if sayac > 0 :
        ad = input("Lütfen isminizi giriniz: ")
        soyad = input("Lütfen soyisminizi giriniz: ")

        if ad == isim and soyad == soyIsim:
            print("Hoşgeldiniz!")
            break

        elif ad == isim and soyad != soyIsim:
            print("Soyisim yanlış girildi.\n")

        elif ad != isim and soyad == soyIsim:
            print("İsim yanlış girildi.\n")

        elif ad != isim and soyad != soyIsim:
            print("İsim ve soyisim yanlış girildi.\n")

        sayac -= 1

    else :
        print("Lütfen daha sonra tekrar deneyin!\n")
        exit()

dersler = []

ders1 = input("1.dersinizi giriniz: ")
ders2 = input("2.dersinizi giriniz: ")
ders3 = input("3.dersinizi giriniz: ")
ders4 = input("4.dersinizi giriniz: ")
ders5 = input("5.dersinizi giriniz: ")
dersler.append([ders1, ders2, ders3, ders4, ders5])
print("{:13} {:13} {:13} {:13} {:16}".format("Ders-1:", "Ders-2:", "Ders-3:", "Ders-4:", "Ders-5:"))
print("{:13} {:13} {:13} {:13} {:16}".format(ders1, ders2, ders3, ders4, ders5[0:-1]))

sayac = 5
basarisizDers = 4
basarisizDersler = []
while True:
    if sayac>0:
        dersSecimi = input("Bir ders seçiniz: ")

        vize = int(input("Dersinizin vize notunu giriniz: "))
        final = int(input("Dersinizin final notunu giriniz: "))
        proje = int(input("Dersinizin proje notunu giriniz: "))

        notlar = dict()
        notlar["Vize"] = vize
        notlar["Final"] = final
        notlar["Proje"] = proje
        print(notlar)

        ortalama = notlar["Vize"]*0.30 + notlar["Final"]*0.50 + notlar["Proje"]*0.20
        print("Ortalama: " + str(ortalama))

        if ortalama>90 :
            print("AA İLE BU DERSİ GEÇTİNİZ.\n")
        elif ortalama>70 and ortalama<90 :
            print("BB İLE BU DERSİ GEÇTİNİZ.\n")
        elif ortalama>50 and ortalama<70 :
            print("CC İLE BU DERSİ GEÇTİNİZ.\n")
        elif ortalama>30 and ortalama<50:
            print("DD İLE GEÇTİNİZ.\n")
        elif ortalama<30:
            basarisizDersler.append([ortalama])
            print("FF İLE BU DERSTEN KALDINIZ.\n")
        sayac -= 1
    if len(basarisizDersler)>3:
        print("3'ten fazla başarısız dersiniz olduğu için sınıfta kaldınız..") 
        
        basarisizDers -= 1
           
                    
        


        