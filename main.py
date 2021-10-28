# -----------------------------------------------------
# Simple Blackjack game (main.py file)
# By Andres Barrera (agb0174)
# -----------------------------------------------------
import blackjack
import cards

# only run code below if this file is run as main file
if __name__ == "__main__":

    blackjack.intro()  # run game intro from blackjack module, collect user's name and use to create new instance of player
    user_name = input("\nTo get started, please enter your name: ")
    print(f"\n--------------------Welcome, {user_name}!--------------------")
    player = blackjack.Player(user_name)

    dealer = blackjack.Dealer()  # setup new dealer, deck, and game instances, print game rules and dealer intro
    deck = cards.Deck()
    blackjack.rules()
    dealer.intro()
    while player.bank > 0:
        dealer.get_bet(player)  # use get_bet function to get bet, passing in player instance as argument| create instances of card using dealCard function from blackjack module as argument
        player_hand = player.get_hand(deck, dealer)  # get_hand function to assign a new hand to player, assign hand to variable so we can send it to be reset
        #dealer_hand = deck.give_hand(dealer)  # get_hand function to assign a new hand to dealer, assign hand to variable we can send it to be reset
    else:
        print(f"\n{dealer.name}: like you have run out of money my friend. Better luck on your next trip to the blackjack table!")
        print("Thanks for playing!")


    # ---------------------------------TEST BLOCK----------------------------------------------#
    #print(player.current_bet)
    #print(player_hand)
    #print(card1.getValue())
    #print(card2.getValue())
    #deck.check()
    #print(card.name)
    # -----------------------------------------------------------------------------------------#


