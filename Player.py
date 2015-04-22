from adt.LinkedPriorityQueue import *
from Card import *

class Player(LinkedPriorityQueue):
    """ Class representing a Player inside the game. Holds a hand of cards, using a PriorityQueue
    implementation to sort them. """

    def __init__(self, name, cards):
        # Init the PQueue
        LinkedPriorityQueue.__init__(self)

        self.__name = name

        for card in cards:
            self.enqueue(card)

    def __str__(self):
        string = self.__name + ", Cards[ "
        for card in self: string += str(card) + " "
        string += "]"

        return string

    def select_card(self, n):
        for card in self.__cards:
            if card.getNumer() == n: return card

    def can_play_card(self, target_card):
        """Returns true if the player can play a card over the given one"""
        for card in self:
            if card.check_card(target_card): return True
        return False

    def play_a_card(self, target_card):
        """Plays one of the compatible cards on hand"""
        played_card = None
        for card in self:
            if card.check_card(target_card):
                played_card = card
                break
        self.remove(played_card)
        return played_card

    @staticmethod
    def test():
        """ Unit test for the Player class. """
        card = Card.random_card()
        cards = [Card.random_card(), Card.random_card(), Card.random_card()]

        p1 = Player("John Doe", cards)
        print p1

        print "Can he play " + str(card) + "?:", p1.can_play_card(card)
        if p1.can_play_card(card):
            p1.play_a_card(card)

        print p1