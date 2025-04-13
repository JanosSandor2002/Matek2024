import math
import utmutato

def kamatoskamat():
    while True:
        utmutato.border()
        print("KAMATOS KAMAT")
        b = input("(1)Kezdőösszeg, (2)Végösszeg, (3)Időszakok száma, (4)Kamat%, (5)Gyüjtőjáradék, (6)Törlesztőrészlet, (ENTER)Kilépés:	")
        if b == "2":
            c= int(input("Kezdőösszeg:	"))
            d= int(input("Időszakok száma:	"))
            e= int(input("Kamat%:	"))
            f= c*((100+e)/100)**d
            print("Végösszeg:  ", f)
        elif b == "3":
            c= int(input("Kezdőösszeg:	"))
            d= int(input("Végösszeg:	"))
            e= int(input("Kamat%:	"))
            f= d / c
            h = (100+e) / 100
            g = math.log10(f) / math.log10(h)
            print("Idószakok száma:  ", math.ceil(g))
        elif b == "1":
            c= int(input("Végösszeg:	"))
            d= int(input("Időszakok száma:	"))
            e= int(input("Kamat%:	"))
            f= ((100+e) / 100)**d
            g= c / f
            print("Kezdőösszeg:  ", g)
        elif b == "4":
            c= int(input("Végösszeg:	"))
            d= int(input("Időszakok száma:	"))
            e= int(input("Kezdőösszeg:	"))
            f= c / e
            g= f**(1 / d)
            h= (g*100) - 100
            print("Kamat%:  ", h)
        elif b == "5":
            while True:
                print("GYÜJTŐ JÁRADÉK")
                print("(1)Végösszeg, (2)Kezdőösszeg, (3)Időszakok száma, (ENTER)Visszalépés")
                j = input("Válasz:  ")
                if j == "1":
                    a = int(input("Kezdőösszeg:  "))
                    b = int(input("Kamat:  "))
                    b = (b + 100) / 100
                    c = int(input("Időszakok száma:  "))                        
                    d = ((a * b) * (((b**c)-1)) / (b - 1))
                    print("Végösszeg:  ", d)
                elif j == "2":
                    a = int(input("Végösszeg:  "))
                    b = int(input("Kamat:  "))
                    b = (b / 100) + 1
                    c = int(input("Időszakok száma:  "))
                    d = (((d * (b - 1)) / b) / ((b**c) - 1))
                    print("Kezdőösszeg:  ", d)
                elif j == "3":
                    a = int(input("Kezdőösszeg:  "))
                    b = int(input("Kamat:  "))
                    b = (b / 100) + 1
                    c = int(input("Végösszeg:  "))
                    d = ((((c / a) / b) * (b - 1)) + 1)
                    d = math.log10(d) / math.log10(b)
                    print("Időszakok száma:  ", d)
                elif j == "":
                    break
        elif b == "6":
            while True:
                print("TÖRLESZTŐ RÉSZLET")
                print("(1)ElosztottÖsszeg, (2)technikai kamat, (3)ÖsszesPénz, (ENTER)Visszalépés")
                f = input("Válasz:  ")
                if f == "1":
                    a = int(input("ÖsszesPénz:  "))
                    b = int(input("TechnikaiKamat:  "))
                    b = b / 100
                    d = int(input("Kamat%:  "))
                    d = (d + 100) / 100
                    c = int(input("Időszakok száma:  "))
                    e = (((a * (d**(c - 1))) * b) / ((d**c) - 1))
                    i = e / 12
                    print("A megadott időszakra elosztott pénz: ", e)
                    print("Egy évre erg egy hónapra elosztott pénz:  ", i)
                elif f == "2":
                    a = int(input("ÖsszesPénz:  "))
                    b = int(input("ElosztottPénz:  "))
                    d = int(input("Kamat%:  "))
                    d = (d + 100) / 100
                    c = int(input("Időszakok száma:  "))
                    e = (((b * ((d**c)-1)) / a) / (d**(c-1)))
                    print("Technikai kamat: ", e)
                elif f == "3":
                    a = int(input("ElosztottPénz:  "))
                    b = int(input("TechnikaiKamat:  "))
                    b = b / 100
                    d = int(input("Kamat%:  "))
                    d = (d + 100) / 100
                    c = int(input("Időszakok száma:  "))
                    e = (((a * ((d**c)-1)) / b) / (d**(c-1)))
                    print("Összepénz: ", e)
                elif f == "":
                    break
        elif b == "":
            utmutato.border()
            break