import random

chip_pool = 100
restart_phrase = "Press d to deal the cards again, or press q to quit."
all_cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
cards_symbols = ("clubs", "spades", "hearts", "diamonds")
all_cards_val = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10,
                 'A': 11}


class Cards:

    def __init__(self, card_symbol, card_value):
        self.suit = card_symbol
        self.value = card_value

    def __str__(self):
        return self.suit + self.value

    def grab_suit(self):
        return self.suit

    def grab_rank(self):
        return self.value

    def draw(self):
        print(self.suit + self.value)


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

    def calculate_value(self):

        if self.ace is True and self.game_points < 12:
            return self.game_points + 10
        else:
            return self.game_points

    def draw(self, hidden):
        if hidden is True and playing is True:
            # Don't show first hidden card
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card, len(self.cards)):
            self.cards[x].draw()


class PlayingDeck():
    def __init__(self):
        self.deck = []
        for suit in cards_symbols:
            for card in all_cards:
                self.deck.append(Cards(suit, card))

        print(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        hit_card = self.deck.pop()
        return hit_card

    def __str__(self):
        deck_comp = " "
        for card in self.deck:
            deck_comp += " " + deck_comp.__str__()

        return "The deck has " + deck_comp


def make_bet():
    global bet
    bet = 0
    print('What amount of chips would you like to bet? (Please enter whole integer) ')

    while bet == 0:

        bet_comp = input()
        bet_comp = int(bet_comp)

        # Check to make sure the bet is within the remaining amount of chips left
        if 1 <= bet_comp <= chip_pool:
            bet = bet_comp
        else:
            print("Invalid bet, you only have " + str(chip_pool) + " remaining")


def deal_cards():
    global result, playing, deck, player_hand, dealer_hand, chip_pool, bet

    game_deck = PlayingDeck()

    game_deck.shuffle()
    print(game_deck.deck)
    test = input()
    make_bet()

    player_hand = Hand()
    dealer_hand = Hand()

    player_hand.hit(game_deck.deal())
    player_hand.hit(game_deck.deal())

    result = "Hit or Stand? Press h for hit or s for stand: "

    if playing is True:
        print('Fold, Sorry')
        chip_pool -= bet

    playing = True
    game_step()


def hit():
    global playing, chip_pool, deck, player_hand, dealer_hand, result, bet

    if playing is True:
        if player_hand.calculate_value() <= 21:
            player_hand.hit(PlayingDeck.deal())

        print("Player hand is %s" % player_hand)

        if player_hand.calculate_value() > 21:
            result = 'Busted!' + restart_phrase

            chip_pool -= bet
            playing = False

    else:
        result = "Sorry, can't hit" + restart_phrase

    game_step()


def stand():
    global playing, chip_pool, deck, player_hand, dealer_hand, result, bet

    '''This function plays the dealers hand, since stand was chosen'''

    if playing is False:
        if player_hand.calculate_value() > 0:
            result = "Sorry, you can't stand!"

    else:

        while dealer_hand.calculate_value() < 17:
            dealer_hand.card_add(PlayingDeck.deal())

        if dealer_hand.calculate_value() > 21:
            result = 'Dealer busts! You win! ' + restart_phrase

            chip_pool += bet
            playing = False

        elif dealer_hand.calculate_value() < player_hand.calculate_value():
            result = 'You beat the dealer, you win! ' + restart_phrase
            chip_pool += bet
            playing = False

        elif dealer_hand.calculate_value == player_hand.calculate_value():
            result = 'Tied up, push!' + restart_phrase
            playing = False

        else:
            result = 'Dealer Wins! ' + restart_phrase
            chip_pool -= bet
            playing = False

    game_step()


def game_step():

    print("")
    print('Player Hand is: ', player_hand.draw(hidden=False))

    print('')
    print('Player hand total is: ' + str(player_hand.calculate_value()))

    print('')
    print('Dealer Hand is: ', dealer_hand.draw(hidden=True))

    if playing is False:
        print(" --- for a total of " + str(dealer_hand.calculate_value()))
        print("Chip Total: " + str(chip_pool))

    else:
        print(" with another card hidden upside down")

    print('')
    print(result)

    player_input()


def game_exit():
    print('Thanks for playing!')
    exit()


def player_input():
    plin = input().lower()

    if plin == 'h':
        hit()
    elif plin == 's':
        stand()
    elif plin == 'd':
        deal_cards()
    elif plin == 'q':
        game_exit()
    else:
        print("Invalid Input. Enter h, s, d, or q: ")
        player_input()


def intro():
    statement = '''Welcome to BlackJack! Get as close to 21 as you can without getting over! 
Dealer hits until she reaches 17. Aces count as 1 or 11. Card output goes a letter followed by a number of face notation. '''
    print(statement)


if __name__ == "__main__":

    deck = PlayingDeck()
    deck.shuffle()
    player_hand = Hand()
    deal_hand = Hand()

    intro()
    deal_cards()
