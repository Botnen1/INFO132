from statistics import mean


emner = []

karakterer = {"INFO100" : "A", "INFO132" : "A", "ExPhil" : "A"}

liste100 = []
liste200 = []
liste300 = []


#EmneLlister
def emneliste():
    global emner
    for i in emner:
        if i[-3] == "1":
            liste100.append(i)
    for i in emner:
        if i[-3] == "2":
            liste200.append(i)
    for i in emner:
        if i[-3] == "3":
            liste300.append(i)

            
    emnevalg = input("Skriv inn fagtype eller nivå (enter for alle): ")
    if emnevalg == "":
        print(emner)
    if emnevalg == "INFO":
        for i in emner:
            if "INFO" in i:
                print(i)
    if emnevalg == "ExPhil":
        for i in emner:
            if "ExPhil" in i:
                print(i)
    if emnevalg == "100":
        print(liste100)
        liste100.clear
        liste200.clear
        liste300.clear
    if emnevalg == "200":
        print(liste200)
        liste100.clear
        liste200.clear
        liste300.clear
    if emnevalg == "300":
        print(liste300)
        liste100.clear
        liste200.clear
        liste300.clear
    

#Legge til emner
def leggTilEmne():
    global emner
    nyttEmne = input("Hvilket emne ønker du å legge til?: ").upper()
    karakterpemne = input("Karakter: ").upper()
    emner.append(nyttEmne)
    karakterer.update({nyttEmne: karakterpemne})
    print("Du har nå disse emnene:", emner)
    

#settekarakter
def settKarakter():
    print(emner)
    fagvalg = input("Hvilket fag ønsker du å endre karakter på?: ").upper()
    nyKarakter = input("Ny karakter: ").upper()
    karakterer[fagvalg] = nyKarakter


#viser emner og karakterer
def visEmnerOgKarekterer():
    print(karakterer)


def clearliste():
    global liste100
    global liste200
    global liste300
    liste100.clear
    liste200.clear
    liste300.clear 


def bokstav(karakter):
    liste = {
        'A': 5,
        'B': 4,
        'C': 3,
        'D': 2,
        'E': 1,
        'F': 0,
    }
    if karakter in liste:
        return liste[karakter] 


def totaltsnitt():
    total = 0
    antallkarakter = 0
    for value in karakterer.values():
        antallkarakter += 1
        verdi = bokstav(value)
        total += verdi
        
    snittet = total / antallkarakter
    if snittet >= 4.5:
        print('Snittet er : A')
    elif 3.5 <= snittet < 4.5:
        print('Snittet er : B')
    elif 2.5 <= snittet < 3.5:
        print('Snittet er : C')
    elif 1.5 <= snittet < 2.5:
        print('Snittet er : D')
    elif 0.5 <= snittet < 1.5:
        print('Snittet er : E')
    else:
        print('Snittet er : F')


def snittper100():
    total = 0
    antallkarakterer = 0
    for k, v in karakterer.items():
        if "INFO1" in k:
            antallkarakterer += 1
            verdi = bokstav(v)
            total += verdi    
    snittet = total / antallkarakterer
    if snittet >= 4.5:
        print('Snittet er : A')
    elif 3.5 <= snittet < 4.5:
        print('Snittet er : B')
    elif 2.5 <= snittet < 3.5:
        print('Snittet er : C')
    elif 1.5 <= snittet < 2.5:
        print('Snittet er : D')
    elif 0.5 <= snittet < 1.5:
        print('Snittet er : E')
    else:
        print('Snittet er : F') 


def snittper200():
    total = 0
    antallkarakterer = 0
    for k, v in karakterer.items():
        if "INFO2" in k:
            antallkarakterer += 1
            verdi = bokstav(v)
            total += verdi    
    snittet = total / antallkarakterer
    if snittet >= 4.5:
        print('Snittet er : A')
    elif 3.5 <= snittet < 4.5:
        print('Snittet er : B')
    elif 2.5 <= snittet < 3.5:
        print('Snittet er : C')
    elif 1.5 <= snittet < 2.5:
        print('Snittet er : D')
    elif 0.5 <= snittet < 1.5:
        print('Snittet er : E')
    else:
        print('Snittet er : F') 


