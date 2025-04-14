import math
import utmutato, masodfoku, kamatoskamat, szamtani, mertani, kombinatorika, sikgeometria, tergeometria, szög, koordinata

utmutato.border()
while True:
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
            print("(1)Másodfokú egyenlet\n(2)Kamatoskamat\n(3)Számtani sorozat\n(4)Mértani sorozat\n(5)Kombinatorika\n(6)Síkgeometria\n(7)Térgeometria(8)Szögfüggvények\n(9)Koordinátageometria\n(ENTER)Visszalépés")
            p = input("Válasz:  ")
            if p == "1":
                masodfoku.masodfoku()
                utmutato.border()
            elif p == "2":
                kamatoskamat.kamatoskamat()
                utmutato.border()
            elif p == "3":
                szamtani.szamtani()
                utmutato.border()
            elif p == "4":
                mertani.mertani()
                utmutato.border()
            elif p == "5":
                utmutato.nincskesz("Kombinatorika")
                #kombinatorika.kombinatorika()
                utmutato.border()
            elif p == "6":
                utmutato.nincskesz("Síkgeometria")
                #sikgeometria.sikgeometria()
                utmutato.border()
            elif p == "7":
                utmutato.nincskesz("Térgeometria")
                #tergeometria.tergeometria()
                utmutato.border()
            elif p == "8":
                utmutato.nincskesz("Szögfüggvények")
                #szög.szög()
                utmutato.border()
            elif p == "9":
                utmutato.nincskesz("Koordinátageometria")
                #koordinata.koordinata()
                utmutato.border()
            elif p == "":
                break
            else:
                print("Rossz input")
                utmutato.border()