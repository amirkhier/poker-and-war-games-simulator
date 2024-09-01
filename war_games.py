# Card Class
class Card:
    def __init__(self, val, suit):
        # Initialize val
        if not ((val >= 1) and (val <= 14)):
            raise ValueError('Sorry, The Number Should be Equal from 1 to 14...')
        self.val = val
        # Initialize suit:
        list1 = ['diamond', 'club', 'heart', 'spade', None]
        # if suit not equal to: 'diamond', 'club', 'heart', 'spade' , None
        # Check if suit doesn't have type None
        if suit != None:
            if suit.lower() not in list1:
                raise ValueError(f'Invalid suit, the suit should be equal to {list1}')
        # if suit is None and val is not 14
        if (suit == list1[4] and val != 14):
            # Logical message based on the example images on page 3 of the FINAL ASSIGNMENT PDF
            raise ValueError('If Suit is None, val must be 14')
        # if suit is not None and val equals 14
        # Check if suit doesn't have type None
        if suit != None:
            if ((suit != list1[4]) and (val == 14)):
                # Logical message based on the example images on page 3 of the FINAL ASSIGNMENT PDF
                raise ValueError('val 14 cannot have a not-None suit.')
        # Preserve suit
        # if suit is a string, else suit is None
        if suit == None:
            self.suit = suit
        else:
            self.suit = suit.lower()
        # define name in dictionary:
        name = {
            1: 'Ace', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
            11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Joker'
        }
        # Initialize name
        get_name = name[val]
        self.name = get_name

    def __repr__(self):
        # for joker
        if self.val == 14:
            return f"{self.name}!"
        else:
            # for the rest
            return f"{self.name} of {self.suit.capitalize()}s"

    def __lt__(self, other):
        return self.val < other.val

import random

class Deck:
    # Create an attribute list of 52 cards excluding Joker
    # Reminder: Two loops are needed to create 52 cards
    # One loop for the list of suits
    # And one for the list of 13 cards
    # Each 13 cards represent each of diamond, club, heart, spade
    # And 13 times 4 equals 52!!
    def __init__(self):
        list_card = []
        list_suit = ['diamond', 'club', 'heart', 'spade']
        # Create 52 cards
        for suit in list_suit:
            for val in range(1, 14):
                list_card.append(Card(val, suit))
        self.card_list = list_card
        random.shuffle(self.card_list)

    def draw_card(self):
        # if the list is empty
        if len(self.card_list) == 0:
            return None
        # remove card from the first element of the list
        else:
            removed_card = self.card_list[0]
            self.card_list.remove(removed_card)
            return removed_card

    def draw_multiple(self, num):
        removed_list = []
        if len(self.card_list) == 0:
            return None
        else:
            for i in range(num):
                removed_list.append(self.card_list[i])
            # removing first card nums in the second loop
            for i in range(len(removed_list)):
                self.card_list.remove(removed_list[i])
            return removed_list

    def shuffle(self):
        # Shuffle cards
        random.shuffle(self.card_list)

    def reset(self):
        self.__init__()
        # Reinitialize the list

    def __repr__(self):
        return f"A Deck Containing {len(self.card_list)} Cards"

    def __lt__(self, other):
        return len(self.card_list) < len(other.card_list)

# The class is a deck of cards containing two jokers, in addition to the rest of the cards.
# This means there are 54 cards: 52 non-joker cards and 2 joker cards.
# This means inheritance must be used; JokerDeck inherits from Deck
class JokerDeck(Deck):
    def __init__(self):
        super().__init__()
        # Add two Joker cards
        self.card_list.append(Card(14, None))
        self.card_list.append(Card(14, None))
        # After adding two Joker cards to the card list, shuffle the list
        random.shuffle(self.card_list)

# Initialize three parameters
# d1 - Deck of cards for the first player (deck1 for the first player)
# d2 - Deck of cards for the second player (deck2 for the second player)
# An empty list to which cards will be added to the pile and taken by the winning player each round (card_pile)

