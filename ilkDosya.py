# 1-> Toplama 2->Çıkarma 3->Çarpma 4->Faktöriyel
import random
import time
import math

while True:
    a = random.randint(1,4)

    print("Lütfen bekleyin yeni soru hazırlanıyor...")
    time.sleep(2)

    if a == 1:
        print("Toplama İşlemi->")
        ilksayi = random.randint(1,20)
        ikincisayi = random.randint(1,20)
        print("Lütfen",ilksayi,"ile",ikincisayi,"sayılarının toplamını giriniz.")
        sonuc = int(input("Cevap :"))

        if (sonuc==ilksayi+ikincisayi):
            print("Sonucu doğru bildiniz.")
            time.sleep(2)
        else:
            print("Yanlış Cevap Verdiniz. Doğru Cevap :",ilksayi+ikincisayi)
            time.sleep(2)
    elif a == 2:
        print("Çıkarma İşlemi ->")
        ilksayi = random.randint(1,20)
        ikincisayi = random.randint(1,20)
        print("Lütfen",ilksayi,"-",ikincisayi,"işleminin sonucunu giriniz :")
        sonuc = int(input("Cevap :"))

        if (sonuc == ilksayi-ikincisayi):
            print("Tebrikler Doğru bildiniz!")
            time.sleep(2)
        else:
            print("Yanlış! Doğru Cevap :",ilksayi-ikincisayi)
            time.sleep(2)

    elif a == 3:
        print("Çarpma İşlemi ->")
        ilksayi = random.randint(1, 10)
        ikincisayi = random.randint(1, 10)
        print("Lütfen", ilksayi, "x", ikincisayi, "işleminin sonucunu giriniz :")
        sonuc = int(input("Cevap :"))

        if (sonuc == ilksayi*ikincisayi):
            print("Tebrikler Doğru bildiniz!")
            time.sleep(2)
        else:
            print("Yanlış! Doğru Cevap :", ilksayi*ikincisayi)
            time.sleep(2)

    elif a == 4:
        print("Faktöriyel İşlemi ->")
        ilksayi = random.randint(1,5)
        print("Lütfen",ilksayi,"sayısının faktöriyelini hesaplayınız.")
        sonuc = int(input("Cevap :"))

        if (sonuc == math.factorial(ilksayi)):
            print("Tebrikler bildiniz.")
            time.sleep(2)
        else:
            print("Yanlış! Doğru Cevap :",math.factorial(ilksayi))
