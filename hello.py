import random as rand
slumptal=rand.randint(1,10)
namn=(input("Hej vad heter du?"))
print(f"Hej {namn} och välkommen till spelet!")

#Spelet
Gissning=int(input("Gissa på ett tal mellan 1-10"))
if Gissning==slumptal:
    print("Grattis du gissade rätt!!")
else:
    print(f"Tyvär du gissade fel, det rätta svaret var {slumptal}")