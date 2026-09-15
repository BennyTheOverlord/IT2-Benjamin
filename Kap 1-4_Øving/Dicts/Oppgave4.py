fag_karakter = {
    "Matematikk": 6,
    "Norsk": 6,
    "It": 6,
    "Spansk": 6
}

if "Engelsk" in fag_karakter:
    print("Engelsk er i systemet")
else:
    print("Engelsk er ikke i systemet")

engelsk_karakter = fag_karakter.get("Engelsk", 0)
print(f"Din karakter i engelsk er: {engelsk_karakter}")