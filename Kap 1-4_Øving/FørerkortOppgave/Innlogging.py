"""
innlogget = False

Registrert_brukernavn = "Bruker01"
Registrert_passord = "Passord01"

while not innlogget:
    brukernavn: str = input("Velg et brukernavn! \n")
    
    if brukernavn != Registrert_brukernavn:
        print("Dette brukernavnet er ikke tilknyttet en registrert bruker!")

    passord: str = input("Velg et passord!")

    if passord != Registrert_passord:
        print("Dette passordet er ikke tilknyttet en bruker i vårt system")


    if brukernavn == Registrert_brukernavn and passord == Registrert_passord:
        innlogget = True
        if innlogget == True:
            print(f"Velkommen tilbake {Registrert_brukernavn}")


print("\"Denne meldingen skrives med hermetegn\"")

"""

import bcrypt

passord = "passord01"

passord = passord.encode("utf-8")

salt = bcrypt.gensalt(rounds = 18)

hashed_passord = bcrypt.hashpw(passord, salt)

print(hashed_passord)


