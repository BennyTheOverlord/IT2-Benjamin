gyldig = False
deltTall = None

while not gyldig:

    brukerTall1 = float(input("Velg et tall! \n"))
    brukerTall2 = float(input("Velg et annet tall! \n"))
    deltTall = brukerTall1 / brukerTall2

    try:
        brukerTall1 = float(brukerTall1)
        brukerTall2 = float(brukerTall2)
        gyldig = True

    except ValueError:
        print ("Verdiene må være et tall!")

    except ZeroDivisionError:
        print("Det er matematisk sett umulig å dele på 0, du må dermed velge et annet tall!")

print(f"Tallene dine delt på hverandre er = {deltTall}!")