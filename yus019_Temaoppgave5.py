print("Oppgave 1")

def fak(n):
    middel = 1
    for i in range(1,n+1):
        middel *= i
    return middel
print(fak(4))

def faku(x):
    n = 1
    while x > 0:
        n = x*n
        x-=1
    return n


print(faku(4))




print("\n\nOppgave 2")

class Monark:
    def __init__(monark, nasjon, navn, fra):
        monark.nasjon = nasjon
        monark.navn = navn
        monark.fra = fra

    def skriv(monark):
        print(monark.navn + " av " + monark.nasjon + " på tronen fra " + str(monark.fra))


    def etterfølger(self, neste):
        self.nesteMonark = neste


haakon = Monark("Norge", "Kong Haakon VII", 1905)
olav = Monark("Norge", "Kong Olav V", 1957)
harald = Monark("Norge", "Kong Harald V", 1991)

def rekkefølge():
    kongerekke = [haakon.skriv(), olav.skriv(), harald.skriv()]
    return(kongerekke)

rekkefølge()



print()
haakon.skriv()
olav.skriv()
harald.skriv()

haakon.etterfølger(olav)
olav.etterfølger(harald)

haakon.nesteMonark.skriv()







