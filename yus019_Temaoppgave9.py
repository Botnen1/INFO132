print("\nINFO132\nObligatorisk Temainnlevering 9")
#Oppgave 1
print("\nOppgave 1\n")

""" Skriv en applikasjon (Et brukeroriert program) med et grafisk brukergrensesnitt
("Graphical User Interface" GUI). Brukergrensesnittet skal ha en knapp ("Button") merket "Farvell".
Når knappen trykkes skal hovedvinduet lukkes. """


import PySimpleGUI as ting

def oppg1(): 
    ting.Window(title="Applikasjon", layout=[[ting.Button("Farvell")]], margins=(200, 200)).read()

oppg1()
#må kjøres hver for seg for at nummer 1 skal fungere


#Oppgave 2
print("\nOppgave 2\n")
""" skriv en applikasjon med et grafisk brukergrensesnitt (GUI) som har en enkelt kanpp. 
Til å begyne med er knappen merket med 0, men hver gang knappen trykkes skal verdien økes med 1. """

from tkinter import *

count = 0
vindu = Tk()

def addnummer():
    global count
    global antallKlikk

    count += 1

    antallKlikk.pack_forget()

    antallKlikk = Label(vindu, text=count)
    antallKlikk.pack()



button = Button(vindu, text="klikk her!", command=addnummer)
button.pack()

antallKlikk = Label(vindu, text=count)
antallKlikk.pack()

vindu.mainloop()

