from Card import *


class SpecialCard(Card):
    # Special types:
    REVERSE = 0
    SKIP = 1
    PLUS_TWO = 2
    PLUS_FOUR = 3
    CHANGE_COLOR = 4

    def __init__(self, special, color):
        self._color = color
        self._number = -1

        self.__special = special

    def __str__(self):
        return "%s:%s" % (self.__special_to_string(), self._color_to_string())

    def is_special(self):
        return True;

    def get_special(self):
        return self.__special

    def __special_to_string(self):
        if self.get_special() == SpecialCard.REVERSE: return "Reverse"
        if self.get_special() == SpecialCard.SKIP: return "Skip"

    @staticmethod
    def random_card():
        return SpecialCard(randint(0, 1), randint(0, 3))

    @staticmethod
    def test():
        if randint(0, 1) == 1:
            c1 = SpecialCard.random_card()
        else:
            c1 = Card.random_card()

        if randint(0, 1) == 1:
            c2 = SpecialCard.random_card()
        else:
            c2 = Card.random_card()

        print c1, "y", c2, "son compatibles?:", c1.check_card(c2)
        print c1, "y", c2, "es mas grande c1?:", c1 >= c2        