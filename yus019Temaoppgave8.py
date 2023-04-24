print("\nOppgave 1A\n")
#Oppgave 1A

eksamen = {
 'INFO100': 'C', 'INFO104': 'B', 'INFO116': 'E',
 'INFO180': 'A', 'INFO201': 'F', 'INFO280': 'C',
 'GEO101': 'D', 'GEO110': 'B', 'ADM101': 'A',
 'ECON100': 'B', 'ECON201': 'C', 'GEO210': 'C',
 'FAIL101': 'F'
}


values = eksamen.values()

def karFreq():
    tellerA = 0
    tellerB = 0
    tellerC = 0
    tellerD = 0
    tellerE = 0
    tellerF = 0
    for i in values:
        if i == "A":
            tellerA += 1
        if i == "B":
            tellerB += 1
        if i == "C":
            tellerC += 1
        if i == "D":
            tellerD += 1
        if i == "E":
            tellerE += 1
        if i == "F":
            tellerF += 1
    print("A :",tellerA, ",  B :",tellerB, ",  C :",tellerC, ",  D :",tellerD, ",  E :",tellerE, ",  F :",tellerF)

karFreq()



#Oppgave 1B

def histogram():
    tellerA = 0
    tellerB = 0
    tellerC = 0
    tellerD = 0
    tellerE = 0
    tellerF = 0
    for i in values:
        if i == "A":
            tellerA += 1
        if i == "B":
            tellerB += 1
        if i == "C":
            tellerC += 1
        if i == "D":
            tellerD += 1
        if i == "E":
            tellerE += 1
        if i == "F":
            tellerF += 1
    liste = [tellerA, tellerB, tellerC, tellerD, tellerE, tellerF]
    for x in liste:
        print("*"*x)
    
print("\n\nOppgave 1B\n")
histogram()


print("\n\nOppgave 2A\n")

engelske_siffer = {
 0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
}


inv = [value for (value) in sorted(engelske_siffer.items())]

print(inv)


print("\n\nOppgave 2B\n")


engelske_siffer2 = {y:x for x, y in engelske_siffer.items()}
print(engelske_siffer2)


print("\n\nOppgave 2C\n")



engelskeSiffer = {
 9: 'nine', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 0: 'zero'
}
def invsort():
    bytt = {value: key for key, value in engelskeSiffer.items()}
    print(bytt)
    a = {key:value for key, value in sorted(bytt.items(),key = lambda x: x[1])} 
    print(a)
invsort()