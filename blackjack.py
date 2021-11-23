# -----------------------------------------------------
# Simple Blackjack game (blackjack.py file)
# By Andres Barrera (agb0174) and Rony Lopez
# -----------------------------------------------------
import cards


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


class Player:  # creating instance of a player
    total_winnings = 0  # class variable for player's total_winnings

    def __init__(self, name="None", bank=0, hand_value=0, current_hand=None, current_bet=0, busted=False):  # initializing player with default values
        self.name = name
        self.bank = bank
        self.hand_value = hand_value
        self.current_bet = current_bet
        self.busted = busted
        if current_hand is None:  # if/else statement to create list that will hold the names of cards in player's current hand
            self.current_hand = []
        else:
            self.current_hand = current_hand

    def info(self):  # function used to return info about the player [name and current bank amount]
        print(f"\t--Player name: {self.name}\n\t--Current amount in bank: ${self.bank}")

    def hit(self, game, deck):  # method to create new card instance and reveal to user
        card = cards.Card(deck.deal_card())
        self.current_hand.append(card.name)
        card.print_up()
        self.hand_value += card.value  # update hand_value variable
        print(f"--Updated hand value is {self.hand_value}")

        if self.hand_value == 21:  # player/dealer was dealt a blackjack, end game
            print(f"****Hand value is currently at 21! {self.name} has a blackjack! Game over.")
            game.end()
        elif self.hand_value > 21:  # player/dealer busted, end game
            print(f"{self.name} has busted!")
            self.busted = True
            game.end()


    def get_hand(self, game, deck):  # method to give player hand, keep giving cards until player stays or busts
        # create card instances, add cards to current_hand list, update hand value, print card1
        card1 = cards.Card(deck.deal_card())
        card2 = cards.Card(deck.deal_card())
        self.current_hand.append(card1.name)
        self.current_hand.append(card2.name)
        self.hand_value = card1.value + card2.value
        print(f"Randomly dealt hand to {self.name}: ")
        card1.print_up()

        #end game if player busts or is dealt a blackjack
        if self.hand_value > 21:  # busted, end round
            print(f"--Hand value is currently {self.hand_value}")
            print(f"Tough luck. {self.name} was dealt a bust. Game over.")
            self.busted = True
            game.end()
        elif self.hand_value == 21:  # dealt a blackjack, end round
            print(f"--Hand value is currently {self.hand_value}")
            print(f"Wow! {self.name} has been dealt a blackjack. Game over.")
            game.end()

        # if/else statement to print out card2 either up or down, depending on issubclass function return value
        if issubclass(type(self), Dealer):  # issubclass function returns T/F if instance is a subclass
            card2.print_down()  # dealer's final card needs to be hidden, call to print_down method
        else:  # false, self = player instance, print card up
            card2.print_up()
            print(f"--Hand value is currently {self.hand_value}")
            print("....Dealer's turn to get cards....")
        return card1, card2  #return card2 and card2 instances

    @staticmethod
    def postgame():  # static method to ask user if they want to play again after hand is over, returns True or False depending on answer
        while True:
            user_choice = input(f"\nWould you like to play another hand?"
                                f"\n\t--To play again enter 'y', or to quit enter 'q' >>> ")

            if user_choice.upper() == 'Y' or user_choice.upper() == 'YES':
                print("\n--You chose to play again. Good luck!")
                return False
            elif user_choice.upper() == 'Q' or user_choice.upper() == 'QUIT':
                print("\n--You chose to quit. See you next time!")
                return True
            else:
                print("ERROR: Invalid option! Please try again.")

    def reset(self):  # method to reset dealer/player class variables
        self.current_bet = 0
        self.hand_value = 0
        self.current_hand.clear()  # clear current_hand list
        self.busted = False

    def winner(self, game):  # method used when player, updates bank, prints user info, ends game
        winnings = self.current_bet * 2  # assign winnings to variable to make code easier to read

        print(f"\nPlayer has won this hand!\nCongrats {self.name}, you have won ${self.current_bet * 2}!")
        print("\t******GAME RESULT: WIN******\nUpdated info after this hand:")
        self.bank += winnings  # update bank total using current_bet value
        self.total_winnings += winnings  # update total_winnings to keep track of player's total amount won over x hands
        self.info()
        game.end()


