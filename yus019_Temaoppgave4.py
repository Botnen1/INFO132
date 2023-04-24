print("Oppgave1\n")

def siste(sekvens):
    siste = sekvens [-1]
    return print(siste)

siste("python")
siste([1, 2, 3, 4, 5])
siste(range(90, 100))

print("\n\nOppgave2\n")
def skriv_sekvens(sekvens):
    for x in sekvens:
        print(x, sep=" ", end=" ")
    print()

skriv_sekvens("PYTHON")
skriv_sekvens([1,2,3,4,5])
skriv_sekvens(range(90,100))

print("\n\nOppgave3\n")

start_beløp = float(input("Startbeløp: "))
rente = float(input("rente: "))
ønsket_beløp = float(input("ønsket beløp: "))
år = 1
penger = start_beløp

while penger < ønsket_beløp:
    penger = penger * rente
    print("år",år, " : ", round(penger, 2))
    år += 1



print("\n\nOppgave4\n")


def lillegangetabellen():
    for x in range(1, 11):
        print("\n", end="")
        for y in range(1, 11):
            gangetabell = x * y
            if gangetabell < 10:
                gangetabell = " " + str(gangetabell)
            print(gangetabell, sep="", end=" ")


lillegangetabellen()