# -----------------------------------------------------
# Simple Blackjack game (blackjack.py file)
# By Andres Barrera (agb0174)
# -----------------------------------------------------
import random
import cards


class Player:
    def __init__(self, name="None", bank=0, has_hand=False, hand_value=0, dealt_cards=None):  # initializing player
        self.name = name
        self.bank = bank
        self.has_hand = has_hand
        self.hand_value = hand_value
        if dealt_cards is None:
            self.dealt_cards = []
        else:
            self.dealt_cards = dealt_cards

    def info(self):  # function used to return info about the player [name and current bank amount]
        print(f"\t----Player name: {self.name}\n\t----Current amount in bank: ${self.bank}")

    def hit(self, deck):  # function to allow player to stay or
        card = cards.Card(deck.deal_card())
        self.dealt_cards.append(card.name)
        card.print_up()
        self.hand_value += card.value
        print(f"--Updated hand value is {self.hand_value}")
        return card

    def get_hand(self, deck):  # function to give player hand, keep giving cards until player stays or busts
        card1 = cards.Card(deck.deal_card())
        card2 = cards.Card(deck.deal_card())
        self.dealt_cards.append(card1.name)
        self.dealt_cards.append(card2.name)
        print(f"Randomly dealt hand to {self.name}: ")
        card1.print_up()
        card2.print_up()
        self.hand_value = card1.value + card2.value
        print(f"--Hand value is currently {self.hand_value}")
        if self.hand_value > 21:  # user busted, end round
            print(f"Tough luck. {self.name} was dealt a bust. Game over.")
        elif self.hand_value == 21:  # user was dealt a blackjack, end round
            print(f"Wow! {self.name} has been dealt a blackjack. Game over.")
        else:
            self.has_hand = True
        print("....Dealer's turn to get cards....")
        return card1, card2


class Dealer(Player):  # TODO: fix overwriting dealer name
    def ___init__(self, name, bank, has_hand, hand_value, dealt_cards):  # initializing dealer instance, random name from list
        super().__init__(name, bank, has_hand, hand_value, dealt_cards)
        name_as_list = ["John", "Kevin", "Bob", "Michael", "Karen", "Tiffany", "Sarah", "Victoria"]
        self.name = random.choice(name_as_list)

    def get_bet(self, player):
        while True:
            try:  # try/except to handle ValueError that crashes program if user enters anything but an integer
                bet = int(input(f"{self.name}: \"Please enter your bet amount now\" >>>>>> $"))
                if bet > player.bank:
                    print(f"\n{self.name}: \"Uh oh. Looks like you don\'t have enough in the bank for that bet!\""
                          f"\n\t----Please enter a bet less than your current bank. "
                          f"\nHere's your info:")
                    player.info()
                elif bet <= 0:
                    print(f"\n{self.name}: \"You have to bet something! No free hands here, sorry.\""
                          f"\n\t----Please enter a bet larger than $0")
                else:
                    print(f"\n{self.name}: \"Great! Your bet was ${bet}.\"")
                    player.current_bet = bet
                    break
            except ValueError:
                print("\t----ERROR: Invalid option. Please enter an integer (whole) number.")

    def get_hand(self, deck):
        card1 = cards.Card(deck.deal_card())
        card2 = cards.Card(deck.deal_card())
        self.dealt_cards.append(card1.name)
        self.dealt_cards.append(card2.name)
        print(f"Randomly dealt hand to {self.name}: ")
        card1.print_up()
        card2.print_down()
        # print(card2.name) # test purposes
        self.hand_value = card1.value + card2.value
        # print(f"--Hand value is currently {self.hand_value}") # use for test purposes. player should not know dealer's hand value at this point
        if self.hand_value > 21:  # dealer busted, end round
            print(f"Tough luck. {self.name} was dealt a bust. Game over.")
        elif self.hand_value == 21:  # dealer was dealt a blackjack, end round
            print(f"Wow! {self.name} has been dealt a blackjack. Game over.")
        else:
            self.has_hand = True
        return card1, card2

    def show_card(self, deck, card1, card2):
        print(f"{self.name}: I will now flip over the last card.")
        cards.Card.print_up(card1)
        cards.Card.print_up(card2)
        if self.hand_value >= 17:
            print(f"----Dealer hand value is currently at {self.hand_value}. {self.name} must stay.")
        else:
            while self.hand_value < 17:
                print(f"----Dealer hand value is currently at {self.hand_value}. {self.name} must hit.")
                self.hit(deck)
            else:
                print(f"----Updated dealer hand value is {self.hand_value}. {self.name} has busted! Game over.")



# ---------------------------------------------------------------------------------------------------------------------



def rules(player):  # function to print rules to user
    print("\nThe concept of Blackjack is simple. Try to beat the dealer!")
    print("\nHow this version of Simple Blackjack works:")
    print("\t1. Numbered cards are worth their number value (e.g. a 2 of Clubs is worth 2 points),"
          "face cards are worth 10 points, and in this game Aces are always worth 11!......")
    print("\t2. After a bet has been placed, your cards will be dealt to you at random from the shuffled deck......")
    print("\t3. If you are dealt a blackjack, you automatically win!......")
    print("\t4. If dealer is dealt a blackjack, the game will result in an instant dealer win and you will forfeit your bet......")
    print("\t5. Dealer will stay on 17 or above......")
    print("\t6. After viewing both hands, you will decide to 'hit' for another card or take your chances and 'stay'......")
    print("\t7. You may hit for as many cards as you can, but if you go over 21 you will 'bust' and lose the game......")
    print(f"\nYou will start with $100. Good luck!")
    player.bank += 100


def bust_reset(deck, player, dealer):
    player.bank -= player.current_bet
    player.has_hand = False  # reset player attributes
    player.current_bet = 0
    player.hand_value = 0
    print(f"\nYour bet of ${player.current_bet} has been forfeited. Your bank has been updated."
          f"\nHere is your updated info:")
    player.info()
    # TODO: Finish bust_reset
    dealer.has_hand = False  # reset dealer attributes
    dealer.hand_value = 0





