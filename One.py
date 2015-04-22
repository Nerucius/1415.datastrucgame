from Player import *
from DiscardPile import *
from adt.CircularDoubleLinkedList import *


class ONE():
    """ Controller class, preps and starts the game. """
    initCards = 7

    def __init__(self):
        # Create all objects necessary for the game.
        self.deck = Deck()
        self.discard_pile = DiscardPile(self.deck.deal_one_card())

        self.players = CircularDoubleLinkedList()
        self.n_players = 0

        # curr_player is the Node containing the player data inside the linkedlist
        self.curr_player = None

        self.skip = 0
        self.reverse = False

    def prepare_game(self):
        # Read input from player to initialize n number of players.
        self.n_players = input("Enter no. of players: ")

        for i in range(self.n_players):
            name = raw_input("Name: ")
            self.players.append(Player(name, self.deck.deal(ONE.initCards)))

    def run_game(self):
        """ The game Loop, keeps running itself while the game is ongoing, only stopping
        if the stop criterion is met. """
        self.curr_player = self.players.get_node(0)

        # Game Loop
        while not self.stop_criterion():
            # Easier to read temp vars
            player = self.curr_player.get_data()
            top_card = self.discard_pile.show_last_card()

            has_played = False
            has_drawn = False

            print "\n"
            print "---------------------------------"
            print "Now playing:", player
            print "Discard pile top:", top_card

            if self.skip > 0:
                self.skip -= 1
                print "\nYou have been skipped."
                raw_input("Press Enter to continue...")
                self.change_turn()
                continue

            # While the player can't play the top card, force him
            # to draw a card from the deck, until he can play
            while not player.can_play_card(top_card):
                print "You can't play any cards."
                card = self.deck.deal_one_card()
                player.enqueue(card)
                print "You draw a card from the deck:", card
                has_drawn = True

            # And now, while he is able to play, allow him to
            # choose whether to play or not, showing him a list
            # of cards the can play.
            # NOTE: the option to chose which one to play is not
            # implemented as it is not referred to in the
            # guidelines
            while player.can_play_card(self.discard_pile.show_last_card()):
                top_card = self.discard_pile.show_last_card()

                playable = ONE.get_playable(top_card, player)
                print ""

                chosen_card = ONE.choose_card(playable)

                # Player has chosen to not play any cards, if the has not
                # played, he is forced to draw a card from the deck.
                if not chosen_card and not has_played:
                    print "You choose to skip"
                    card = self.deck.deal_one_card()
                    player.enqueue(card)
                    print "You draw a card from the deck:", card
                    has_drawn = True
                    break
                # if he has played before choosing to stop playing, his turn
                # simply ends and he doesn't have to draw a card.
                elif not chosen_card and has_played:
                    print "You choose to end your turn."
                    break

                # Player has chosen to play one of his cards, put it ontop of the
                # discard pile, and then check for any special effects.
                elif chosen_card:
                    player.remove(chosen_card)
                    print "\nYou play", chosen_card
                    self.discard_pile.push(chosen_card)

                    # Special Cards
                    if chosen_card.is_special():
                        if chosen_card.get_special() == SpecialCard.SKIP:
                            self.skip += 1
                        if chosen_card.get_special() == SpecialCard.REVERSE:
                            self.reverse = not self.reverse

                    # Played flag
                    has_played = True
                    playable = ONE.get_playable(top_card, player)

                else:
                    print "Incorrect prompt"
            # End while can play card

            # After the player's actions, a few more rules apply, if he has played,
            # he is told his turn has ended.
            # If he has not played, AND he has not drawn, he is forced to draw.
            # NOTE: The last block of code is rendered useless by the made up rule
            # to force a player to keep drawing until he can play.
            if has_played and playable == []:
                print "You can't play more cards, your turn ends."
                raw_input("Press Enter to continue...")

            elif has_played and playable != []:
                print "You choose not to play more cards, your turn ends."
                raw_input("Press Enter to continue...")

            elif not has_drawn:
                print "You can't play any cards."
                card = self.deck.deal_one_card()
                player.enqueue(card)
                print "You draw a card from the deck:", card
                raw_input("Press Enter to continue...")

            # Changing the turn, the code for this is better left on a separate method.
            self.change_turn()

            # End While

    @staticmethod
    def get_playable(top_card, player):
        playable = []
        for i in range(0, len(player)):
            if player[i].check_card(top_card):
                playable += [player[i]]
        return playable

    @staticmethod
    def choose_card(card_list):
        # Display list of cards, starts at index 1
        i = 1
        print "Choose a card:"
        for card in card_list:
            print "\t%d) %s" %(i, card)
            i += 1
        print ""


        # Ask for user input, check bounds
        opt = 0
        index = opt - 1
        while index < 0 or index > len(card_list) - 1:
            opt = eval(raw_input(">>Card n.? (0 to skip turn): "))
            if opt == 0:
                return None
            index = opt - 1

        return card_list[index]

    def stop_criterion(self):
        """ Returns true if the game should be stopped and the winner announced. """
        for player in self.players:
            if len(player) == 0:
                self.announce_champion(player)
                return True

        return False

    def change_turn(self):
        """ Changes the turn, takes into account the reverse status to change in one
        direction or the other. """
        if not self.reverse:
            self.curr_player = self.curr_player.next()
        else:
            self.curr_player = self.curr_player.prev()

    @staticmethod
    def announce_champion(player):
        """Prints the champion"""
        print "====================================="
        print player.getName(), "Has won the game."
        print "====================================="
        pass


# Basic start method.
def start():
    game = ONE()
    game.prepare_game()
    game.run_game()


def test():
    deck = Deck()
    list = deck.deal(5)

    print ONE.choose_card(list)


if __name__ == "__main__":
    start()