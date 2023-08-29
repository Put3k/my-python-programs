from deck import Deck

class Hand:
    def __init__(self):
        self.hand = []
        self.hide = False

    def get_value(self): #returns total value of cards in hand
        value = 0
        aces = []
        for i in self.hand:
            if i.value == 1:
                aces.append(i)
            elif i.value > 10:
                value += 10
            else:
                value += i.value

        if len(aces) != 0:
            for i in aces:
                if value <= 10:
                    value += 11
                else:
                    value += 1

        return value
        
    def add_to_hand(self, cards): #adds cards to hand
        dealt_cards = []
        for card in cards:
            self.hand.append(card)
            dealt_cards.append(card)
        if self.hide:
            dealt_cards[1] = "Unknown"
        self.hide = False
        return dealt_cards

    def clear(self):
        self.hand.clear()

    def __str__(self):
        return f"{self.hand}"
