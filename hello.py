import random as rand

hemligt_str = "".join(str(rand.randint(0, 9)) for _ in range(4))
antal=10
print("Tjena, nu ska du spela Mastermind, detta spel går ut på att gissa nummer och efter en gissning kommer två symboler visas upp. \nFöljande symbol visas om du har rätt plats och rätt siffra 😇\n Det andra tecknet du kan få är 🫠, den visas om du har fått rätt nummer men på fel plats.")
while antal>0:
    try:
        gissning = input("Gissa på ett tal")
        gissning_längd=len(gissning)
        if gissning_längd!=4:
            print("Du måste skriva 4 siffror, inte mer och inte mindre")
            continue
        
    except ValueError:
        print("Fel! Du måste skriva en siffra, försök igen")
        continue
    antal-=1
    print(f"Du har {antal} gissningar kvar")
    resultat=""

    for i in range(4):
        if gissning[i] == hemligt_str[i]:
            resultat += "😇"
        elif gissning[i] in hemligt_str:
            resultat += "🫠"
    print(resultat)
    if gissning==hemligt_str:
        print("Tack för att du spelat, du fick rätt svar")

print(f"Du fick tyvärr fel svar efter 10 omgångar och misslyckade att klara ut spelet, det rätta ordet var {hemligt_nummer}")
