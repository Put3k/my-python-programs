from deck import Deck
from hand import Hand


class Game:
    MINIMUM_BET = 1

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.bet = None
        self.deck = Deck()
        self.deck.create_deck()

    def reset(self):
        self.player.hand.clear()
        self.dealer.hand.clear()
        self.deck.shuffle()
        self.bet = None
        self.lose = False
        self.dealer.hand.hide = True

    def hit(self):
        print(f"You are dealt: {', '.join(str(x) for x in self.player.hand.add_to_hand(self.deck.deal(1)))}")
        print(f"You now have: {', '.join(str(x) for x in self.player.hand.hand)}")
        print(f"Value of your hand is: {self.player.get_hand_value()}")

    def stay(self):
        pass

    def player_hit_or_stay(self):
        while True:
            result = input("Would you like to hit or stay? ")
            if result.lower() == "hit":
                self.hit()

                if self.player.get_hand_value() == 21:
                    self.dealer_hit_or_stay()
                    print(f"Blackjack! You win ${self.bet}")
                    break

                if self.player.get_hand_value() > 21:
                    print(f"Your hand value is over 21 and you lose ${self.bet}")
                    self.player.balance -= self.bet
                    self.lose = True
                    break

                else:
                    self.player_hit_or_stay()
                    break

            elif result.lower() == "stay":
                self.dealer_hit_or_stay()
                break

            else:
                print("That is not a valid option.")

    def dealer_hit_or_stay(self):
        self.dealer.hand.hide = False
        print("The dealer has: " + self.dealer.get_str_hand())

        if self.dealer.get_hand_value() > 21:
            print(f"The dealer busts, You win ${self.bet}")

        if self.dealer.get_hand_value() == 21:
            if self.player.get_hand_value() == 21:
                print("You tie. Your bet has been returned.")
            else:
                print(f"The dealer wins, you lose ${self.bet}")
                self.player.balance -= self.bet

        if self.dealer.get_hand_value() >= 17:
            print("The dealer stays.")

            if self.dealer.get_hand_value() == self.player.get_hand_value():
                print("You tie. Your bet has been returned")

            if self.dealer.get_hand_value() > self.player.get_hand_value():
                print(f"The dealer wins, you lose ${self.bet}")
                self.player.balance -= self.bet
                
            else:
                print(f"You win ${self.bet}!")
                self.player.balance += self.bet

        if self.dealer.get_hand_value() <= 16:
            print(f"The dealer hits and is dealt: {', '.join(str(x) for x in self.dealer.hand.add_to_hand(self.deck.deal(1)))}")
            print(f"The dealer has: {', '.join(str(x) for x in self.dealer.hand.hand)}")
            self.dealer_hit_or_stay()

    def start_game(self):
        while True:
            if self.player.balance == 0:
                print()
                print("You've ran out of money. Please restart this program to try again. Goodbye.")
                break
            self.reset()
            print()
            player_input = input(f"You are starting with ${self.player.balance}. Would you like to play a hand? ")
            if player_input.lower() != "yes":
                break
            else:
                while True:
                    self.bet = float(input("Place your bet: "))

                    if self.bet > float(self.player.balance):
                        print("You don't have enough money to make this bet! Try again.")
                        print()
                        continue
                    if self.bet >= Game.MINIMUM_BET:
                        break
                    else:
                        print("The minimum bet is $1.")
                        print()
                        continue
                    
            print(f"You are dealt: {', '.join(str(x) for x in self.player.hand.add_to_hand(self.deck.deal(2)))}")
            print(f"The dealer is dealt {', '.join(str(x) for x in self.dealer.hand.add_to_hand(self.deck.deal(2)))}")

            if self.player.get_hand_value() == 21 and self.dealer.get_hand_value() == 21:
                print("You tie. Your bet has been returned.")
                continue
            if self.player.get_hand_value() == 21:
                print(f"Blackjack! You win ${self.bet}")
                #set status to win
                continue
            if self.lose == True:
                self.player.balance -= self.bet
                continue
            else:
                self.player_hit_or_stay()