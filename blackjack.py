# -----------------------------------------------------
# Simple Blackjack game (blackjack.py file)
# By Andres Barrera (agb0174)
# -----------------------------------------------------
import random
import cards


class Player:
    def __init__(self, name="None"):  # initializing player instance
        self.name = name
        self.bank = 100
        self.has_hand = False
        self.current_bet = 0
        self.hand_value = 0
        self.dealt_cards = []

    def info(self):  # function used to return info about the player [name and current bank amount]
        print(f"\t----Player name: {self.name}\n\t----Current amount in bank: ${self.bank}")

    def hit(self, deck):  # function to allow player to stay or
        card = cards.Card(deck.deal_card())
        self.dealt_cards.append(card.name)
        card.print_up()
        self.hand_value += card.value
        print(f"--Updated hand value is {self.hand_value}")

    def stay(self, deck):
        pass

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
        elif self.hand_value == 21: # user was dealt a blackjack, end round
            print(f"Wow! {self.name} has been dealt a blackjack. Game over.")
        else:
            self.has_hand = True
        print("....Dealer's turn to get cards....")



class Dealer:

    def __init__(self, name="None"):  # initializing dealer instance, random name from list
        names_list = ["John", "Kevin", "Bob", "Michael", "Karen", "Tiffany", "Sarah", "Victoria"]
        self.name = random.choice(names_list)
        self.bank = 0
        self.has_hand = False
        self.hand_value = 0
        self.dealt_cards = []

    def intro(self):
        print("------------------------------------------------------------------------------------------------------------")
        print(f"\nThe dealer assigned to you today is: {self.name}")
        print(f"\nFrom {self.name}: \"Good evening! I will be your dealer today. Let's get this show on the road!\"")

    def get_bet(self, player):
        while True:
            try:  # try/except to handle ValueError that crashes program if user enters anything but an integer
                bet = int(input(f"{self.name}: \"Please enter your bet amount now\" >>>>>> $"))
                if bet > player.bank:
                    print(f"\n{self.name}: \"Uh oh. Looks like you don\'t have enough in the bank for that bet!\"\n\t----Please enter a bet less than your current bank. \nHere's your info:")
                    player.info()
                elif bet <= 0:
                    print(f"\n{self.name}: \"You have to bet something! No free hands here, sorry.\"\n\t----Please enter a bet larger than $0")
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
        self.hand_value = card1.value + card2.value
        # print(f"--Hand value is currently {self.hand_value}") # use for test purposes. player should not know dealer's hand value at this point
        if self.hand_value > 21:  # dealer busted, end round
            print(f"Tough luck. {self.name} was dealt a bust. Game over.")
        elif self.hand_value == 21:  # dealer was dealt a blackjack, end round
            print(f"Wow! {self.name} has been dealt a blackjack. Game over.")
        else:
            self.has_hand = True


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def intro():  # function to print intro to user
    print("+---------------------------------------------------+\n|       Computer Science and Engineering            |\n|      CSCE 1035 - Computer Programming I           |\n| Andres Barera agb0174 andresbarrera@my.unt.edu    |\n+---------------------------------------------------+")
    print("\nWelcome to Simple Blackjack by Andres Barrera!")


def rules():  # function to print rules to user
    print("\nThe concept of Blackjack is simple. Try to beat the dealer!")
    print("")
    print("Rules:")
    print("\t1. Numbered cards are worth their number value (e.g. a 2 of Clubs is worth 2 points),face cards are worth 10 points, and in this game Aces are always worth 11!......")
    print("\t2. After a bet has been placed, your cards will be dealt to you at random from the shuffled deck......")
    print("\t3. If you are dealt a blackjack, you automatically win!......")
    print("\t4. If dealer is dealt a blackjack, the game will result in an instant dealer win and you will forfeit your bet......")
    print("\t5. After viewing your cards, you will decide to 'hit' for another card or take your chances and 'stay'......")
    print("\t6. You may hit for as many cards as you can, but if you go over 21 you will 'bust' and lose the game......")
    print(f"\nYou will start with $100. Good luck!")


def bust_reset(deck, player, dealer):
    player.bank -= player.current_bet
    player.has_hand = False  # reset player attributes
    player.current_bet = 0
    player.hand_value = 0
    print(f"\nYour bet of ${player.current_bet} has been forfeited. Your bank has been updated.\nHere is your updated info:")
    player.info()

    dealer.has_hand = False  # reset dealer attributes
    dealer.hand_value = 0





