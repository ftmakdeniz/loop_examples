"""
WHİLE--FOR
 while (kosul):
kosul true oldugu surece bu kod blogu calısır.
break ile durdurulur.
contuinue ile de döngü basa sarar.
while True program kapatılana kadar calısır.
** dikkat edilmezse döngüyü sonsuz donguye sokabılır***
"""

"""
i = 1
while i< 11:
    print(i)
    if i == 5:
        break
    i += 1
"""

"""
while True:
    print("Fatma")
    break
"""

"""
# 80 ile 90 arasında ki sayilari ekrana yazdıralım.

sayi = 80
while sayi <= 90:
    print(sayi)
    sayi +=1


### 1 ile 100 arasında ki sayıları tek çift ayrı ayrı toplamlarını yazdıralım.
### Ayrı hesaplayan kod yazıp if else ve while kullanılsın.

tek_toplam = 0
cift_toplam = 0
sayi = 1

while sayi <= 100:

    if sayi % 2 == 0:
        tek_toplam += sayi
    else:
        cift_toplam += sayi
    sayi += 1
print(f"1-100 arasındaki tek sayilar toplamı {tek_toplam}")
print(f"1-100 arasındaki cift sayilar toplamı {cift_toplam}")

"""
"""
### 80 ile 50 arasındaki sayıların 3'e tam bölünenleri ekrana yazdıralım.

sayi =50
while sayi <= 80:
    if sayi %3 ==0:
        print(sayi)
    sayi += 1
"""

"""
## bu işlemi tersten yapalım bu defada.

sayi =80
while sayi >= 50:
    if sayi %3 ==0:
        print(sayi)
    sayi -= 1
###   bu işlemde " -" olduğunu unutmayalım. 

"""

"""
### 1' den kullanıcının girdiği sayıya kadar olan sayıların karesini ekrana yazdıralım.

baslangic = 1
bitis = int(input("Kaça kadar?"))

while baslangic <= bitis:
    print(baslangic **2)
    baslangic += 1
"""


"""
### 1'den kullanıcının girdiği sayıya kadar olan
### sayıların eger tek ise karesi, cift ise küplerini
### alip ayrı ayrı toplayalım.

baslangic = 1
bitis = int(input("Lütfen bir sayi giriniz"))
tek_toplam = 0
cift_toplam = 0

while baslangic <= bitis:
    if baslangic %2==0:
        cift_toplam += baslangic **3
    else:
        tek_toplam += baslangic **2
    baslangic += 1
print(tek_toplam)
print(cift_toplam)
"""
"""
### Klavyeden girilen deger "çık" ise döngüden cıkacak.
### Değil ise toplama işlemi gerceklestirecek.

toplam = 0
while True:
    cevap = input("Lütfen bir sayı girin veya çıkmak için çık yazın").upper()
    if cevap == "ÇIK":
        break
    else:
        toplam += int(cevap)
print(toplam)
"""


"""
### Klavyeden girilen sayının faktöriyerini hesaplayan program

sayi = int(input("Faktöryeli alınacak sayıyı girin:"))
sayac = 1
sonuc = 1
while sayac <= sayi:
    sonuc *= sayac
    sayac +=1
print(f"{sayi}! = {sonuc}")
"""

"""
### kullanıcıadı/Email ve şifre ile giris saglanacak. 3 defa giriş hakkı vardır.
### Giriş basarılı ise ekrana "Giriş Başarılı" yazssın. Değil ise;
### Kullanıcıya kayıt olmak ister misiniz?
### Hayır ise ;
### kullanıcıadı, ad, soyad, email, şifre ve şifre tekrarı
### Alarak kayıt yapalım.
### şifre ve şifre tekrarı aynı olması

kullanici_mail = "info@fatma.net"
kullaici_adi = "fatma"
sifre = "1234"
hak = 3
giris_basarili = False

while True:
    print("###KULLANICI GİRİŞİ###")

    while hak > 0:
        user_name = input("Kullanıcı adınızı veya email adresinizi:")
        password = input("Şifreniz")
        hak -= 1
        if (kullaici_adi == user_name or kullanici_mail == user_name) and (password == sifre):
           print("Başarılı")
           giris_basarili = True
           break
        else:
            print(f"Giriş bilgileriniz hatalı kalan hakkınız {hak}")
            continue
    if hak == 0:
        print("Hakınız Kalmadı")
        break
    if giris_basarili:
        break
"""


"""
### Kullanıcıdan alınacak sayının asal olup olmadıgını ekran yazddırınız.
### Asal sayı 1 ve kendisinden baska hiç bir sayıya bölünmeyen sayıdır.

asal_mi = True
i = 2
s = int(input("Asallığı kontrol edilecek sayıyı giriniz:"))
while i < s:
    if s % i ==0:
        asal_mi = False
        break
    i += 1

if asal_mi :
    print("Sayı asal")
else:
    print("Asal değil")

"""