def snittper300():
    total = 0
    antallkarakterer = 0
    for k, v in karakterer.items():
        if "INFO3" in k:
            antallkarakterer += 1
            verdi = bokstav(v)
            total += verdi    
    snittet = total / antallkarakterer
    if snittet >= 4.5:
        print('Snittet er : A')
    elif 3.5 <= snittet < 4.5:
        print('Snittet er : B')
    elif 2.5 <= snittet < 3.5:
        print('Snittet er : C')
    elif 1.5 <= snittet < 2.5:
        print('Snittet er : D')
    elif 0.5 <= snittet < 1.5:
        print('Snittet er : E')
    else:
        print('Snittet er : F') 

def snittperINFO():
    total = 0
    antallkarakterer = 0
    for k, v in karakterer.items():
        if "INFO" in k:
            antallkarakterer += 1
            verdi = bokstav(v)
            total += verdi
    snittet = total / antallkarakterer
    if snittet >= 4.5:
        print('Snittet er : A')
    elif 3.5 <= snittet < 4.5:
        print('Snittet er : B')
    elif 2.5 <= snittet < 3.5:
        print('Snittet er : C')
    elif 1.5 <= snittet < 2.5:
        print('Snittet er : D')
    elif 0.5 <= snittet < 1.5:
        print('Snittet er : E')
    else:
        print('Snittet er : F') 

def snittperEX():
    total = 0
    antallkarakterer = 0
    for k, v in karakterer.items():
        if "ExPhil" in k:
            antallkarakterer += 1
            verdi = bokstav(v)
            total += verdi
    snittet = total / antallkarakterer
    if snittet >= 4.5:
        print('Snittet er : A')
    elif 3.5 <= snittet < 4.5:
        print('Snittet er : B')
    elif 2.5 <= snittet < 3.5:
        print('Snittet er : C')
    elif 1.5 <= snittet < 2.5:
        print('Snittet er : D')
    elif 0.5 <= snittet < 1.5:
        print('Snittet er : E')
    else:
        print('Snittet er : F') 



def snitt100():
    global liste100
    global emner
    global karakterer
    clearliste()
    snittper100()
    clearliste()


def snitt200():
    global liste200
    global emner
    global karakterer
    clearliste()
    snittper200()
    clearliste()
            

def snitt300():
    global liste300
    global emner
    global karakterer
    clearliste()
    snittper300()
    clearliste()


def snittINFO():
    global emner
    global karakterer
    snittperINFO()


def snittEX():      
    global emner
    global karakterer
    snittperEX()


def snitt():
    global emner
    global karakterer
    clearliste()
    snittAv = input("Skriv inn fagtype eller nivå (enter for alle):")
    if snittAv == "":
        totaltsnitt()

    if snittAv == "INFO":
        snittINFO()

    if snittAv == "ExPhil":
        snittEX()

    if snittAv == "100":
        snitt100()
        
    if snittAv == "200":
        snitt200() 
     
    if snittAv == "300":
        snitt300()  
        

def datainn(): 
    with open('data.txt', 'r') as f:
        inputL = []
        for i in f:
            inputL.append(i.strip())
 
        splitter = inputL.index('')
 
        emner.extend(inputL[1:splitter])
        karliste = inputL[splitter + 2:]

        for i in karliste:
            karakterer[i[:-3]] = i[-1]


def dataSave():
    with open('data.txt', 'w+') as f:
        f.write('Fag: \n')
        for i in sorted(emner):
            f.write(f'{i}\n')

        f.write('\nKarakterer:\n')
        for n in karakterer.items():
            f.write(f'{n[0]}: {n[1]}\n')


#quit
def avslutt():
    dataSave()
    quit()


#START
def start():
    starte = input("Ønsker du å start? (ja / nei): ").lower()
    while starte != "nei":
        valg()

datainn()


#Menyen til programmet
def valg():
    print("\n")
    print(".........................")
    print("1 - Emneliste\n2 - Legg til emne\n3 - Sett karakter\n4 - Karaktersnitt\n5 - Vis emner med karakterer\n6 - Lagre og Avslutt")
    print(".........................")
    valget = input("\nValg: ")

    if valget == "1":
        emneliste()

    if valget == "2":
        leggTilEmne()

    if valget == "3":
        settKarakter()

    if valget == "4":
        snitt()

    if valget =="5":
        visEmnerOgKarekterer()

    if valget == "6":
        avslutt()


start()