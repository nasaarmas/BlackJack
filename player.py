import random

all_cards = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
cards_symbols = ("clubs", "spades", "hearts", "diamonds")
all_cards_val = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10,
                 'A': 11}


class Cards:
    def __init__(self, card_symbol, card_value):
        self.suit = card_symbol
        self.value = card_value


class Hand:

    def __init__(self):
        self.game_points = 0
        self.cards = []
        self.ace = False

    def __str__(self):
        for card in self.cards:
            card_name = card.__str__()
            print(card_name)

    def hit(self, card):
        self.cards.append(card)

        if card == 'A':
            self.ace = True
        self.game_points += all_cards_val[card]


class PlayingDeck:
    def __init__(self):
        self.deck = []
        for suit in cards_symbols:
            for card in all_cards:
                self.deck.append(Cards(suit, card))

    def shuffle(self):
        random.shuffle(self.deck)

    def hit(self):
        hit_card = self.deck.pop()
        return hit_card

# def game():
#    player_choice = 0
#   player_choice = input("Do you want to [T]ake another card, [P]ause, [Q]uit: ".lower())
