import random
# print(sorted([random.choice([(m,i+1) for m in ('S','H','C','D') for i in range(13)]) for i in range(0,5)],key=lambda x: x[1]))
cards = [(m,i+1) for m in ('S','H','C','D') for i in range(13)]
print(sorted([random.choice(cards) for i in range(0,5)],key=lambda x: x[1]))