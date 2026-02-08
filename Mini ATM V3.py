from datetime import datetime

import sys

#selamlama
print("//Mini ATM V3'e hoşgeldiniz!//")

sifre = "TTYY9112211++"

hak = 3

islem_gecmisi = []

try:
    with open("islem_gecmisiV3.txt", "r") as f:
        for x in f:
            temizle = x.strip()
            if temizle:
                islem_gecmisi.append(temizle)

except FileNotFoundError:
    with open("islem_gecmisiV3.txt", "w") as f:
        f.write(str(islem_gecmisi))

mevcut_bakiye = 19000

try:
    with open("bakiye.txt", "r") as f:
        mevcut_bakiye = int(f.read())

except ValueError:
    mevcut_bakiye = 19000

#Para yatırma fonksiyonu
def para_yatir(mevcut_bakiye):
    try:
        yatirilan_para = int(input("Lütfen yatırmak istediğiniz miktarı yazınız: "))

        yeni_bakiye = int(mevcut_bakiye + yatirilan_para)
        simdiki = datetime.now()
        simdi = simdiki.strftime("%d.%m.%Y - %H:%M:%S")

        print(f" {simdi} tarihinde Miktar yatırıldı: +{yatirilan_para}, yeni bakiyeniz: +{yeni_bakiye}")
        islem_gecmisi.append(f" {simdi} tarihinde Miktar yatırıldı: +{yatirilan_para}, Yeni bakiye: +{yeni_bakiye}")

        return yeni_bakiye

    except ValueError:
        print("Sadece sayı girmelisiniz...")

        return mevcut_bakiye

#Para çekme fonksiyonu
def para_cek(mevcut_bakiye):
    try:
        cekilen_para = int(input("Lütfen çekmek istediğiniz miktarı yazınız: "))

        if cekilen_para > mevcut_bakiye:
            print("Bakiye yetersiz!")

            return mevcut_bakiye

        else:
            yeni_bakiye = mevcut_bakiye - cekilen_para
            simdiki = datetime.now()
            simdi = simdiki.strftime("%d.%m.%Y - %H:%M:%S")

            print(f"{simdi} tarihinde Miktar çekildi: -{cekilen_para}, Yeni bakiyeniz: +{yeni_bakiye}")
            islem_gecmisi.append(f"{simdi} tarihinde Miktar çekildi: -{cekilen_para}, Yeni bakiye: +{yeni_bakiye}")

            return yeni_bakiye

    except ValueError:
        print("Sadece sayı girmelisiniz...")

        return mevcut_bakiye

#Bakiye görüntüleme fonksiyonu
def bakiye_goruntule(mevcut_bakiye):
    simdiki = datetime.now()
    simdi = simdiki.strftime("%d.%m.%Y - %H:%M:%S")

    print(f"{simdi} tarihinde Bakiyeniz: {mevcut_bakiye}")

    islem_gecmisi.append(f" {simdi} tarihinde Bakiyeniz görüntülendi: {mevcut_bakiye}")

    return mevcut_bakiye

def islem_gecmis():

    if not islem_gecmisi:
        print("Daha işlem yapmadınız...")

    else:
        print("\n------İşlem geçmişi-----")
        for x in islem_gecmisi:
            print(f"{x}")
        print("------------------------\n")

#Çıkış fonksiyonu
def cikis():
    print("Bay bay!")
    simdiki = datetime.now()
    simdi = simdiki.strftime("%d.%m.%Y - %H:%M:%S")

    islem_gecmisi.append(f" {simdi} tarihinde çıkış yapıldı")

#Dosyaya aktarma fonksiyonu
def dosya_aktar():

    with open("islem_gecmisiV3.txt", "w") as f:
        for x in islem_gecmisi:
            f.write(x + "\n")

def bakiye_kaydet(mevcut_bakiye):

    with open("bakiye.txt", "w") as f:
        f.write(str(mevcut_bakiye))

    return mevcut_bakiye

while True:
    sifre_giris = input("Lütfen şifreyi giriniz (3 Hakkınız vardır): ")

    if sifre_giris == sifre:
        print("Şifre doğru!")
        break
    else:
        hak -= 1
        if hak == 0:
            print("Hakkınız bitmiştir! Çıkış yapılıyor...")
            sys.exit()

        else:
            print(f"Şifre yanlış! {hak} hakkınız kaldı")
            continue

while True:
    secim = input("Ana menüye geçmek ister misiniz? (Evet için 1, hayır için 2): ")

    if secim == "1":
        while True:
            ana_menu = input("""//Ana menüye hoşgeldiniz!//
1. Para yatırma
2. Para çekme
3. Bakiyeyi görüntüle
4. İşlem geçmişini görüntüle
5. Çıkış
Lütfen bir seçim yapınız: """)

            if ana_menu == "1":
                mevcut_bakiye = para_yatir(mevcut_bakiye)
                dosya_aktar()
                bakiye_kaydet(mevcut_bakiye)

            elif ana_menu == "2":
                mevcut_bakiye = para_cek(mevcut_bakiye)
                dosya_aktar()
                bakiye_kaydet(mevcut_bakiye)

            elif ana_menu == "3":
                bakiye_goruntule(mevcut_bakiye)
                dosya_aktar()

            elif ana_menu == "4":
                islem_gecmis()

            elif ana_menu == "5":
                cikis()
                dosya_aktar()
                sys.exit(0)

            else:
                print("1, 2, 3, 4 veya 5 yazmalısınız...")
                continue

    elif secim == "2":
        print("Bay bay!")
        sys.exit()

    else:
        print("1 veya 2 seçmelisiniz...")

        continue
