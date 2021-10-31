# -----------------------------------------------------
# Simple Blackjack game (main.py file)
# By Andres Barrera (agb0174)
# -----------------------------------------------------
import blackjack
import cards
import random

# only run code below if this file is run as main file
if __name__ == "__main__":
    print("+---------------------------------------------------+\n|       "
          "Computer Science and Engineering            |"
          "\n|      CSCE 1035 - Computer Programming I           "
          "|\n| Andres Barera agb0174 andresbarrera@my.unt.edu    |"
          "\n+---------------------------------------------------+")
    print("\nWelcome to Simple Blackjack by Andres Barrera!")
    user_name = input("\nTo get started, please enter your name: ")
    print(f"\n--------------------Welcome, {user_name}!--------------------")
    player = blackjack.Player(user_name)
    possible_names = ["John", "Kevin", "Bob", "Michael", "Karen", "Tiffany", "Sarah", "Victoria"]
    dealer = blackjack.Dealer(random.choice(possible_names))  # setup new dealer, deck, and game instances
    deck = cards.Deck()
    game = blackjack.Game(deck, dealer, player)
    blackjack.rules()  # print game rules
    game.first_run()
    game.get_player_bet()
    game.start()

    # print(player.dealt_cards, dealer.dealt_cards) #test
    # print(player.has_hand, dealer.has_hand) #testr

