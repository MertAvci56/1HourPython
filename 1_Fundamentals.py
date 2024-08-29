#String ifadeler "arasına" alınır.
print("hello World!")

x = 14
print(x)
print(type(x)) #Değişkenin türünü gösterir.

isim = "Selahaddin" #String
yas = 20 #Integer
kilo = 78.5 #Float
burdaMi = True #Bool/Boolean
print(type(kilo))

#Kullanıcıdan çıktı almak:
name = input("What's your name? ")
print("Hello " + name)
food = input("What's your favorite food? ")
print(name + " " + food + " Sever")

#Tür değiştirme:
name = "Mert"
yas = 20
print(name + " " + str(yas) + " Yaşinda")

#Aritmetik İşlemler
x = 9
y = 5
print(x + y) #Toplama
print(x - y) #Çıkarma
print(x * y) #Çarpma
print(x / y) #Bölme
print(x // y) #Küsuratı almayan bölme işlemidir.
print(x % y) #Remainder = Bölümden kalanı verir.
print(x ** y) #Üssünü verir.

#Kullanıcıdan inputla alınan veri stringdir, "TÜR DEĞİŞTİRME" yapmalısın.
#1.YOL
a = input("First number: ")
b = input("Second number: ")
print(int(a) + int(b))
#2.YOL
a = int(input("First number: "))
b = int(input("Second number: "))
print(a + b)
#Değişkensiz Yol:
print(int(input("First number: ")) + int(input("Second number: ")))

