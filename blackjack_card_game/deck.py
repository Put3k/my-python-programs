import random
from card import Card


class Deck:
    def __init__(self):
        self.deck = []

    def create_deck(self):
        for suit in Card.SUIT_SYMBOLS:
            for value in Card.VALUE_NAMES:
                self.deck.append(Card(suit, value)) #First element in the list is the top card
        random.shuffle(self.deck)

    def shuffle(self):
        self.deck.clear()
        Deck.create_deck(self)
        random.shuffle(self.deck)

    def deal(self, num_cards):
        deal_list = []
        for card in range(num_cards):
            deal_list.append(self.deck.pop(0))

        return deal_list