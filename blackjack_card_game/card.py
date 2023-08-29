class Card:
    SUIT_SYMBOLS = {
        0: u"\u2666",  # diamonds
        1: u"\u2665",  # hearts
        2: u"\u2663",  # clubs
        3: u"\u2660"  # spades
    }

    VALUE_NAMES = {
        1: "A",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "T",
        11: "J",
        12: "Q",
        13: "K"
    }

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.card_code = str(suit)+str(value) #card code "---" 3 digit, first -> suit, else -> value

    def __str__(self):
        return f"{Card.VALUE_NAMES[self.value]}{Card.SUIT_SYMBOLS[self.suit]}"
    
    def __repr__(self):
        return f"{Card.VALUE_NAMES[self.value]}{Card.SUIT_SYMBOLS[self.suit]}"

    def __add__(self, other):
        if isinstance(other, Card):
            print("card")
            return self.value + other.value
        if isinstance(other, int):
            return self.value + other

        return False

    def __radd__(self, other):
        if isinstance(other, Card):
            return other.value + self.value
        if isinstance(other, int):
            return other + self.value
            
        return False

    def __eq__(self, other):
        return self.value == other