#Oppgave 1
print("\nOppgave1\n")
def antallVokaler(tekst):
    vokal = ["a", "e", "i", "o", "u", "y", "æ", "ø", "å", "A", "E", "I", "O", "U", "Y", "Æ", "Ø", "Å"]
    antall = 0
    for x in tekst:
        if x in vokal:
            antall += 1
    return antall


print(antallVokaler("Tre små kinesere på Høybro plass"))
    


#Oppgave2
print("\nOppgave2\n")
TV = '''\
Tulleveien Velforening
leder: Kari
kasserer: Ole
IT-ansvarlig: Liv
parkeringsansvarlig: Kari
arrangementsansvarlig: Liv
hagekonsulent: Kari
brannansvarlig: Kari
'''
def verv(navn):
    list = []
    linjer = TV.split("\n")
    for x in linjer:
        posisjon = x.find(":")
        if navn in x[posisjon:]:
            list.append(x[:posisjon])       
    return list


print(verv("Kari"))