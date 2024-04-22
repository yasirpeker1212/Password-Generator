import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

sifre_uzunlugu = int(input("Şifre Uzunluğu: "))
if sifre_uzunlugu <= 4:
    print("Lütfen 4'den fazla karakter uzunluğu seçin")
    
else:
    sifre = ""

    for i in range(sifre_uzunlugu):
        sifre += random.choice(karakterler)

    print("Şifreniz: ",sifre)
