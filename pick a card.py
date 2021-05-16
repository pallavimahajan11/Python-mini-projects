import random
cards=['Diamonds','Spades','Hearts','clubs']
ranks=[2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]

def pick_card():
    card= random.choices(cards)
    rank=random.choices(ranks)
    print(f"The {rank} of {card}")
pick_card()


