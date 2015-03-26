from Player import *
from DiscardPile import *


class ONE():
    """ Controller class, preps and starts the game. """
    initCards = 7

    def __init__(self):
        # Create all objects necessary for the game.
        self.deck = Deck()
        self.discard_pile = DiscardPile(self.deck.deal_one_card())

        self.players = []
        self.n_players = 0
        self.curr_player = 0

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

        # Game Loop
        while not self.stop_criterion():
            # Easier to read temp vars
            player = self.players[self.curr_player]
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
            while player.can_play_card(top_card):
                playable = []
                print "You can play these cards: "
                for i in range(0, len(player)):
                    if player[i].check_card(top_card):
                        print player[i],
                        playable += [player[i]]

                opt = raw_input("\n\n>>Play? (Y/N): ")

                # Player has chosen to not play any cards, if the has not
                # played, he is forced to draw a card from the deck.
                if opt.lower() == "n" and not has_played:
                    print "You choose to skip"
                    card = self.deck.deal_one_card()
                    player.enqueue(card)
                    print "You draw a card from the deck:", card
                    has_drawn = True
                    break
                # if he has played before choosing to stop playing, his turn
                # simply ends and he doesn't have to draw a card.
                elif opt.lower() == "n" and has_played:
                    print "You choose to end your turn."
                    break

                # Player has chosen to play one of his cards, put it ontop of the
                # discard pile, and then check for any special effects.
                elif opt.lower() == "y":
                    played_card = player.play_a_card(top_card)
                    print "\nYou play", played_card
                    self.discard_pile.push(played_card)

                    # Special Cards
                    if type(played_card) == SpecialCard:
                        if played_card.get_special() == SpecialCard.SKIP:
                            self.skip += 1
                        if played_card.get_special() == SpecialCard.REVERSE:
                            self.reverse = not self.reverse

                    # Played flag
                    has_played = True

                else:
                    print "Incorrect prompt"
            # End while can play card

            # After the player's actions, a few more rules apply, if he has played,
            # he is told his turn has ended.
            # If he has not played, AND he has not drawn, he is forced to draw.
            # NOTE: The last block of code is rendered useless by the made up rule
            # to force a player to keep drawing until he can play.
            if has_played:
                print "You can't play more cards, your turn ends."
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

    def stop_criterion(self):
        """Returns true if the game should be stopped and the winner announced"""
        for player in self.players:
            if len(player) == 0:
                self.announce_champion(player)
                return True

        return False

    def change_turn(self):
        """ Changes the turn, takes into account the reverse status to change in one
        direction or the other."""
        if not self.reverse:
            self.curr_player = (self.curr_player + 1) % self.n_players
        else:
            self.curr_player = (self.curr_player - 1) % self.n_players

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


start()

