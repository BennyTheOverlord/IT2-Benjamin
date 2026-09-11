gyldig = False
brukerTall = None

while not gyldig:
    brukerTall = input("Velg et heltall fra og med 0 - 100! \n")

    try:
        brukerTall = int(brukerTall)

    except ValueError:
        print("Tallet må være et heltall!")
        continue

    if (brukerTall > 100) or (brukerTall < 0):
        print("Tallet må være mellom 0 - 100!")
    else:
          gyldig = True

print(f"Du valgte tallet {brukerTall}!")