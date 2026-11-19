from classes.game import Game
from classes.player import Player


player = Player("Player")
computer = Player("Computer")
game = Game(player, computer)

game.run()
