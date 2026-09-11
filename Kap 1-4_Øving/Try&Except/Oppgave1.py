gyldig = False
brukerTall = None

while not gyldig:
    brukerTall = (input("Velg et heltall! \n"))

    try:
        brukerTall = int(brukerTall)
        gyldig = True
    
    except ValueError:
        print("Tallet må være et heltall")

print(f"Du valgte tallet {brukerTall}!")
