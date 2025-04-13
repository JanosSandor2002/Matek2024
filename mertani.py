import math
import utmutato

def mertani():
    while True:
        utmutato.border()
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
            utmutato.border()
            break