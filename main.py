import math
import utmutato
import masodfoku
import kamatoskamat
import szamtani
import mertani

def border():
	print("§∆×•~====================~•×∆§")
def masodfoku():
    while True:
        border()
        print("MÁSODFOKÚ EGYENLET MEGOLDÁSA")
        b=input("X^2:	")
        if b == "":
            border()
            break
        b = int(b)
        r = b
        b=input("X:	")
        if b == "":
            border()
            break
        b = int(b)
        w = b
        b=input("Konstans:	")
        if b == "":
            border()
            break
        b = int(b)
        c = b
        d= -1*w
        e=(w**2)-(4*r*c)
        if e < 0:
            print("Nincs megoldás, Gyök alá negatív szám jön ki")
        else:
            if e == 0:
                print("Egy megoldása van")
            if e > 0:
                print("Két megoldása van")
            f=e**(1/2)
            g=(d +f)/(2*r)
            h=(d-f)/(2*r)
            print("Első Gyök:	",g)
            if g != h:
                print("Második Gyök:	",h)                
def kamatoskamat():
    while True:
        border()
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
            border()
            break
def szamtani():
    while True:
        border()
        print("SZÁMTANI SOROZAT")
        b = input("(1)Két különböző tag VAGY (2)két egyenlet, (3)Sn, (4)Tagja-e a sorozatnak, (ENTER)Visszalépés: ")
        if b == "1":
            c = int(input("Hanyadik tag?: "))
            d = int(input("Mennyivel egyenlő?: "))
            e = int(input("Hanyadik tag?: "))
            f = int(input("Mennyivel egyenlő?: "))
            if c > e:
                g = c - e
                h = d - f
            else:
                g = e - c
                h = f - d
            i = h / g
            j = d - (i * (c - 1))
            print("Az első tag:", j)
            print("A differenciál:", i)
    
        elif b == "2":
            c = int(input("Első sor, Első tag? "))
            d = int(input("Első sor, Második tag? "))
            e = int(input("Első sor, Mennyi? "))
            f = int(input("Második sor, Első tag? "))
            g = int(input("Második sor Második tag? "))
            h = int(input("Második sor mivel egyenlő? "))
            i = (c - 1) + (d - 1)
            j = (f - 1) + (g - 1)
            if e > h:
                z = (e - h) / (i - j)
            elif h > e:
                z = (h - e) / (j - i)
            y = ((e - (z * i))/2)
            print("Differenciál =", z)
            print("Első tag =", y)
        elif b == "3":
                dd = int(input("Hány tagot kérsz?: "))
                j = int(input("Első tag értéke:  "))
                i = int(input("Differenciál értéke:  "))
                jj = j + ((dd - 1) * i)
                gh = dd * ((j + jj) / 2)
                print("Az összeg:", gh)
        elif b == "4":
            df = int(input("írd be a számot: "))
            j = int(input("Első tag értéke:  "))
            i = int(input("Differenciál értéke:  "))
            t = (df - j)
            tt = (t / i) + 1
            uu = -(-tt // 1)
            if tt != uu:
                print("Nem tagja a sorozatnak!")
            elif tt == uu:
                print("A", tt, "tagja a sorozatnak")
        elif b == "":
            border()
            break
def mertani():
    while True:
        border()
        print("MÉRTANI SOROZAT")
        b = input("(1)Két különböző tag VAGY (2)két egyenlet, (3)Sn, (4)Tagja-e a sorozatnak, (ENTER)Visszalépés: ")
        if b == "1":
            c = int(input("Hanyadik tag?: "))
            d = int(input("Mennyivel egyenlő?: "))
            e = int(input("Hanyadik tag?: "))
            f = int(input("Mennyivel egyenlő?: "))
            if c > e:
                g = c - e
                h = d / f
            else:
                g = e - c
                h = f / d
            i = h / g
            j = d / (i ** (c - 1) )
            print("Az első tag:", j)
            print("Kóciens:", i)
    
        elif b == "2":
            c = int(input("Első sor, Első tag? "))
            d = int(input("Első sor, Második tag? "))
            e = int(input("Első sor, Mennyi? "))
            f = int(input("Második sor, Első tag? "))
            g = int(input("Második sor Második tag? "))
            h = int(input("Második sor mivel egyenlő? "))
            p = c
            l = d
            if e > h:
                sum = e / h
            elif h > e:
                sum = h / e
            if ((c < d) and (c < f) and (c < g)):
                d -= c
                f -= c
                g -= c
                c = 1
            elif ((d < c) and (d < f) and (d < g)):
                c -= d
                f -= d
                g -= d
                d = 1
            elif ((f < d) and (f < c) and (f < g)):
                d -= f
                c -= f
                g -= f
                f = 1
            elif ((g < d) and (g < c) and (g < f)):
                d -= g
                f -= g
                c -= g
                g = 1
            if ((c > d) and (c > f) and (c > g)):
                koc = d
            elif ((c < d) and (d > f) and (d > g)):
                koc = c
            elif ((f > d) and (f > c) and (f > g)):
                koc = g
            elif ((g > d) and (g > f) and (g > c)):
                koc = f
            z = sum**(1/koc)
            if koc % 2 == 0:
                zz = -1 * z
                print("1. Kóciens: ", zz)
                print("2. Kóciens: ", z)
            else:
                print("Kóciens: ", z)
            dvtk = (z**(p-1))+(z**(l-1))
            print("osztando: ", dvtk)
            y = e / dvtk
            print("Első tag =", y)
        elif b == "3":
                dd = int(input("Hány tagot kérsz?: "))
                j = int(input("Első tag értéke:  "))
                i = int(input("Differenciál értéke:  "))
                gh = (j * ((i**(dd))-1))/(i - 1)
                print("Az összeg:", gh)
        elif b == "4":
            df = int(input("írd be a számot: "))
            j = int(input("Első tag értéke:  "))
            i = int(input("Differenciál értéke:  "))
            t = (df / j)
            tt = math.log10(t) / math.log10(i)
            tt += 1
            uu = -(-tt // 1)
            if tt != uu:
                print("Nem tagja a sorozatnak!")
            elif tt == uu:
                print("A", tt, "tagja a sorozatnak")
        elif b == "":
            border()
            break
def kombinatorika():
    while True:
        border()
        print("KOMBINATORIKA")
        print("Nem elérhető még")
        border()
        break
def sikgeometria():
    while True:
        border()
        print("SÍKGEOMETRIA")
        print("Fejlesztés alatt, ne használd még")
        print("(1)Háromszög, (2)Négyzet, (3)Téglalap, (4)Trapéz, (5)Paralelogramma, (6)Rombusz, (7)Kör, (ENTER)Visszalépés")
        a = input("Válasz:  ")
        if a == "1":
            a = a
        elif a == "2":
            a = a
        elif a == "3":
            a = a
        elif a == "4":
            a = a
        elif a == "5":
            a = a
        elif a == "6":
            a = a
        elif a == "7":
            a = a
        elif a =="":
            border()
            break
def tergeometria():
    while True:
        border()
        print("TÉRGEOMETRIA")
        print("Fejlesztés alatt, ne használd még")
        print("(1)Háromszög, (2)Négyzet, (3)Téglalap, (4)Trapéz, (5)Paralelogramma, (6)Rombusz, (7)Kör, (ENTER)Visszalépés")
        a = input("Válasz:  ")
        if a == "1":
            a = a
        elif a == "2":
            a = a
        elif a == "3":
            a = a
        elif a == "4":
            a = a
        elif a == "5":
            a = a
        elif a == "6":
            a = a
        elif a == "7":
            a = a
        elif a =="":
            border()
            break
def szög():
    while True:
        border()
        print("SZÖGFÜGGVÉNYEK")
        print("Még nincs kész")
        print("(1)Sin-tétel és Cos-tétel, (2)Trigonometrikus Szögfüggvények, (ENTER)Visszalépés")
        z = input("Válasz:  ")
        if z == "1":
            a = int(input("a: "))
            b = int(input("b: "))
            c = int(input("c: "))
            alfa = int(input("alfa: "))
            beta = int(input("beta: "))
            gamma = int(input("gamma: "))
            if ((a != 0) and (b != 0) and (c != 0)):
                gamma = math.acos((((a*a)+(b*b)-(c*c))/2*a*b))
            elif ((a != 0) and (b != 0) and (gamma != 0)):
                c = ((a*a)+(b*b)-(2*a*b*(math.cos(gamma))))**(1/2)
            elif ((a != 0) and (c != 0) and (gamma != 0)):
                b = ((c*c) - (a*a) + (2*a*b*(math.cos(gamma))))**(1/2)
            elif ((b != 0) and (c != 0) and (gamma != 0)):
                a = ((c*c) - (b*b) + (2*a*b*(math.cos(gamma))))**(1/2)
            print(a, b, c, alfa, beta, gamma)
            if ((a != 0) and (b != 0) and (alfa != 0)):
                break
            elif ((a != 0) and (b != 0) and (beta != 0)):
                break

            elif ((a != 0) and (c != 0) and (alfa != 0)):
                break
            elif ((a != 0) and (c != 0) and (gamma != 0)):
                break

            elif ((c != 0) and (b != 0) and (beta != 0)):
                break
            elif ((c != 0) and (b != 0) and (gamma != 0)):
                break

            elif ((a != 0) and (beta != 0) and (alfa != 0)):
                break
            elif ((b != 0) and (beta != 0) and (alfa != 0)):
                break

            elif ((a != 0) and (gamma != 0) and (alfa != 0)):
                break
            elif ((c != 0) and (gamma != 0) and (alfa != 0)):
                break

            elif ((b != 0) and (beta != 0) and (gamma != 0)):
                break
            elif ((c != 0) and (beta != 0) and (gamma != 0)):
                break

        elif z == "2":
            break
        elif z == "":
            border()
            break
def koordináta():
    border()
    print("KOORDINÁTAGEOMETRIA")
    print("Nincs még kész")
    border()
while True:
    border()
    print("MATEMATIKA 2024 CHEAT PROGRAM\n(1)Info\n(2)Programok\n(ENTER)Kilépés")
    a = input("Válasz:  ")
    print("\n")
    border()
    if a == "":
        print("Kilépés...")
        border()
        break
    if a == "1":
        border()
        print("Másodfokú egyenlet: Megmondja a gyököket, illetve ha nem lehet megoldani a feladatot.\n5x^2 + 2x - 4 = 0\n 5 -> x^2\n2->x\n-4->Konstans\n")
        border()
        print("Kamatoskamat: Kiszámolja a hiányzó adatot, melyek a következők:\nVégösszeg: Tn jelzés\nKezdőösszeg: T0 jelzésű\nIdőszakok száma: n jelzés, ahol vedd figyelembe hogy nem csak évente lehetnek\nKamatláb: p jelzés\nEzen kívül Gyüjtőjáradékot is számol és törlesztőrészletet\n")
        border()
        print("Számtani sorozat: Megoldja az 1 és 2 soros számtani sorozatokat.\nKét különböző tag esetén Pl: a5 = 32 és a2 = 20 ekkor kiszámítja a1 és d-t.\nKét egyenlet esetén: a2 + a4 = 20 és a4 + a7 = 34\n Hanyadik tag mindig az a indexére kérdez rá, pl a5 indexe az 5\n")
        border()
        print("Mértani sorozat: Megoldja az 1 és 2 soros mértani sorozatokat.\nKét különböző tag esetén Pl: a5 = 32 és a2 = 8 ekkor kiszámítja a1 és q-t.\nKét egyenlet esetén: a2 + a4 = 40 és a4 + a7 = 80\n Hanyadik tag mindig az a indexére kérdez rá, pl a5 indexe az 5\n")
        border()
        print("Kombinatorika: Nincs kész\n")
        border()
        print("Geometria: Nincs kész\n")
        border()
        print("Szögfüggvények: Nincs kész\n")
        border()
        print("Koordinátageometria: Nincs kész\n")
        border()
    elif a == "2":
        while True:
            print("(1)Másodfokú egyenlet\n(2)Kamatoskamat\n(3)Számtani sorozat\n(4)Mértani sorozat\n(5)Kombinatorika\n(6)Geometria\n(7)Szögfüggvények\n(8)Koordinátageometria\n(ENTER)Visszalépés")
            p = input("Válasz:  ")
            if p == "1":
                masodfoku()
            elif p == "2":
                kamatoskamat()
            elif p == "3":
                szamtani()
            elif p == "4":
                mertani()
            elif p == "5":
                kombinatorika()
            elif p == "6":
                print("(1)SíkGeometria, (2)Térgeometria, (ENTER)Visszalépés")
                u = input("Válasz:  ")
                if u == "1":
                    sikgeometria()
                elif u == "2":
                    tergeometria()
                elif u == "":
                    break
            elif p == "7":
                szög()
            elif p == "8":
                koordináta()
            elif p == "":
                break