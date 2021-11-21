# -----------------------------------------------------
# Simple Blackjack game (cards.py file)
# By Andres Barrera (agb0174) and Rony Lopez
# -----------------------------------------------------
import random


class Deck:
    def __init__(self, game_deck=None):  # create deck
        if game_deck is None:
            new_deck = []
            card_name = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
            card_suit = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
            for name in range(len(card_name)):  # for loop to create deck that will be used for game
                for suit in range(len(card_suit)):
                    new_card = card_name[name] + ' of ' + card_suit[suit]
                    new_deck.append(new_card)
            random.shuffle(new_deck)
            self.game_deck = new_deck
        else:
            self.game_deck = game_deck

    def check(self):  # function to print out deck list and length to make sure there are 52 unique cards
        print(self.game_deck)
        print(len(self.game_deck))

    def deal_card(self):  # function to get random card from deck and remove it from game deck
        card_choice = random.choice(self.game_deck)
        self.game_deck.remove(card_choice)
        return card_choice


class Card:
    def __init__(self, name="None"):  # initialize card
        self.name = name
        self.value = 0

        # assign value to card
        name_as_list = self.name.split(' of ')  # create new list separating the card name and suit
        card_num = name_as_list[0]
        if card_num == 'Ace':  # if/else statement to decide if card is face card or not, then assign value
            self.value = 11  # TODO: Figure out how to assign ace value of 1 or 11 depending on hand value
        elif card_num == 'Jack':
            self.value = 10
        elif card_num == 'Queen':
            self.value = 10
        elif card_num == 'King':
            self.value = 10
        else:  # card does not have a face name, convert name to a value using int()
            self.value = int(name_as_list[0])

    def print_up(self):  # function to print card face-up
        name_as_list = self.name.split(" of ")  # create new list separating the card name and suit
        card_num = name_as_list[0]
        card_suit = name_as_list[1]
        suits = ['♥', '♦', '♣', '♠']  # list of characters that will be used to represent the suit on the car
        if card_num == 'Ace':  # if/else statement to change card name to number
            n = 'A'
        elif card_num == 'Jack':
            n = 'J'
        elif card_num == 'Queen':
            n = 'Q'
        elif card_num == 'King':
            n = 'K'
        else:
            n = card_num

        if card_suit == 'Clubs':  # if/else statement to assign symbol using card suit
            s = suits[2]
        elif card_suit == 'Spades':
            s = suits[3]
        elif card_suit == 'Hearts':
            s = suits[0]
        else:
            s = suits[1]

        print(self.name)
        print(f'┌───────┐\n| {n:<2}    |\n|       |\n|   {s}   |\n|       |\n|    {n:>2} |\n└───────┘')

    @staticmethod
    def print_down():  # function to print card face-down
        # print(self.card_name) #test to make sure instance of card is being passed through
        n = '?'
        s = '?'
        print("\nUnknown card")
        print(f'┌───────┐\n| {n:<2}    |\n|       |\n|   {s}   |\n|       |\n|    {n:>2} |\n└───────┘')


# -----------------------------------------------------------------------------------------------------------------------
