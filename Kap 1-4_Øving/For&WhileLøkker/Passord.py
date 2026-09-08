riktigpassord: str = "RiktigPassord1"
passord = str(input("Skriv inn passordet! \n" ))

while passord != riktigpassord:
    passord = str(input("Skriv inn passordet! \n"))

    if passord == riktigpassord:
        print("Velkommen!")
        break