#Oppgave 1
print("\nOppgave1\n")

with open("/Users/hanschristianbotnen/Documents/Skole/KODE/PYTHON/Temaoppgave7/telefon.txt",'a',encoding = 'utf-8') as f:
    inputnavnognummer = str(input("Navn og Nummer: "))
    f.write(inputnavnognummer)
    f.write("\n")
    



#Oppgave 2
print("\nOppgave2\n")

with open("/Users/hanschristianbotnen/Documents/Skole/KODE/PYTHON/Temaoppgave7/telefon.txt",'r',encoding = 'utf-8') as f: #lese
    lines = f.readlines()
kontaktNavn = input("Hvilken kontakt ønsker du å endre?: ")
count = 0
for x in lines:
    if x.startswith(kontaktNavn):
        y = x[len(kontaktNavn)+1:-1]
        print(y)
        endreKontaktensNummer = input("Hva er det nye nummeret til denne kontakten?: ")
        lines[count] = x.replace(y, endreKontaktensNummer)
        print(f"Kontaktens nummer ble endret fra", y, "til", endreKontaktensNummer)
        break
    count += 1
with open("/Users/hanschristianbotnen/Documents/Skole/KODE/PYTHON/Temaoppgave7/telefon.txt",'w',encoding = 'utf-8') as f: 
    f.writelines(lines)



#Oppgave 3
print("\nOppgave3\n")


def fjernVokaler(file):
    with open(file,'r',encoding = 'UTF-8') as f:
        leseFil = f.read()
        vokaler = ["a", "e", "o", "i", "u", "ø", "å", "æ", "y", "A", "E", "O", "I", "U", "Ø", "Æ", "Å", "Y"]
        for x in leseFil:
            if x in vokaler:
                leseFil = leseFil.replace(x, " ")
        print(leseFil)

    with open("endret.txt", 'w', encoding = 'UTF-8') as wf:
        wf.write(leseFil)

fjernVokaler("/Users/hanschristianbotnen/Documents/Skole/KODE/PYTHON/Temaoppgave7/tresmaakinersere.txt")