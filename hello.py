print("Vilken huvudstad har Norge?")
print("1. Oslo")
print("2. Stockholm")
print("3. Köpenhamn")
svar1=1
svar2=2
poäng=0
gissning=int(input("Gissa på vilken av dessa svarsalternativ som är korrekt"))
if svar1==gissning:
    print("Du svarade rätt!")
    poäng+=1
else:
    print("Du fick fel svar")

print("Vilket år började andra världskriget")
print("1. 1914")
print("2. 1939")
print("3. 1945")
gissning=int(input("Gissa på vilken av dessa svarsalternativ som är korrekt"))
if svar2==gissning:
    print("Du svarade rätt!")
    poäng+=1
else:
    print("Du fick fel svar")

print(f"Du fick {poäng} av 2 rätt")