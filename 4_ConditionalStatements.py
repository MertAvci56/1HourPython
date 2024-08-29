#KOŞULLU İFADELER:
# İF = İSE, EĞER
# ElSE İF/ELİF = DEĞİLSE, AKSİ TAKDİRDE
# ELSE = HİÇBİRİYSE / HİÇBİRİ DEĞİLSE

bulutlu = True  # veya False
yagmurlu = False  # veya True
if bulutlu:
    if yagmurlu:
        print("Şemsiye tak!")
    else:
        print("Yağmura hazir ol!")
else:
    print("Güneşin tadini çikar :) ")

#AND, OR, NOT OPERATORS / VE, VEYA, DEĞİL OPERATÖRLERİ
# İŞLEM SIRASI
# 1- Not
# 2- And
# 3- Or
bulutlu = True  # veya False
yagmurlu = False  # veya True
if bulutlu and yagmurlu:
    print("Şemsiye tak")
elif bulutlu and yagmurlu == False:
    print("Yağmura hazir ol")
else:
    print("Güneşin tadini çikar")

ehliyet = True
araba = True
if ehliyet and araba:
    print("Araba kullanabilirsin")
elif araba and not ehliyet:
    print("Kursumuza gelin hemen Ehliyet alin")
elif ehliyet or araba:
    print("Az daha sabret")
else:
    print("Araba kullanmana daha çok var")


#KARŞILAŞTIRMA OPERATÖRLERİ
# == Eşit mi ? / Eşit midir ? / Eşitse ... KONTROLÜNÜ SAĞLAR.
# != Eşit değil mi ? / Eşit değil midir ? / Eşit değilse ...
# <= Küçük eşittir , >= Büyük eşittir ...
derece = int(input("What is the temperature? "))
if derece >= 30:
    print("Very HOT!")
elif derece <= 0:
    print("Very COLD!")

yas = int(input("How old are you? "))
school = input("Are you studying at school? y/n ").lower()
# .lower() komutuyla büyük/küçük harf uyumunu kapatırız.
if yas >= 18 and school == "n":
    print("Askere Gelme Yaşiniz Geldi!")
elif yas >= 18 and school == "y":
    print("Okulunuz Bittiğinde Askere Geleceksiniz!")
else:
    print("Askerlik Yaşiniz Daha Gelmedi!")

