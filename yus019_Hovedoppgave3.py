from random import *
import pickle

#Hovedoppgave3
print("Hovedoppgave3\nyus019")
''' 
Kort fortalt:
Man bruker 32 kort (alle 2’ere – 6’ere fjernes 
fra kortstokken) som fordeles på 8 bunker. 
Kun det øverste kortet er synlig i hver bunke. 
I hvert trekk kan man fjerne to kort som 
har samme verdi og målet med spillet er å fjerne 
alle kortene. 
'''

'''
Lag et program som lar brukeren spille WISH SOLITAIRE.
'''


SPAR = '\u2660'
RUTER = '\u2666'
KLØVER = '\u2663'
HJERTER = '\u2665'
print(SPAR, RUTER, HJERTER, KLØVER)


kortstokk = []

for i in range(7, 15):
    kortstokk.append(f'\u2665 {i}')
    kortstokk.append(f'\u2663 {i}')
    kortstokk.append(f'\u2666 {i}')
    kortstokk.append(f'\u2660 {i}')
print("\nkortstokken")
print(kortstokk)

'''
Utvid programmet slik at man kan:
Lagre spillets tilstand til en fil
Lese in og fortsette et lagret spill
'''

def lagre1(kortene):
    pickle.dump(kortene, open("lagre1.p", "wb")) #Lagrer spillet ditt i en Pickle fil (lagre1.p) som kan hentes ut senere
    print("\n")
    print(RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER,)
    print("Spillet ble lagret!")
    print(RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER,"\n")
    print(RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER,)
    print("Lagret i i filen med navn 'lagre1.p'")
    print("Velg valg nummer '2' neste gang du spiller for å fortsette!")
    print(RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER,"\n")
    print(RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER,)
    print("Du kan nå velge å fortsette å spille, eller krysse ut.")
    print("Om du fortsetter må du huske å lagre på nytt før du avslutter :)")
    print(RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER,"\n")

def lagre2(kortene):
    pickle.dump(kortene, open("lagre2.p", "wb")) #Lagrer spillet ditt i en Pickle fil (lagre2.p) som kan hentes ut senere
    print("\n")
    print(RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER,)
    print("Spillet ble lagret!")
    print(RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER,"\n")
    print(RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER,)
    print("Lagret i i filen med navn 'lagre2.p'")
    print("Velg valg nummer '2' neste gang du spiller for å fortsette!")
    print(RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER,"\n")
    print(RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER,)
    print("Du kan nå velge å fortsette å spille, eller krysse ut.")
    print("Om du fortsetter må du huske å lagre på nytt før du avslutter :)")
    print(RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER,"\n")

def lagre3(kortene):
    pickle.dump(kortene, open("lagre3.p", "wb")) #Lagrer spillet ditt i en Pickle fil (lagre3.p) som kan hentes ut senere
    print("\n")
    print(RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER,)
    print("Spillet ble lagret!")
    print(RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER,"\n")
    print(RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER,)
    print("Lagret i i filen med navn 'lagre3.p'")
    print("Velg valg nummer '2' neste gang du spiller for å fortsette!")
    print(RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER,"\n")
    print(RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER,)
    print("Du kan nå velge å fortsette å spille, eller krysse ut.")
    print("Om du fortsetter må du huske å lagre på nytt før du avslutter :)")
    print(RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER,"\n")

    
def laste_inn_spill1():
    global bunker
    try:
        bunker = pickle.load(open("lagre1.p", "rb")) #Laster inn Pickle filen (lagre1.p) som inneholder spillet du sist lagret
        print("\nLastet inn spill fra fil\nFilen 'lagre1.p' ble åpnet.\nDu kan nå fortsette på spillet ditt.\nOm du vil lagre igjen kan du det, men husk at du da skriver over det du har gjort til nå.\n")
        spill(bunker)
    except FileNotFoundError: #Gir deg en feilmelding om du ikke har et spill lagret fra før
        print(RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER,)
        print("Du har ikke et lagret spill.")
        print(RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER,)

def laste_inn_spill2():
    global bunker
    try:
        bunker = pickle.load(open("lagre2.p", "rb")) #Laster inn Pickle filen (lagre2.p) som inneholder spillet du sist lagret
        print("\nLastet inn spill fra fil\nFilen 'lagre2.p' ble åpnet.\nDu kan nå fortsette på spillet ditt.\nOm du vil lagre igjen kan du det, men husk at du da skriver over det du har gjort til nå.\n")
        spill(bunker)
    except FileNotFoundError: #Gir deg en feilmelding om du ikke har et spill lagret fra før
        print(RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER,)
        print("Du har ikke et lagret spill.")
        print(RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER,)

def laste_inn_spill3():
    global bunker
    try:
        bunker = pickle.load(open("lagre3.p", "rb")) #Laster inn Pickle filen (lagre3.p) som inneholder spillet du sist lagret
        print("\nLastet inn spill fra fil\nFilen 'lagre3.p' ble åpnet.\nDu kan nå fortsette på spillet ditt.\nOm du vil lagre igjen kan du det, men husk at du da skriver over det du har gjort til nå.\n")
        spill(bunker)
    except FileNotFoundError: #Gir deg en feilmelding om du ikke har et spill lagret fra før
        print(RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER,)
        print("Du har ikke et lagret spill.")
        print(RUTER, RUTER, RUTER, RUTER, RUTER, RUTER, RUTER,)
        


