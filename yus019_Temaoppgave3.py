#Oppgave 1

#x!=7 and y<=50
#x>7 or 50<y) and (x>y or y<100)


x = 9
y = 66

#A
print(x!=7 and y<=50)
print(x>7 or 50<y) and (x>y or y<100)

#B
print(6 <= x <= 8 and y < 50 == 50)
print(x != 7 <= 8) and (y < x or y <= 99)



#Oppgave 2

x = int(input("Hvor gammel er du? "))
y = int(input("Hvor mange år har du bodd i Tulleby? "))

if x >= 30 and y >= 9:
    print("Du kan bli ordfører eller sitte i styret!")
elif x >= 30 and y >= 5 < 9:
    print("Du kan sitte i styret, men du må bo i Tulleby i", 9 - y, "år til før du kan bli ordfører!")
elif x >= 25 and y >= 9:
    print("Du kan sitte i styret, men du må bli", 30 - x, "år eldre før du kan bli ordøfer")
elif x >= 25 and y >= 5 < 9:
    print("Du kan sitte i styret, men du må bli", 30 - x, "år eldre, og bo i byen", 9 - y, "år til før du kan bli ordfører")
elif x < 25 and y < 5:
    print("Du må bli", 25 - x, "år eldre og bo i byen", 5 - y, "år til før du kan sitte i styret")
    print("Du må bli", 30 - x, "år eldre og bo i byen", 9 - y, "år til før du kan bli ordfører")
elif x > 0 < 25 and y >= 9:
    print("Du må bli", 25 - x, "år eldre før du kan sitte i styret")
    print("Du må bli", 30 - x, "år eldre før du kan bli ordfører")
elif x > 30 and y < 9:
    print("Du må bo i Tulleby i",5 - y, "år til for å sitte i styret og", 9 - y, "år til før du kan bli ordfører")


#Oppgave 3

x = int(input("Tall: "))
if x > 5:
    if x < 10:
        print("6 , 7, 8 eller 9")
        if x >= 10:
            print("Minst 10")
if x <= 5:
    print("Maks 5")

#   Skriv om programmet uten nøstede if-setninger

x = int(input("Tall: "))

if 5 < x < 10:
    print("6, 7, 8 eller 9")
elif x >= 10:
    print("Minst 10")
elif x <=5:
    print("Maks 5")
