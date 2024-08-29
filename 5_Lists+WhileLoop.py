#Listeler[], Index mantığı bundada geçerlidir.
isciler = ["Mehmet", "Mert", "Mahmut", "Harun", "Ali"]
print(isciler[0])
print(isciler[-2])
print(isciler[0:3])

#While Döngüsü
#0'dan 5'e kadar olan sayıları döngüyle yazdırmak.
i = 0
while i <= 5:
    print(i)
    i = i + 1

#BASİT HESAP MAKİNESİ
islem = input("Hangi işlemi yapmak istersiniz ? (+, -, *, /, **) ")
x = int(input("İlk sayiyi giriniz: "))
y = int(input("İkinci sayiyi giriniz: "))
if islem == "+":
    print("Sonuç: " + str(x + y))
elif islem == "-":
    print(x - y)
elif islem == "*":
    print(x * y)
elif islem == "/":
    if y == 0:
        print("Hata: Sifira bölme hatasi")
    else:
        print("Sonuç: " + str(x / y))
elif islem == "**":
    print(x ** y)
else:
    print("Geçersiz işlem seçimi")










