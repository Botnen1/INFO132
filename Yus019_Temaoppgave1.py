#  1. Lag minst to ulike programmer som skriver navnet ditt på skjermen, med for-(mellom-) og etternavn på hver sin linje
print()
print(" oppgave 1. Lag minst to ulike programmer som skriver navnet ditt på skjermen, med for-(mellom-) og etternavn på hver sin linje")
print ()

print("Hans Christian\nOlebakken\nBotnen")

print()
print()

h = "Hans"
c = "Christian"
o = "Olebakken"
b = "Botnen"

print(h, c)
print(o)
print(b)

print()

fornavn = input("Skriv fornavnet ditt her: " )
mellomnavn = input("Skriv mellomnavnet ditt her: " )
etternavn = input("Skriv etternavnet ditt her: " )
print()
print(fornavn)
print(mellomnavn)
print(etternavn)

print()
print()
#  2. Lag et program som skriver fornavnet ditt på skjermen på denne måten:
print(" oppgave 2 Lag et program som skriver fornavnet ditt på skjermen på denne måten")
print()

en = ("*       *      *      *       *    * * * *")
to = ("*       *    *   *    * *     *  *        ")
tre = ("* * * * *   *  *  *   *   *   *    * * * ")
fire = ("*       *  *       *  *     * *          *")
fem = ("*       *  *       *  *       *   * * * *")

print(en)
print(to)
print(tre)
print(fire)
print(fem)

# 3

print()
print( "oppgave 3 - Valuttakalkulator")
print()

#   a) Lag et program som regner om et beløp fra norske kroner til EURO og Dollar.

kroner = float(input("Hvor mange kroner har du?: "))

print()
#  fant at dollarkurs var 0.1181
#  fant eurokurs på 0.1011

Dollar = kroner * 0.1181
Euro = kroner * 0.1011

verdi_dollar = float(Dollar)
formatert_verdi_dollar = "{:.2f}".format(verdi_dollar)
float_value_dollar = float(formatert_verdi_dollar)

verdi_euro = float(Euro)
formatert_verdi_euro = "{:.2f}".format(verdi_euro)
float_value_euro = float(formatert_verdi_euro)

print("a")
print(kroner, "kroner tilsvarer", formatert_verdi_euro, "euro og", formatert_verdi_dollar, "dollar")

print()

#   b) Spesialtegnene € og $ kan skrives ved hjelp av tegnkoder,  Bruk disse til å lage utskrift som dette.
print("b")
print(kroner, "kroner tilsvarer", formatert_verdi_euro,(u"\N{euro sign}"), "og", formatert_verdi_dollar,(u"\N{dollar sign}"))


