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
            return self.get_special() == card.get_special() or self.get_color() == card.get_color()
            #return self.getSpecial() == card.getSpecial()

        return self.get_numer() == card.get_numer() or self.get_color() == card.get_color()

    def get_numer(self):
        return self._number

    def get_color(self):
        return self._color

    def _color_to_string(self):
        if self.get_color() == Card.RED: return "Red"
        if self.get_color() == Card.GREEN: return "Green"
        if self.get_color() == Card.YELLOW: return "Yellow"
        if self.get_color() == Card.BLUE: return "Blue"
        return None

    def is_special(self):
        """ Method to be overridden by special cards extending this class. """
        return False

    def __cmp__(self, obj):
        # Comparator overload so that PriorityQueue works

        # Orders first by number, then by color
        if self.get_numer() > obj.get_numer():
            return 1
        elif self.get_numer() == obj.get_numer():
            if self.get_color() > obj.get_color():
                return 1
            elif self.get_color() == obj.get_color():
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

