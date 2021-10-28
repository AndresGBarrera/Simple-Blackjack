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
    player.rules()
    dealer.intro()

    dealer.get_bet(player)  # use get_bet function to get bet, passing in player instance as argument| create instances of card using dealCard function from blackjack module as argument
    player.get_hand(deck)  # get_hand function to assign a new hand to player
    dealer.get_hand(deck)  # get_hand function to assign a new hand to dealer
    # print(player.dealt_cards, dealer.dealt_cards) #test
    # print(player.has_hand, dealer.has_hand) #test



