# -----------------------------------------------------
# Simple Blackjack game (blackjack.py file)
# By Andres Barrera (agb0174)
# -----------------------------------------------------
import random
import cards


class Player:
    def __init__(self, name="None", bank=100, has_hand=False, current_bet=0):  # initializing player instance
        self.name = name
        self.bank = bank
        self.has_hand = has_hand
        self.current_bet = current_bet

    def info(self):  # function used to return info about the player [name and current bank amount]
        print(f"\t--Player name: {self.name}\n\t--Current amount in bank: ${self.bank}")


    def get_hand(self, deck, dealer): #function to give player hand, keep giving cards until player stays or busts
        dealt_cards = []
        card1 = cards.Card(deck.deal_card())
        card2 = cards.Card(deck.deal_card())
        dealt_cards.append(card1.name)
        dealt_cards.append(card2.name)
        print("Randomly dealt hand: ")
        card1.print_up()
        card2.print_up()
        hand_value = card1.value + card2.value # make sure player does not have blackjack, if so end game
        print(f"--Hand value is currently {hand_value}")
        if hand_value > 21: # user busted, end game
            print(f"Tough luck. {self.name} was dealt a bust. Game over.")
        elif hand_value == 21:
            print(f"Wow! {self.name} has been dealt a blackjack. Game over.")
        else:
            self.has_hand = True
            while hand_value <= 21:
                player_choice = input(f"{dealer.name}: \"\nWould you like to hit or stay?\"\nEnter 'h' to hit or 's' to stay >>>>>> ")
                if player_choice == 'h':
                    print("You chose to hit.")
                    card3 = cards.Card(deck.deal_card())
                    dealt_cards.append(card3.name)
                    print("Here is your next card:")
                    card3.print_up()
                    hand_value += card3.value
                    print(f"--Updated hand value is {hand_value}")
                elif player_choice == 's':
                    print("You chose to stay")
                    break
                else:
                    print("ERROR: Invalid option. Please enter 'h' or 's'")
            else:  # player busted
                print(
                    f"\n{dealer.name}: Oh no! Looks like you busted. Unfortunately you have lost. Better luck next time!")
                deck.reset()
                self.has_hand = False
                print(f"{dealer.name}: Your bet of ${self.current_bet} has been forfeited. Your bank has been updated.\nHere is your updated info:")
                self.bank -= self.current_bet
                self.info()
                self.current_bet = 0
        return dealt_cards


class Dealer:

    def __init__(self, name="None", bank=0, has_hand=False):  # initializing dealer instance, random name from list
        names_list = ["John", "Kevin", "Bob", "Michael", "Karen", "Tiffany", "Sarah", "Victoria"]
        self.name = random.choice(names_list)
        self.bank = bank
        self.has_hand = has_hand

    def intro(self):
        print("------------------------------------------------------------------------------------------------------------")
        print(f"\nThe dealer assigned to you today is: {self.name}")
        print(f"\nFrom {self.name}: \"Good evening! I will be your dealer today. Let's get this show on the road!\"")

    def get_bet(self, player):
        player.info()
        while True:
            bet = int(input(f"{self.name}: \"Please enter your bet amount now\" >>>>>> $"))
            if bet > player.bank:
                print(f"\n{self.name}: \"Uh oh. Looks like you don\'t have enough in the bank for that bet!\"\n\tPlease try again.")
            elif bet <= 0:
                print(f"\n{self.name}: \"You have to bet something! No free hands here, sorry.\"\n\t--Please try again.")
            else:
                print(f"\n{self.name}: \"Great! Your bet was ${bet}.\"")
                player.current_bet = bet
                break


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
    print("\t6. You may hit for as many cards as you can, but if you go over 21 you will 'bust' and lose the game")
    print("\nYou will start with $100. Good luck!")


def end_hand(dealer, player, deck):
    pass



