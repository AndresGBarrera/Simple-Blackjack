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
    while not game.over:
        game.get_player_bet()
        game.new_hand()
    else:
        game.decide_winner()
        game.reset(dealer, player)

    # first hand is over, ask user if they want to keep playing, if not exit
    done = False
    while not done and player.bank > 0:
        done = player.postgame()  # uses postgame method to assign value of True or False depending on user input
        if done:  # if done is True, break loop, else continue
            break

        # setup new deck and game instances, run through game again
        deck = cards.Deck()
        game = blackjack.Game(deck, dealer, player)
        game.reset(dealer, player)
        while not game.over:
            game.get_player_bet()
            game.new_hand()
        else:
            game.decide_winner()
            game.reset(dealer, player)


    if player.bank <= 0:
        print("\nLooks like you lost all your money on the blackjack table! Tough luck!"
              "\n\t****GAME OVER****")
    else:
        print(f"\nThank you for playing, {player.name}!")
        print(f"You exited with ${player.bank}. Impressive!")


