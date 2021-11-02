# -----------------------------------------------------
# Simple Blackjack game (blackjack.py file)
# By Andres Barrera (agb0174)
# -----------------------------------------------------
import cards
import main


def rules():  # function to print rules to user
    print("\nThe concept of Blackjack is simple. Try to beat the dealer!")
    print("\nHow this version of Simple Blackjack works:")
    print("\t1. Numbered cards are worth their number value (e.g. a 2 of Clubs is worth 2 points),"
          "face cards are worth 10 points, and Aces will be worth 11 points until your hand value is > 21. Ace will then be worth 1 point so you do not bust")
    print("\t2. After a bet has been placed, your cards will be dealt to you at random from the shuffled deck")
    print("\t3. If you are dealt a blackjack, you automatically win!")
    print("\t4. If dealer is dealt a blackjack, "
          "the game will result in an instant dealer win and you will forfeit your bet")
    print("\t5. Dealer will stand on 17 or above")
    print("\t6. After viewing both hands, "
          "you will decide to 'hit' for another card or take your chances and 'stay'")
    print("\t7. You may hit for as many cards as you can, "
          "but if you go over 21 you will 'bust' and lose the game!")


class Player:
    current_bet = 0

    def __init__(self, name="None", bank=0, hand_value=0, current_hand=None, current_bet=0, busted=False):  # initializing player
        self.name = name
        self.bank = bank
        self.hand_value = hand_value
        self.current_bet = current_bet
        self.busted = busted
        if current_hand is None:
            self.current_hand = []
        else:
            self.current_hand = current_hand

    def info(self):  # function used to return info about the player [name and current bank amount]
        print(f"\t--Player name: {self.name}\n\t--Current amount in bank: ${self.bank}")

    def hit(self, deck):  # function to allow player to stay or
        card = cards.Card(deck.deal_card())
        self.current_hand.append(card.name)
        card.print_up()
        self.hand_value += card.value
        print(f"--Updated hand value is {self.hand_value}")
        if self.hand_value == 21:
            print(f"****Hand value is currently at 21! {self.name} has a blackjack! Game over.")
            Game.end()
        elif self.hand_value > 21:  # player/dealer busted, end game
            print(f"{self.name} has busted!")
            self.busted = True
            Game.end()


    def get_hand(self, deck):  # function to give player hand, keep giving cards until player stays or busts
        card1 = cards.Card(deck.deal_card())
        card2 = cards.Card(deck.deal_card())
        self.current_hand.append(card1.name)
        self.current_hand.append(card2.name)
        self.hand_value = card1.value + card2.value
        print(f"Randomly dealt hand to {self.name}: ")
        card1.print_up()

        if self.hand_value > 21:  # busted, end round
            print(f"--Hand value is currently {self.hand_value}")
            print(f"Tough luck. {self.name} was dealt a bust. Game over.")  # TODO: Add reset function here
            self.busted = True
            Game.end()
        elif self.hand_value == 21:  # dealt a blackjack, end round
            print(f"--Hand value is currently {self.hand_value}")
            print(f"Wow! {self.name} has been dealt a blackjack. Game over.")  # TODO: Add reset function here
            Game.end()  # TODO: Make sure game is ending when blackjacks are dealt

        if issubclass(type(self), Dealer):  # if true , self = dealer instance
            card2.print_down()
        else:  # false, self = player instance
            card2.print_up()
            print(f"--Hand value is currently {self.hand_value}")
            print("....Dealer's turn to get cards....")
        return card1, card2

    def postgame(self):
        while True:
            user_choice = input(f"\nWould you like to play another hand?"
                                f"\n\t--To play again enter 'y', or to quit enter 'q' >>> ")

            if user_choice.upper() == 'Y' or user_choice.upper() == 'YES':
                print("--You chose to play again. Good luck!")
                return False
            elif user_choice.upper() == 'Q' or user_choice.upper() == 'QUIT':
                print("--You chose to quit. See you next time!")
                return True
            else:
                print("ERROR: Invalid option! Please try again.")

    def reset(self):
        self.current_bet = 0
        self.hand_value = 0
        self.current_hand.clear()
        self.busted = False

    def winner(self):
        print(f"\nPlayer has won this hand!\nCongrats {self.name}, you have won ${self.current_bet * 2}!")
        print("\t******GAME RESULT: WIN******\nUpdated info after this hand:")
        self.bank += self.current_bet * 2
        self.info()


