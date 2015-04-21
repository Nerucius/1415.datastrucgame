from adt.Stack import *
from Deck import *


class DiscardPile(Stack):
    """ Monton de cartas descartadas por los jugadores, la carta de encima del
    todo se usa para la siguiente jugada. """

    def __init__(self, init_card):
        # Init the Stack
        super(DiscardPile, self).__init__()

        self.push(init_card)

    def show_last_card(self):
        """Returns the top of the stack of Cards, without removing it"""
        return self.peek()

    def append(self, card):
        self.push(card)

    @staticmethod
    def test():
        deck = Deck()
        pile = DiscardPile(deck)

        print len(pile)
        print pile.show_last_card()

        pile.append(Card.random_card())
        print len(pile)
        print pile.show_last_card()