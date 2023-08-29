from hand import Hand
class Player:
    def __init__(self, balance):
        self.balance = balance
        self.hand = Hand()

    def get_str_hand(self):
        # return self.hand.hand
        return f"{', '.join(str(x) for x in self.hand.hand)}"

    def get_hand_value(self): #returning player hand value
        return self.hand.get_value()