class Dealer(Player):
    def ___init__(self, name, bank, hand_value, current_hand, busted):  # initializing dealer instance5
        super().__init__(name, bank, hand_value, current_hand, busted)

    def check_hand(self, deck):
        if self.hand_value >= 17:
            print(f"----Dealer hand value is currently at {self.hand_value}. {self.name} must stand.")
        else:
            while self.hand_value < 17:
                print(f"----Dealer hand value is currently at {self.hand_value}. {self.name} must hit.")
                self.hit(deck)
                if 17 <= self.hand_value < 21:
                    print(
                        f"----Dealer hand value is currently at or greater than 17. {self.name} must stand.")
                    break
                elif self.hand_value == 21:
                    print(f"Dealer has a blackjack, they win! Game over.")
                    break
            else:
                print(f"--Dealer has busted! Game over.")
                self.busted = True
                Game.end()

    def win(self, player):
        self.bank += player.current_bet
        print(f"\n--Dealer has won this hand! You have forfeited you bet of {player.current_bet}.")
        print("\t******GAME RESULT: LOSS******\nUpdated info after this hand:")
        player.info()


class Game:
    over = False

    def __init__(self, deck, dealer, player):
        self.deck = deck
        self.dealer = dealer
        self.player = player

    def first_run(self):
        print("You will start with $100. Good luck!")
        self.player.bank += 100
        self.player.info()
        print("------------------------------------------------------------------------------------------------------------")
        print(f"\nThe dealer assigned to you today is: {self.dealer.name}")
        print(f"\nFrom {self.dealer.name}: \"Good evening! I will be your dealer today. Let's get this show on the road!\"")

    def get_player_bet(self):
        # assign these to variables so code is easier to read
        dealer = self.dealer
        player = self.player

        while player.current_bet == 0:
            try:  # try/except to handle ValueError that crashes program if user enters anything but an integer
                bet = int(input(f"{dealer.name}: \"Please enter your bet amount now\" >>>>>> $"))
                if bet > player.bank:
                    print(f"\n{dealer.name}: \"Uh oh. Looks like you don\'t have enough in the bank for that bet!\""
                          f"\n\t----Please enter a bet less than your current bank. "
                          f"\nHere's your info:")
                    player.info()
                elif bet <= 0:
                    print(f"\n{dealer.name}: \"You have to bet something! No free hands here, sorry.\""
                          f"\n\t----Please enter a bet larger than $0")
                else:
                    print(f"\n{dealer.name}: \"Great! Your bet was ${bet}.\"")
                    player.current_bet = bet
                    player.bank -= bet
                    break
            except ValueError:
                print("\t----ERROR: Invalid option. Please enter an integer (whole) number.")

    def new_hand(self):
        player = self.player
        dealer = self.dealer
        deck = self.deck

        player_card1, player_card2 = player.get_hand(deck)  # get_hand function to assign a new hand to player
        player.current_hand.append(player_card1)
        player.current_hand.append(player_card2)
        dealer_card1, dealer_card2 = dealer.get_hand(deck)  # get_hand function to assign a new hand to dealer
        dealer.current_hand.append(dealer_card1)
        dealer.current_hand.append(dealer_card2)

        while not player.busted:
            player_choice = input(f"{dealer.name}: \"Would you like to hit or stay?\""
                                  f"\nEnter 'h' to hit or 's' to stay >>>>>> ")
            if player_choice.upper() == 'H' or player_choice.upper() == 'HIT':
                print(f"{dealer.name}: You chose to hit. Here is your card")
                player.hit(deck)
            elif player_choice.upper() == 'S' or player_choice.upper() == 'STAY':
                print(f"{dealer.name}: You chose to stay. I will now reveal the hidden card.")
                cards.Card.print_up(dealer_card1)
                cards.Card.print_up(dealer_card2)
                dealer.check_hand(deck)
                break
            else:
                print("\t----ERROR: Invalid option. Please enter 'h' or 's'----")

    def reset(self, dealer, player):  # need to reset player/dealer variables and reset the deck (maybe on the deck)
        self.over = False
        dealer.reset()
        player.reset()

    @staticmethod
    def end():
        Game.over = True

    def decide_winner(self):
        player = self.player
        dealer = self.dealer
        print("\n\t----------GAME OVER----------")
        print("\n****FINAL HAND VALUES****")
        print(f"\n\t{player.name}: {player.hand_value}")
        print(f"\n\t{dealer.name}: {dealer.hand_value}")

        if player.hand_value > dealer.hand_value and not player.busted and not dealer.busted: # win for player
            player.winner()
        elif player.hand_value < dealer.hand_value and not player.busted and not dealer.busted: # loss for player
            dealer.win(player)
        elif player.hand_value == dealer.hand_value and not player.busted and not dealer.busted:
            print("Player and dealer have the same hand value!")
            print(f"{dealer.name}: Looks like you get to keep your bet, {player.name}.")
            print("\t******GAME RESULT: PUSH (tie)******")
            player.bank += player.current_bet  # give bet back to player
        elif not player.busted and dealer.busted:
            player.winner()
        elif player.busted and not dealer.busted:
            dealer.win(player)
        else:
            print("ERROR: Game outcome not recognized.")
