import math
import random

print("\n\n\nOPPGAVE 1")


def pi(d=2):
    antall_Desimaler = round(math.pi, d)
    if d > 15:
        return "For mange desimaler, bruk lavere tall"
    return antall_Desimaler

print(pi(3))

print("\n\n\nOPPGAVE 2")

def temperaturkonvertering(temp, var):
    celcius = (temp * (9/5)+32)
    farenheit = (temp - 32) * (5/9)
    if var == "c":
        return celcius, "Fahrenheit"
    if var == "f":
        return farenheit, "Celcius"
    if var == "":
        return celcius, "Fahrenheit"

print(temperaturkonvertering(30, "c" ))




print("\n\n\nOPPGAVE 4")

def tilfeldige_tall():
    x = random.randrange(0, 9)
    y = random.randrange(0, 9)
    z = random.randrange(0, 9)
    tall = [x, y, z]
    tall.sort()
    return tall
print(tilfeldige_tall())




print("\n\n\nOPPGAVE 3")

saldo = 500
rentesats = 1.01
endringer = [0, 0, 0]


#VIS SALDO
def visSaldo():
    print("\nDin saldo er:", saldo,"kr")

#INNSKUDD
def innskudd():
    global saldo
    global endringer
    print("Du har:", saldo, "kr på konto...")
    penger_inn = float(input("Hvor mye ønsker du å sette inn?: "))
    nysaldo = saldo + penger_inn
    print("\nDu satt inn:", penger_inn, "kr, ny saldo er:", nysaldo, "kr")
    saldo = nysaldo
    endringer += ["+" + str(penger_inn)]

#UTTAK
def uttak():
    global saldo
    global endringer
    print("Du har:", saldo, "kr på konto...")
    penger_ut = float(input("Hvor mye ønsker du å ta ut?: "))
    if penger_ut < saldo:
        nysaldo = saldo - penger_ut
        saldo = nysaldo
        print("\nDu tok ut:", penger_ut, "kr, ny saldo er:", nysaldo, "kr")
        endringer += ["-" + str(penger_ut)]
    else:
        print("Du kan ikke ta ut med enn du har!")

#RENTEBEREGNING
def renteRegning():
    global endringer
    if saldo > 1000000:
        print("Du har:", saldo, "kr på konto...\nDin rente er:", 1.02)
        utregnet = saldo * 1.02
        print("\nEtter renter er din saldo:", utregnet,"kr")
        endringer += ["r " + str(utregnet)]
    else:
        print("Du har:", saldo, "kr på konto...\nDin rente er:", rentesats)
        utregnet = saldo * rentesats
        print("\nEtter renter er din saldo:", utregnet, "kr")
        endringer += ["r " + str(utregnet)]

#ENDERINGER
def endring():
    print(endringer[-3])
    print(endringer[-2])
    print(endringer[-1])
    print("Nå er saldoen",saldo, "kr")


#GRENSESNITT
def valg():
    print("\nBanken tilbyr disse valgene: ")
    print(".........................")
    print("1 - Vis Saldo\n2 - Innskudd\n3 - Uttak\n4 - Renteutregning\n5 - Dine 3 siste kontoendringer\n6 - Avslutt")
    print(".........................")
    valget = input("\nValg: ")
    if valget == "1":
        visSaldo()
    if valget == "2":
        innskudd()
    if valget == "3":
        uttak()
    if valget == "4":
        renteRegning()
    if valget == "5":
        endring()
    if valget == "6":
        quit()



#BANKEN_START
def start():
    startes = input("Ønsker du å starte? ( ja / nei ): ")
    while startes == "ja":
        valg()


start()

