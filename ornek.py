"""
1- bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.
müşteri adı
müşteri soy adı
müşteri ad + soyad
müşteri cinsiyet 
müşteri tc
müşteri doğum yılı
adres bilgisi
yaş
"""
musteriAdi = "nursu"
musteriSoyad = "girit"
musteriAdSoyad = musteriAdi + ' ' + musteriSoyad
musteriCinsiyet = True #kadın
musteriTc = '12345678910' #string
musteriDogumYili = 2002
musteriAdres = "İstanbul Sarıyer"
musteriYasi = 2019 - musteriDogumYili


"""
2- aşağıdaki siparişlerin toplam bilgisini hesaplayınız 

sipariş 1 => 110 tl
sipariş 2 => 1110.5 tl
sipariş 3 => 356.65 tl
"""

print(110 + 1110.5 + 356.65)
order1 = 110
order2 = 1110.5
order3 = 356.65
print(order1 + order2 + order3)
total = order1 + order2 + order3
print("total:", total)