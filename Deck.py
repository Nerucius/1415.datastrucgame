from random import shuffle

from adt.LinkedQueue import *
from SpecialCard import *


class Deck(LinkedQueue):
    """Clase que define el comportamiento de un mazo de cartas. Estructura de
    Stack, con capacidad de repartir cartas y devolver un elemento i"""

    def __init__(self):
        # Init the Queue
        LinkedQueue.__init__(self)

        # Init all 40 cards + 16 wildcards (2 of each type times 4 colors) 
        cards = []
        for n in range(0, 10):  # 0 to 9
            for color in range(0, 4):  # colors 0 to 3
                cards += [(Card(n, color))]

        for color in range(0, 4):
            for i in range(0, 2):
                cards += [SpecialCard(SpecialCard.SKIP, color)]
                cards += [SpecialCard(SpecialCard.REVERSE, color)]

        shuffle(cards)

        for card in cards:
            self.enqueue(card)

    def deal_one_card(self):
        return self.dequeue()

    def deal(self, n):
        dealtCards = []
        for i in range(0, n):
            dealtCards += [self.deal_one_card()]

        return dealtCards

    @staticmethod
    def test():
        deck = Deck()
        print "Deck: "
        print len(deck),
        for card in deck: print card,
        print "\n"

        print "Dealt 5 cards:"
        for card in deck.deal(5): print card,
        print "\n"

        print "Deck: "
        print len(deck),
        for card in deck: print card,