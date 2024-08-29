#Tek tırnaklada string kaydedebilirsin.
name = 'selahaddin'

#Ama dezavantajları var:
name0 = "Mert'in"

"""
Bu uzun bir yorumdur.
Birden fazla satıra yayılabilir.
"""

ogrenci = """Selahaddin Mert
21 yaşinda, 178cm boyunda, 78 kilodur."""
print(ogrenci)

#INDEKS[START:STOP:STEPPİNG SİZE] (0'DAN BAŞLAR)
#INDEX[-1] = Sonuncu index'i verir.
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[0:3]) #0'dan başlar ama 3. alınmaz.
print(name[-4:-1]) #-4'den başladı ama -1. alınmadı.

#STRING FUNCTİONS

# String Length Function (METİN UZUNLUĞUNU HESAPLAR)
print(len(name))

# Title Function (HER KELİMENİN İLK HARFİNİ BÜYÜK, GERİ KALANINI KÜÇÜK YAPAR)
print(ogrenci.title())

# Capitalize Function (SADECE İLK KELİMENİN İLK HARFİNİ BÜYÜK, GERİ KALANINI KÜÇÜK YAPAR)
print(ogrenci.capitalize())

# Upper Function (TÜM HARFLERİ BÜYÜK HARFE DÖNÜŞTÜRÜR)
print(ogrenci.upper())

# Lower Function (TÜM HARFLERİ KÜÇÜK HARFE DÖNÜŞTÜRÜR)
print(ogrenci.lower())

# Find Function (METİNDE BİR ALT DIZİNİN KONUMUNU BULUR; BULUNAMAZSA -1 DÖNER)
print(ogrenci.find('S'))

ogrenci = """Selahaddin Mert
21 yaşinda, 178cm boyunda, 78 kilodur."""
print(ogrenci)

#INDEKS[START:STOP:STEPPİNG SİZE] (0'DAN BAŞLAR)
#INDEX[-1] = Sonuncu index'i verir.
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[0:3]) #0'dan başlar ama 3. alınmaz.
print(name[-4:-1]) #-4'den başladı ama -1. alınmadı.

#STRING FUNCTİONS

# String Length Function (METİN UZUNLUĞUNU HESAPLAR)
print(len(name))

# Title Function (HER KELİMENİN İLK HARFİNİ BÜYÜK, GERİ KALANINI KÜÇÜK YAPAR)
print(ogrenci.title())

# Capitalize Function (SADECE İLK KELİMENİN İLK HARFİNİ BÜYÜK, GERİ KALANINI KÜÇÜK YAPAR)
print(ogrenci.capitalize())

# Upper Function (TÜM HARFLERİ BÜYÜK HARFE DÖNÜŞTÜRÜR)
print(ogrenci.upper())

# Lower Function (TÜM HARFLERİ KÜÇÜK HARFE DÖNÜŞTÜRÜR)
print(ogrenci.lower())

# Find Function (METİNDE BİR ALT DIZİNİN KONUMUNU BULUR; BULUNAMAZSA -1 DÖNER)
print(ogrenci.find('S'))

# Replace Function (BİR ALT DİZİYİ BELİRLENEN YENİ DİZİYLE DEĞİŞTİRİR)
print(ogrenci.replace('Selahaddin', 'Mehmet'))

#ÖDEV-1
# Kullanıcıdan ismini al
isim = input("Lütfen isminizi girin: ")
# İlk harfi büyük, geri kalanı küçük yapmak için işlemi yap
duzenlenmis_isim = isim.capitalize()
# Sonucu ekrana yazdır
print("Düzenlenmiş isim:", duzenlenmis_isim)

