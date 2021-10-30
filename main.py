# -----------------------------------------------------
# Simple Blackjack game (main.py file)
# By Andres Barrera (agb0174)
# -----------------------------------------------------
import blackjack
import cards

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
    dealer = blackjack.Dealer()  # setup new dealer, deck, and game instances, print game rules and dealer intro
    deck = cards.Deck()
    blackjack.rules(player)
    player.info()

    print("------------------------------------------------------------------------------------------------------------")
    print(f"\nThe dealer assigned to you today is: {dealer.name}")
    print(f"\nFrom {dealer.name}: \"Good evening! I will be your dealer today. Let's get this show on the road!\"")
    dealer.get_bet(player)  # use get_bet function to get bet, passing in player instance as argument| create instances of card using dealCard function from blackjack module as argument
    player.get_hand(deck)  # get_hand function to assign a new hand to player
    card1, card2 = dealer.get_hand(deck)  # get_hand function to assign a new hand to dealer
    while player.hand_value <= 21:
        if player.hand_value != 21:
            player_choice = input(f"{dealer.name}: \"Would you like to hit or stay?\"\nEnter 'h' to hit or 's' to stay >>>>>> ")
            if player_choice.upper() == 'H' or player_choice.upper() == 'HIT':
                print(f"{dealer.name}: You chose to hit. Here is your card")
                player.hit(deck)
            elif player_choice.upper() == 'S' or player_choice.upper() == 'STAY':
                print(f"{dealer.name}: You chose to stay")
                dealer.show_card(deck, card1, card2)
                break
            else:
                print("\t----ERROR: Invalid option. Please enter 'h' or 's'----")
        else:
            print(f"----Player hand value is currently at 21. You have a blackjack! Game over.")
    else:  # player busted
        print(f"\n{dealer.name}: Oh no! Unfortunately you have busted and lost. Better luck next time!")
        blackjack.bust_reset(deck, player, dealer)

    # print(player.dealt_cards, dealer.dealt_cards) #test
    # print(player.has_hand, dealer.has_hand) #test