class Dealer(Player):  # creating instance of Dealer, child/subclass of Player class
    def ___init__(self, name, bank, hand_value, current_hand, busted):  # initializing dealer instance with default values
        super().__init__(name, bank, hand_value, current_hand, busted)  # default values inherited from Player class

    def check_hand(self, game, deck):  # method to check the value of dealer's hand, end game if necessary
        if self.hand_value >= 17:  # dealer must stand at hand value of 17 or more
            print(f"----Dealer hand value is currently at {self.hand_value}. {self.name} must stand.")
        else:
            while self.hand_value < 17:  # while loop to keep hitting until Dealers hand is <=21 but > 17
                print(f"----Dealer hand value is currently at {self.hand_value}. {self.name} must hit.")
                self.hit(game, deck)
                if 17 <= self.hand_value < 21:  # range dealer must stand in (17-20)
                    print(f"----Dealer hand value is currently at or greater than 17. {self.name} must stand.")
                    break
                elif self.hand_value == 21:  # dealer has a blackjack
                    print(f"Dealer has a blackjack, they win! Game over.")
                    game.end()
                    break
            else:  # dealer hand value is over 21, has busted
                print(f"--Dealer has busted! Game over.")
                self.busted = True
                game.end()

    def win(self, game, player):  # method to use when dealer is winner
        self.bank += player.current_bet  #update dealer bank to keep track of total losses
        print(f"\n--Dealer has won this hand! You have forfeited you bet of ${player.current_bet}.")
        print("\t******GAME RESULT: LOSS******\nUpdated info after this hand:")
        player.info()
        game.end()


class Game:  # Game class to create instance of a game (blackjack hand)
    over = False

    def __init__(self, deck, dealer, player):  # initialize with deck, dealer, player arguments
        self.deck = deck
        self.dealer = dealer
        self.player = player

    def first_run(self):  # method to give player bank $100
        print("You will start with $100. Good luck!")
        self.player.bank += 100
        self.player.info()
        print("------------------------------------------------------------------------------------------------------------")
        print(f"\nThe dealer assigned to you today is: {self.dealer.name}")
        print(f"\nFrom {self.dealer.name}: \"Good evening! I will be your dealer today. Let's get this show on the road!\"")

    def get_player_bet(self):
        # assign dealer, player instances to variables so code is easier to read
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
        # assign variables to make code easier to read
        player = self.player
        dealer = self.dealer
        deck = self.deck
        game = self  # game instance

        # assign cards to dealer and player
        player_card1, player_card2 = player.get_hand(game, deck)  # get_hand function to assign a new hand to player
        player.current_hand.append(player_card1)
        player.current_hand.append(player_card2)
        dealer_card1, dealer_card2 = dealer.get_hand(game, deck)  # get_hand function to assign a new hand to dealer
        dealer.current_hand.append(dealer_card1)
        dealer.current_hand.append(dealer_card2)

        # ask user hit or stay
        while not player.busted and not self.over:  # while loop to keep block going until player has busted or game is over
            player_choice = input(f"{dealer.name}: \"Would you like to hit or stay?\""
                                  f"\nEnter 'h' to hit or 's' to stay >>>>>> ")
            if player_choice.upper() == 'H' or player_choice.upper() == 'HIT':  # if/else block to handle possible choices
                print(f"{dealer.name}: You chose to hit. Here is your card")
                player.hit(game, deck)
            elif player_choice.upper() == 'S' or player_choice.upper() == 'STAY':
                print(f"{dealer.name}: You chose to stay. I will now reveal the hidden card.")
                cards.Card.print_up(dealer_card1)
                cards.Card.print_up(dealer_card2)
                dealer.check_hand(game, deck)
                break
            else:  # user did not enter h/hit or s/stay
                print("\t----ERROR: Invalid option. Please enter 'h' or 's'----")

    def reset(self, dealer, player):  # method to reset player/dealer attributes
        self.over = False
        dealer.reset()
        player.reset()

    def end(self):
        self.over = True

    def decide_winner(self):
        player = self.player
        dealer = self.dealer
        game = self
        print("\n\t----------GAME OVER----------")
        print("\n****FINAL HAND VALUES****")
        print(f"\n\t{player.name}: {player.hand_value}")
        print(f"\n\t{dealer.name}: {dealer.hand_value}")

        if player.hand_value > dealer.hand_value and not player.busted and not dealer.busted:  # win for player
            player.winner(game)
        elif player.hand_value < dealer.hand_value and not player.busted and not dealer.busted:  # loss for player
            dealer.win(game, player)
        elif player.hand_value == dealer.hand_value and not player.busted and not dealer.busted:
            print("Player and dealer have the same hand value!")
            print(f"{dealer.name}: Looks like you get to keep your bet, {player.name}.")
            print("\t******GAME RESULT: PUSH (tie)******")
            player.bank += player.current_bet  # give bet back to player
            player.info()
            self.over = True
        elif not player.busted and dealer.busted:
            player.winner(game)
        elif player.busted and not dealer.busted:
            dealer.win(game, player)
        else:
            print("ERROR: Game outcome not recognized.")
