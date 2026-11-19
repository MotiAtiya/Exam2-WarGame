from .player import Player
from .deck import Deck


class Game:
    def __init__(self, player:Player, computer:Player):
        self.player = player
        self.computer = computer

        self.deck = Deck()

    def run(self):
        print(self.deck)


