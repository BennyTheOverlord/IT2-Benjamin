"""
def Førerkort () -> None:
    bruker_alder = int(input("Hvor gammel er du?"))

    if bruker_alder < 16:
        print("Du kan ikke ta noen form for førerkort!")

    elif 16 <= bruker_alder < 18:
        print("Du kan ta mopedlappen!")

    elif 18 <= bruker_alder < 21:
        print("Du kan ta bil-lappen!")

    elif 21 <= bruker_alder < 75:
        print("Du kan ta buss-lappen!")
    
    else:
        print("Du burde ikke kjøre bil")

Førerkort()
"""

import random

vant: dict[str, str] = {
    "stein": "saks",
    "saks": "papir",
    "papir": "stein",

}

alternativ: list[str] = ["stein", "saks", "papir"]

poeng_spiller: int = 0
poeng_datamaskin: int = 0
uavgjort: int = 0

while poeng_spiller < 3 and poeng_datamaskin < 3:
    bruker_valg = input("Velg stein saks eller papir: ").lower()
    datamaskin_valg = random.choice(alternativ)

    if bruker_valg not in alternativ:
        print("Ugyldig svar")
        break

    if vant[bruker_valg] == datamaskin_valg:
        poeng_spiller = (poeng_spiller + 1)
        print("Du vant!")

    elif vant[datamaskin_valg] == bruker_valg:
        datamaskin_valg = (poeng_datamaskin + 1)
        print("Du tapte!")

    else: 
        uavgjort = (uavgjort + 1)
        print("Uavgjort!")


    """if bruker_valg == "stein" and datamaskin_valg == "saks":
        print("Du vant!")
        poeng_spiller = poeng_spiller + 1"""
            