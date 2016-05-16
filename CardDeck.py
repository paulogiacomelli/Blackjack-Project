import itertools
import random

#defines a class. A blueprint for a object.
class CardDeck:

    #constructor
    def __init__(self):
        self.values = ['2','3','4','5','6','7','8','9','10','j','q','k','a']
        self.suite = ['c', 's', 'h', 'd']
        #joins values and suit into one item.  Stores in a list called deck.
        self.deck = tuple(''.join(card) for card in itertools.product(self.suite, self.values))
        #associated images with each card

        self.takenCards = []

    #define new methods for this class.

    '''
    draws a new card randomly from the deck
    '''
    def drawCard(self):
        print()








