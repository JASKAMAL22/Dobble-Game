import string
import random

symbols=[]

symbols=list(string.ascii_letters)

card1 = [0]*5
card2 = [0]*5

pos1=random.randint(0, 4)
pos2=random.randint(0, 4)
print(pos1)
print(pos2)

same_sym = random.choice(symbols)
symbols.remove(same_sym)
if (pos1 == pos2):
    card2[pos1]=same_sym
    card1[pos2]=same_sym
else:
    card1[pos1]=same_sym
    card2[pos2]=same_sym
    card1[pos2]=random.choice(symbols)
    symbols.remove(card1[pos2])

    card2[pos1]=random.choice(symbols)
    symbols.remove(card2[pos1])

i=0
while(i<5):
    if (i!=pos1 and i!=pos2):
        alph_1 = random.choice(symbols)
        symbols.remove(alph_1)
        alph_2 = random.choice(symbols)
        symbols.remove(alph_2)
        card1[i] = alph_1
        card2[i] = alph_2
    i+=1
print(card1)
print(card2)

ch = input("Spot Similar Symbol: ")
if  ch==same_sym:
    print("Right! Well Done...")
else:
    print("Better luck next time")
