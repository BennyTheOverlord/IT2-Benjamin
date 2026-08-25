"""
navn = input("Hva er navnet ditt?")

navn.capitalize()

alder = int(input("Hvor gammel er du?"))

tekst = f"Neste år er du {alder + 1} år {navn}"

print(tekst)
"""

"""
Tall1 = float(input("Velg et tall"))

Tall2 = float(input("Velg et til tall"))

sum = Tall1 + Tall2

differanse = Tall1 - Tall2

Produktet = Tall1 * Tall2

Utregning = f"Sum = {sum}, differanse = {differanse}, produktet = {Produktet}."

print(Utregning)
"""
"""
Lengde = float(input("Velg en lengde"))

Bredde = float(input("Velg en bredde"))

areal = Lengde * Bredde

omkrets = Lengde + Lengde + Bredde + Bredde

print(f"areal er {areal:.2f}, omkrets er {omkrets:.2f}")
"""
"""
dag = 25

måned = 8

år = 2026

print(dag, måned, år, sep="-", end="")
print(" Er datoen i dag")
"""
"""
a, b = 1, 2

print (a, b)

a, b = b, a

print (a, b)
"""
"""
a = 3
b = 7

print(f"a = {a}, b = {b}")

a, b = b, a

print(f"a = {a}, b = {b}")
"""
"""
høyde = 180
vekt = 75

høydeM = høyde / 100

BMI = (vekt/(høydeM**høydeM))

print(f"{BMI:.2f}")
"""
"""
MVA_SATS = 0.25

pris = int(input("Velg en pris"))

pris_medMVA = pris + (pris*MVA_SATS)

print(pris_medMVA)
"""

from math import pi

def regnUtSirkelOmkrets(diameter):
    # diameter = 10
    omkrets = pi * diameter
    print(omkrets)

regnUtSirkelOmkrets(10)
