from random import randint


class Card(object):
    """ Class representing a single card in the game Uno. """

    # Class variables representing the 4 colors of card.
    RED = 0
    GREEN = 1
    YELLOW = 2
    BLUE = 3

    def __init__(self, number, color):
        # number and color are PROTECTED fields since SpecialCard needs access to them
        self._number = number
        self._color = color

    def __str__(self):
        return "%d:%s" % (self._number, self._color_to_string())

    def check_card(self, card):
        # A card is compatible if either the number or the color coincides

        # Polymorphism example, here first checks if both cards are special, if so, we are clear
        # to use the SpecialCard method getSpecial()
        if self.is_special() and card.is_special():
            return self.getSpecial() == card.get_special() or self.getColor() == card.getColor()
            #return self.getSpecial() == card.getSpecial()

        return self.getNumber() == card.getNumber() or self.getColor() == card.getColor()

    def getNumber(self):
        return self._number

    def getColor(self):
        return self._color

    def _color_to_string(self):
        if self.getColor() == Card.RED: return "Red"
        if self.getColor() == Card.GREEN: return "Green"
        if self.getColor() == Card.YELLOW: return "Yellow"
        if self.getColor() == Card.BLUE: return "Blue"
        return None

    def is_special(self):
        """ Method to be overridden by special cards extending this class. """
        return False;

    def __cmp__(self, obj):
        # Comparator overload so that PriorityQueue works

        # Orders first by number, then by color
        if self.getNumber() > obj.getNumber():
            return 1
        elif self.getNumber() == obj.getNumber():
            if self.getColor() > obj.getColor():
                return 1
            elif self.getColor() == obj.getColor():
                return 0
            else:
                return -1
        else:
            return -1

    @staticmethod
    def random_card():
        return Card(randint(0, 9), randint(0, 3))

    @staticmethod
    def test():
        """ Unit test for the Card class. """

        c1 = Card.random_card()
        c2 = Card.random_card()
        print c1, "y", c2, "son compatibles?:", c1.check_card(c2)

        print c1, "y", c2, "es mas grande c1?:", c1 >= c2

