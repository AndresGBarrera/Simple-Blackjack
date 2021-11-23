# -----------------------------------------------------
# Simple Blackjack game (main.py file)
# By Andres Barrera (agb0174) and Rony Lopez
# -----------------------------------------------------
import blackjack
import cards
import random


if __name__ == "__main__":
    # print introduction
    print("+---------------------------------------------------+\n|       "
          "Computer Science and Engineering            |"
          "\n|      CSCE 1035 - Computer Programming I           "
          "|\n|        Andres Barera and Rony Lopez               |"
          "\n+---------------------------------------------------+")
    print("\nWelcome to Simple Blackjack by Andres Barrera and Rony Lopez!")
    user_name = input("\nTo get started, please enter your name: ")
    print(f"\n--------------------Welcome, {user_name}!--------------------")

    # setup player, dealer, and game instances
    player = blackjack.Player(user_name)
    possible_names = ["John", "Kevin", "Bob", "Michael", "Karen", "Tiffany", "Sarah", "Victoria"]
    dealer = blackjack.Dealer(random.choice(possible_names))  # setup new dealer, deck, and game instances
    deck = cards.Deck()
    game = blackjack.Game(deck, dealer, player)
    blackjack.rules()  # print game rules to user
    game.first_run()
    # run first game using methods from Game class
    while not game.over:  # while loop to keep game going until someone busts or has a blackjack
        game.get_player_bet()
        game.new_hand()
        game.decide_winner()
    game.reset(dealer, player)

    # first hand is over, ask user if they want to keep playing, if not exit program
    done = False  # boolean that represents if player is done playing
    while not done and player.bank > 0:  # while loop to keep playing hands until user is done, or runs out of money
        done = player.postgame()  # uses postgame method to assign value of True or False depending on user input
        if done:  # if done is True, break loop, else continue to play
            break

        while not game.over:  # while loop to keep game going until someone busts or has a blackjack
            # setup new deck and game instances, run through game again
            deck = cards.Deck()
            game = blackjack.Game(deck, dealer, player)
            game.get_player_bet()
            game.new_hand()
            game.decide_winner()
        game.reset(dealer, player)


    # if/else statement to decide what to print to user at end of program
    if player.bank <= 0:
        print("\nLooks like you lost all your money on the blackjack table! Tough luck!"
              "\n\t****GAME OVER****")
    else:
        print(f"\nThank you for playing, {player.name}!")
        print(f"You exited with ${player.bank}. Impressive!")
    print(f"******TOTAL AMOUNT WON TODAY******\n\t--${player.total_winnings}")
    print(f"******TOTAL AMOUNT LOST TODAY******\n\t--${dealer.bank}")


