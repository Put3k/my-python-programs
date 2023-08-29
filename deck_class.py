import random

class Deck:
    
    valid_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    valid_suits = ["H", "D", "C", "S"]
    valid_cards = []
    for suit in valid_suits:
        for value in valid_values:
            valid_cards.append(f"{value}{suit}")

    def __init__(self):
        self.cards = Deck.valid_cards.copy()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n):
        self.n = n
        deal = []
        counter = 0

        if self.n > len(self.cards):
            deal = self.cards
            return deal

        for card in range(self.n):
            if counter < self.n:
                deal.append(self.cards.pop())
                counter += 1
            else:
                break

        return deal

    def sort_by_suit(self):
        def sortBySuits(card):
            if "H" in card:
                return 1
            if "D" in card:
                return 2
            if "C" in card:
                return 3
            if "S" in card:
                return 4
        self.cards.sort(key=sortBySuits)

    def contains(self, card):
        if card in self.cards:
            return True
        else:
            return False

    def copy(self):
        new_deck = Deck()
        new_deck.cards = self.cards.copy()
        return new_deck

    def get_cards(self):
        cards = self.cards.copy()
        return cards

    def __len__(self):
        return len(self.cards)

deck1 = Deck()
print(len(deck1))
for i in range(10):
    cards = deck1.deal(5)
    print (len(deck1), cards)