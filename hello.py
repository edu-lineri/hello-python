import random as rand

hemligt_nummer=rand.randint(1000,9999)
print(hemligt_nummer)
hemligt_str=str(hemligt_nummer)
antal=5
print("Tjena, nu ska du spela Mastermind, detta spel går ut på att gissa nummer och efter en gissning kommer två symboler visas upp. \nFöljande symbol visas om du har rätt plats och rätt siffra 😇\n Det andra tecknet du kan få är 🫠, den visas om du har fått rätt nummer men på fel plats.")
while antal>0:
    try:
        gissning=int(input("Gissa på ett tal"))
    except ValueError or len(gissning)>4:
        print("Fel! Du måste skriva en siffra, försök igen")
    antal-=1
    resultat=""
    gissning_str=str(gissning)

    for i in range(4):
        if gissning_str[i] == hemligt_str[i]:
            resultat += "😇"
        elif gissning_str[i] in hemligt_str:
            resultat += "🫠"
    print(resultat)
    if gissning==hemligt_nummer:
        print("Tack för att du spelat, du fick rätt svar")

print(f"Du fick tyvär fel svar efter 5 omgångar och misslyckade att klara ut spelet, det rätta ordet var {hemligt_nummer}")