import math
import utmutato

def szög():
    while True:
        utmutato.border()
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
            utmutato.border()
            break