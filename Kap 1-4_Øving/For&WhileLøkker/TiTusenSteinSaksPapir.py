import random

valgAlternativer = ["Stein", "Saks", "Papir"]

stein = 0
saks = 0
papir = 0

for i in range (1, 10_000 + 1, 1):
    botValg = str(valgAlternativer[random.randint(0, 2)])

    if botValg == "Stein":
        stein += 1

    elif botValg == "Saks":
        saks += 1     

    else: papir += 1

print(f"Datamaskinen fikk {stein} stein, {saks} saks og {papir} papir")
