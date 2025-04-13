import math
import utmutato

def szamtani():
    while True:
        utmutato.border()
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
            utmutato.border()
            break