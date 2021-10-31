# -----------------------------------------------------
# Simple Blackjack game (blackjack.py file)
# By Andres Barrera (agb0174)
# -----------------------------------------------------
import cards


def rules():  # function to print rules to user
    print("\nThe concept of Blackjack is simple. Try to beat the dealer!")
    print("\nHow this version of Simple Blackjack works:")
    print("\t1. Numbered cards are worth their number value (e.g. a 2 of Clubs is worth 2 points),"
          "face cards are worth 10 points, and in this game Aces are always worth 11!......")
    print("\t2. After a bet has been placed, your cards will be dealt to you at random from the shuffled deck......")
    print("\t3. If you are dealt a blackjack, you automatically win!......")
    print("\t4. If dealer is dealt a blackjack, "
          "the game will result in an instant dealer win and you will forfeit your bet......")
    print("\t5. Dealer will stay on 17 or above......")
    print("\t6. After viewing both hands, "
          "you will decide to 'hit' for another card or take your chances and 'stay'......")
    print("\t7. You may hit for as many cards as you can, "
          "but if you go over 21 you will 'bust' and lose the game......")


class Player:
    current_bet=0

    def __init__(self, name="None", bank=0, has_hand=False, hand_value=0, dealt_cards=None, winner=False):  # initializing player
        self.name = name
        self.bank = bank
        self.has_hand = has_hand
        self.hand_value = hand_value
        self.winner = winner
        if dealt_cards is None:
            self.dealt_cards = []
        else:
            self.dealt_cards = dealt_cards

    def info(self):  # function used to return info about the player [name and current bank amount]
        print(f"\t--Player name: {self.name}\n\t--Current amount in bank: ${self.bank}")

    def hit(self, deck):  # function to allow player to stay or
        card = cards.Card(deck.deal_card())
        self.dealt_cards.append(card.name)
        card.print_up()
        self.hand_value += card.value
        print(f"--Updated hand value is {self.hand_value}")
        if self.hand_value == 21:
            print(f"****Hand value is currently at 21! {self.name} has a blackjack! Game over.")
        elif self.hand_value > 21:  # player/dealer busted, end game
            print(f"----{self.name} has busted! Game over.")


    def get_hand(self, deck):  # function to give player hand, keep giving cards until player stays or busts
        card1 = cards.Card(deck.deal_card())
        card2 = cards.Card(deck.deal_card())
        self.dealt_cards.append(card1.name)
        self.dealt_cards.append(card2.name)
        self.hand_value = card1.value + card2.value
        print(f"Randomly dealt hand to {self.name}: ")
        card1.print_up()

        if issubclass(type(self), Dealer):  # if true , self = dealer instance
            card2.print_down()
        else:  # false, self = player instance
            card2.print_up()
            print(f"--Hand value is currently {self.hand_value}")
            print("....Dealer's turn to get cards....")

        if self.hand_value > 21:  # busted, end round
            print(f"--Hand value is currently {self.hand_value}")
            print(f"Tough luck. {self.name} was dealt a bust. Game over.")
        elif self.hand_value == 21:  # dealt a blackjack, end round
            print(f"--Hand value is currently {self.hand_value}")
            print(f"Wow! {self.name} has been dealt a blackjack. Game over.")
        else:
            self.has_hand = True
        return card1, card2


class Dealer(Player):
    def ___init__(self, name, bank, has_hand, hand_value, dealt_cards):  # initializing dealer instance5
        super().__init__(name, bank, has_hand, hand_value, dealt_cards)


class Game:
    def __init__(self, deck, dealer, player, over=False):
        self.deck = deck
        self.dealer = dealer
        self.player = player
        self.over = over

    def first_run(self):
        print("You will start with $100. Good luck!")
        self.player.bank += 100
        self.player.info()
        print("------------------------------------------------------------------------------------------------------------")
        print(f"\nThe dealer assigned to you today is: {self.dealer.name}")
        print(f"\nFrom {self.dealer.name}: \"Good evening! I will be your dealer today. Let's get this show on the road!\"")

    def get_player_bet(self):
        while self.player.current_bet == 0:
            try:  # try/except to handle ValueError that crashes program if user enters anything but an integer
                bet = int(input(f"{self.dealer.name}: \"Please enter your bet amount now\" >>>>>> $"))
                if bet > self.player.bank:
                    print(f"\n{self.dealer.name}: \"Uh oh. Looks like you don\'t have enough in the bank for that bet!\""
                          f"\n\t----Please enter a bet less than your current bank. "
                          f"\nHere's your info:")
                    self.player.info()
                elif bet <= 0:
                    print(f"\n{self.dealer.name}: \"You have to bet something! No free hands here, sorry.\""
                          f"\n\t----Please enter a bet larger than $0")
                else:
                    print(f"\n{self.dealer.name}: \"Great! Your bet was ${bet}.\"")
                    self.player.current_bet = bet
                    break
            except ValueError:
                print("\t----ERROR: Invalid option. Please enter an integer (whole) number.")

    def start(self):  # TODO: Fix this method to correctly end game if either player is dealt a blackjack, was still asked to hit when dealer was dealt a blackjack
        self.player.get_hand(self.deck)  # get_hand function to assign a new hand to player
        card1, card2 = self.dealer.get_hand(self.deck)  # get_hand function to assign a new hand to dealer
        while self.player.hand_value < 21:
            player_choice = input(f"{self.dealer.name}: \"Would you like to hit or stay?\""
                                  f"\nEnter 'h' to hit or 's' to stay >>>>>> ")
            if player_choice.upper() != 'H' or player_choice.upper() != 'HIT':
                print(f"{self.dealer.name}: You chose to hit. Here is your card")
                self.player.hit(self.deck)
            elif player_choice.upper() != 's' or player_choice.upper() != 'STAY':
                print(f"{self.dealer.name}: You chose to stay")
                self.reveal_dealer_card(card1, card2)
                break
            else:
                print("\t----ERROR: Invalid option. Please enter 'h' or 's'----")

    def reveal_dealer_card(self, card1, card2):
        print(f"{self.dealer.name}: I will now flip over the last card.")
        cards.Card.print_up(card1)
        cards.Card.print_up(card2)
        if self.dealer.hand_value >= 17:
            print(f"----Dealer hand value is currently at {self.dealer.hand_value}. {self.dealer.name} must stand.")
        else:
            while self.dealer.hand_value != 17 and self.dealer.hand_value < 21:
                print(f"----Dealer hand value is currently at {self.dealer.hand_value}. {self.dealer.name} must hit.")
                self.dealer.hit(self.deck)
                if self.dealer.hand_value <= 17 or self.dealer.hand_value < 21:
                    print(f"----{self.dealer.name} hand value is currently at or greater than 17. {self.dealer.name} must stand.")
                    break
                elif self.dealer.hand_value == 21:
                    print(f"{self.dealer.name} has a blackjack, they win! Game over.")
                    break
                else:
                    continue
            else:
                print(f"----Dealer has busted! Game over.")

    def reset(self, deck, player, dealer):
        pass

    def decide_winner(self):
        pass
