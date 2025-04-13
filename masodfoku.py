import math
import utmutato

def masodfoku():
    while True:
        utmutato.border()
        print("MÁSODFOKÚ EGYENLET MEGOLDÁSA")
        b=input("X^2:	")
        if b == "":
            utmutato.border()
            break
        b = int(b)
        r = b
        b=input("X:	")
        if b == "":
            utmutato.border()
            break
        b = int(b)
        w = b
        b=input("Konstans:	")
        if b == "":
            utmutato.border()
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