import math
import utmutato, masodfoku, kamatoskamat, szamtani, mertani, kombinatorika, sikgeometria, tergeometria, szög, koordinata

while True:
    utmutato.border()
    print("MATEMATIKA 2024 CHEAT PROGRAM\n(1)Info\n(2)Programok\n(ENTER)Kilépés")
    a = input("Válasz:  ")
    print("\n")
    utmutato.border()
    if a == "":
        print("Kilépés...")
        utmutato.border()
        break
    if a == "1":
        utmutato.utmutato()
    elif a == "2":
        while True:
            print("(1)Másodfokú egyenlet\n(2)Kamatoskamat\n(3)Számtani sorozat\n(4)Mértani sorozat\n(5)Kombinatorika\n(6)Geometria\n(7)Szögfüggvények\n(8)Koordinátageometria\n(ENTER)Visszalépés")
            p = input("Válasz:  ")
            if p == "1":
                masodfoku.masodfoku()
            elif p == "2":
                kamatoskamat.kamatoskamat()
            elif p == "3":
                szamtani.szamtani()
            elif p == "4":
                mertani.mertani()
            elif p == "5":
                kombinatorika.kombinatorika()
            elif p == "6":
                print("(1)SíkGeometria, (2)Térgeometria, (ENTER)Visszalépés")
                u = input("Válasz:  ")
                if u == "1":
                    sikgeometria.sikgeometria()
                elif u == "2":
                    tergeometria.tergeometria()
                elif u == "":
                    break
            elif p == "7":
                szög.szög()
            elif p == "8":
                koordinata.koordinata()
            elif p == "":
                break