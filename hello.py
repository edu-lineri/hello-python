import random as rand
slumptal=rand.randint(1,10)
namn=(input("Hej vad heter du?"))
print(f"Hej {namn} och välkommen till spelet!")

#Spelet
Gissning=int(input("Gissa på ett tal mellan 1-10"))
while not Gissning==slumptal:
    print(f"Tyvär du gissade fel, gissa igen")
    Gissning=int(input("Gissa på ett tal mellan 1-10"))
else:
    print("Grattis du gissade rätt")


