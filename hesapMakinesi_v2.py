# -*- coding: utf-8 -*-

class hesapMakinesi_v2(object):

       def __init__(self,sayi1,sayi2):

           self.sayi1 = sayi1
           self.sayi2 = sayi2


       def topla(self):

          return self.sayi1 + self.sayi2

       def cikar(self):

          return  self.sayi1 - self.sayi2

       def carp(self):

          return  self.sayi1 * self.sayi2

       def bol(self):

          return  self.sayi1 / self.sayi2

birincisayi = int(input("Birinci Sayıyı Giriniz: "))
ikincisayi  = int(input("İkinci Sayıyı Giriniz:  "))
secim = input("Yapmak İstediğiniz İşlemi Seçiniz\n1)Topla: \n2)Çıkar: \n3)Çarp: \n4)Böl: \n")
print("Seçilen İşlem Numarası:",secim)
hesapla = hesapMakinesi_v2(birincisayi,ikincisayi)

if secim == "1":

    print("Seçilen Sayıların Toplamı: ", hesapla.topla())    

elif secim == "2":

    print("Seçilen Sayıların Çıkarımı: ", hesapla.cikar())

elif secim == "3":
    
    print("Seçilen Sayıların Çarpımı: ", hesapla.carp())

elif secim == "4":

    print("Seçilen Sayıların Bölümü: ", hesapla.bol())        




