from hand import Hand

class Dealer:
    def __init__(self):
        self.hand = Hand()

    def get_str_hand(self):
        # return self.hand.hand
        return f"{', '.join(str(x) for x in self.hand.hand)}"

    def get_hand_value(self): #returning dealer hand value
        return self.hand.get_value()