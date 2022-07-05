from random import choice

def create_deck(suits, cards):
    deck = [(c, s) for c in cards for s in suits]
    return deck

def is_poker(hand):
    cards = []
    for i in hand:
        cards.append(i[0])
    print(cards)

    for i in cards:
        if cards.count(i) >= 4:
            return True
    return False

deck = create_deck(['♠', '♥', '♦', '♣'], ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'])
cheating_deck = create_deck(['♠', '♥', '♦', '♣'], ['A', 'K'])

hand = []
for i in range(5):
    card = choice(cheating_deck)
    hand.append(card)
    cheating_deck.remove(card)
print(hand)

if is_poker(hand):
    print("Poker!")
else:
    print("Better luck next time")
