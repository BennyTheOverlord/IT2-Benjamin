ordliste = [
    "Banan",
    "Skolefri",
    "Koding",
    "Banan",
    "Banan"
]

antallBokstaver = {}

for ord in ordliste:
    print(ord)
    for bokstav in ord:
        #print(bokstav)
        antallBokstaver[bokstav] = antallBokstaver.get(bokstav, 0) + 1

print(antallBokstaver)