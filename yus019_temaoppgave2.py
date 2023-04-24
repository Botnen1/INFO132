    #Oppgave1

import math
r = float(input("Radius " ))
areal = "{:.3f}".format(math.pi * r ** 2)
print(areal)
print("\nArealet av en sirkel med radius", r, "er", areal, "\n\n")



    #Oppgave2

setning = input("Skriv en setning: ")
antall = len(setning)
gjett = input("Hvor mange bokstaver tror du det var i den setnignen?: ")
if int(gjett) == antall:
    print("\nTrue")
else:
    print("\nFalse")
    print("Riktig antall bokstaver var:", antall, "\n\n")



    # Oppgave3

import random

x = input("Gi meg et tall: ")
y = random.randint(0, 9)
variabel = str(x) + str(y)
utregning = int(variabel) / int(x)
print(variabel, "/", str(x), "=", utregning)