def del_ut_kort(split):
    shuffle(split)
    split = [split[x:x + 4] for x in range(0, len(split), 4)]
    return split


def tap(kortene):
    kopi = []
    for item in kortene:
        try: 
            kopi.append(int(item[0][2:]))
        except:
            continue

    kopi_check = set(kopi)
    if len(kopi) == len(kopi_check):
        return True


def fjerne(kort1, kort2):
    global bunker
    listeMedTall = list("12345678")
    convert = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7}

    if kort1 != kort2 and kort1 in listeMedTall and kort2 in listeMedTall and bunker[convert[kort1]][0][2:] == bunker[convert[kort2]][0][2:]:
        bunker[convert[kort1]].pop(0)
        bunker[convert[kort2]].pop(0)
    else:
        print(KLØVER, KLØVER, KLØVER, KLØVER, KLØVER, KLØVER, KLØVER, )
        print("Ugyldig valg\nprøv igjen") #melding om feil dersom bruker skriver inn to bunker som ikke matcher
        print(KLØVER, KLØVER, KLØVER, KLØVER, KLØVER, KLØVER, KLØVER, )
        


def seier(kortene):
    if sum([len(x) for x in kortene]) == 0: 
        return True


def spill(kortene):
    listeMedTall = list("12345678")
    """ print(listeMedTall) """
    while True:
        if seier(kortene):
            print(HJERTER, SPAR, RUTER, KLØVER, HJERTER, SPAR, RUTER, KLØVER,)
            print("\nDu vant!\nDu fikk fjernet alle kortene")
            print(HJERTER, SPAR, RUTER, KLØVER, HJERTER, SPAR, RUTER, KLØVER,)
            break
        elif tap(kortene):
            print(HJERTER, SPAR, RUTER, KLØVER, HJERTER, SPAR, RUTER, KLØVER,)
            print("\nDu tapte :(\nBedre lykke neste gang!\n\nOm du hadde lagret underveis\nkan du gå tilbake for å \nfortsette fra der du lagret.")
            print(HJERTER, SPAR, RUTER, KLØVER, HJERTER, SPAR, RUTER, KLØVER,)
            break
        else:
            for index, bunke in enumerate(kortene):
                if len(bunke) > 0:
                    print(f'{listeMedTall[index]}: {bunke[0]} {" "* (len(bunke[0])%2)}{"X "* len(bunke[1:])}')
                elif len(bunke) <= 0:
                    print(f'{listeMedTall[index]}: '"bunken er tom")

            print("\nVil du lagre spillet?\nDu kan ha 3 ulike 'saves'\nskriv 'lagre1', 'lagre2', 'lagre3'\nDisse kan du laste inn om du vil fortsette på spillet ditt senere")
            spiller = input("Velg bunker (for eksempel 56)): ").upper()
            if spiller == "LAGRE1": 
                lagre1(kortene)
            elif spiller =="LAGRE2":
                lagre2(kortene)
            elif spiller =="LAGRE3":
                lagre3(kortene)
            else:
                if len(spiller) == 2:
                    kort1 = spiller[0]
                    kort2 = spiller[1]
                    fjerne(kort1, kort2)
                else: spill(kortene)

bunker = del_ut_kort(kortstokk)

""" print(bunker) """

def meny():
    global bunker


    print("\n\nVelkommen til Wish Solitaire\nOm du er usikker på reglene kan du sjekke disse her\nhttps://semicolon.com/Solitaire/Rules/TheWish.html\neller se denne videoen:\nhttps://www.youtube.com/watch?v=tk5YokL8yaA\n")
    print(HJERTER, SPAR, RUTER, KLØVER, HJERTER, SPAR, RUTER, KLØVER,)
    print("1 - Nytt Spill\n2 - Last Spill\n3 - Avslutt")
    print(HJERTER, SPAR, RUTER, KLØVER, HJERTER, SPAR, RUTER, KLØVER,"\n")

    valg_spiller = input("Valg: ")

    if valg_spiller == "1":
        bunker = del_ut_kort(kortstokk)
        spill(bunker)

    if valg_spiller == "2":
        print("Laste inn 'lagre1', 'lagre2', eller 'lagre3")
        versjon = input("Hvilket spill vil du hente ut? :")

        if versjon == "lagre1":
            laste_inn_spill1()

        elif versjon == "lagre2":
            laste_inn_spill2()

        elif versjon == "lagre3":
            laste_inn_spill3()


    if valg_spiller == "3":
        quit()

    else:
        print(SPAR, SPAR, SPAR, SPAR, SPAR, SPAR, SPAR,)
        print("Ugyldig valg!")
        print(SPAR, SPAR, SPAR, SPAR, SPAR, SPAR, SPAR,)

    

meny()

