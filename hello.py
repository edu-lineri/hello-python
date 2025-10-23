print("Vilken huvudstad har Sverige?")
print("1. Oslo")
print("2. Stockholm")
print("3. Köpenhamn")
svar=2
gissning=int(input("Gissa på vilken av dessa svarsalternativ som är korrekt"))
if svar==gissning:
    print("Du svarade rätt!")
else:
    print("Du fick fel svar")