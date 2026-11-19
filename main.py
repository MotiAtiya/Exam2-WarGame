from classes.game import Game
from classes.player import Player


player = Player("player")
computer = Player("computer")
game = Game(player, computer)

game.run()