class Wargame:
    def __init__(self, has_joker):
        # Check if the value is not boolean
        if (has_joker != True) and (has_joker != False):
            raise TypeError('The value you input is not boolean...')
        # If both players want to play with decks including Jokers
        elif has_joker == True:
            self.d1 = JokerDeck()
            self.d2 = JokerDeck()

        # If both players do not want to play with decks including Jokers
        elif has_joker == False:
            self.d1 = Deck()
            self.d2 = Deck()

        self.card_pile = []

    def give_pile(self, player):
        if player == 1:
            self.d1.card_list.extend(self.card_pile)

        elif player == 2:
            self.d2.card_list.extend(self.card_pile)

        else:
            raise ValueError('Invalid Value Type...')

        self.card_pile = []

    def round(self, i):
        # Draw a card from each deck for each player
        player_draw_card_d1 = self.d1.draw_card()
        player_draw_card_d2 = self.d2.draw_card()
        # Print a string in the following format
        print(f"Round {i}: {player_draw_card_d1} vs {player_draw_card_d2}")
        # Add the two drawn cards to the pile
        self.card_pile.append(player_draw_card_d1)
        self.card_pile.append(player_draw_card_d2)
        # Determine which player won the round
        if player_draw_card_d1 > player_draw_card_d2:
            print('Player 1 Won\n')
            # The pile will be given to the first player
            self.give_pile(1)
        elif player_draw_card_d2 > player_draw_card_d1:
            print('Player 2 Won\n')
            # The pile will be given to the second player
            self.give_pile(2)
        # If there is a tie
        else:
            print('War!\n.\n.\n.\n ')
            # If one player's deck has fewer than three cards
            if (len(self.d1.card_list) < 3) or (len(self.d2.card_list) < 3):
                print('Not enough cards for a war...')
                self.d1.card_list = []
                self.d2.card_list = []
            else:
                self.card_pile.extend(self.d1.draw_multiple(3))
                self.card_pile.extend(self.d2.draw_multiple(3))

    def run_game(self):
        print('STARTING WAR...')
        i = 0
        # Start the game until one player's deck is empty
        while (len(self.d1.card_list) != 0) and (len(self.d2.card_list) != 0):
            # Start the game
            self.round(i)
            i += 1
        # If the second deck is empty, and the first deck is not
        if (len(self.d2.card_list) == 0) and (len(self.d1.card_list) != 0):
            print('PLAYER 1 IS THE VICTOR!')
        # If the first deck is empty, and the second deck is not
        elif (len(self.d1.card_list) == 0) and (len(self.d2.card_list) != 0):
            print('PLAYER 2 IS THE VICTOR!')
        # If both decks are empty simultaneously
        elif (len(self.d1.card_list) == 0) and (len(self.d2.card_list) == 0):
            print('IT\'S A TIE!')

# LimitedWarGame Class
class LimitedWarGame(Wargame):
    def __init__(self, has_joker=False, round=10000):
        super().__init__(has_joker)
        self.rounds = round
    # Question:
    # Consider which function from the original WarGame needs to be overridden in LimitedWarGame to limit the number of rounds? And what needs to be changed in it?
    # The answer is: run_game
    def run_game(self):
        print('STARTING WAR...')
        # Start the game until the end of the specified round
        # The change needed is instead of a loop stopping when one player's deck is empty,
        # Use a loop that runs until the defined ROUND is reached.
        for i in range(0, self.rounds):
            # Start the game
            self.round(i)

        # If the first deck is larger,
        if len(self.d2.card_list) < len(self.d1.card_list):
            print('PLAYER 1 IS THE VICTOR!')
        # If the second deck is larger
        elif len(self.d2.card_list) > len(self.d1.card_list):
            print('PLAYER 2 IS THE VICTOR!')
        # If they are equal
        else:
            print('IT\'S A TIE!')

# Tests for the classes
# Card Class Test:
# card = Card(5, 'bla') -> approved
# card = Card(16, 'heart') -> approved
# card = Card(14, 'heart') -> approved
# card = Card(7, None) -> approved

# Test:
# c1 = Card(5, 'heart')
# c2 = Card(14, None)
# c3 = Card(11, 'club')
# c4 = Card(6, 'club')
# c5 = Card(11, 'Spade')
# print(c1)
# print(c2)
# print(c3)
# print(c4)
# print(c5)
# print(c3 > c2)
# print(c1 < c2)
# print(c4 < c1)

# Deck Class Test:
# Test1
# d1 = Deck()
# print(d1)
# c1 = d1.draw_card()
# print(c1)
# cards = d1.draw_multiple(5)
# print(cards)
# print(d1)
# d1.reset()
# print(d1)

# Test2
# deck1 = Deck()
# deck2 = Deck()
# c = deck2.draw_card()
# print(deck1 > deck2)

# JokerDeck Test:
# j_d2 = JokerDeck()
# print(j_d2)
# c2 = j_d2.draw_card()
# print(c2)
# J_cards = j_d2.draw_multiple(5)
# print(J_cards)
# print(j_d2)
# j_d2.reset()
# print(j_d2)

# Test for constructor instance defined in Wargame class
# wargame1 = Wargame(True)
wargame2 = Wargame(False)
# print(wargame1)
# Game test
wargame2.run_game()

# Test LimitedWarGame
# limitedWarGame = LimitedWarGame(True, 250)
# Game test
# limitedWarGame.run_game()
