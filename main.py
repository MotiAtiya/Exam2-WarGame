from classes.game import Game
from classes.player import Player
from classes.printer import Printer
from classes.user_input import UserInput


def main():
    player = Player("Player")
    computer = Player("Computer")
    game = Game(player, computer)

    menu = {
        1: "New game",
        2: "Exit"
    }

    start_new_game = True
    while start_new_game:
        Printer.display_menu(menu, "War Game")
        choice = UserInput.ask_choice(1,len(menu))
        if choice == 1:
            game.run()
        if choice == 2:
            start_new_game = False

    print("\nBye!\n")
        
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye!\n")
