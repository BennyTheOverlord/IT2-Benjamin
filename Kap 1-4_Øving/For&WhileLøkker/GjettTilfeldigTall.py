import random 

def startSpill():
    tilfeldigTall = int(random.randint(1, 100))
    antallForsøk = 0

    brukerValg = int(input("Prøv å gjett hvilket tall jeg tenker på. Hint: Tallet er mellom 1 - 100 \n"))

    while brukerValg != tilfeldigTall or brukerValg == tilfeldigTall:
        antallForsøk = (antallForsøk + 1)

        if brukerValg > tilfeldigTall:
            print("For høyt!")
            brukerValg = int(input("Feil tall. Prøv igjen! \n"))
            

        elif brukerValg < tilfeldigTall:
             print("For lavt!")
             brukerValg = int(input("Feil tall. Prøv igjen! \n"))
           
        else:
            print(f"Du gjettet riktig, tallet var {tilfeldigTall}. Du brukte {antallForsøk} forsøk")
            break

startSpill()
