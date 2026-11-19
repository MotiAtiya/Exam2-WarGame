from .player import Player
from .deck import Deck
from .printer import Printer
from .user_input import UserInput


class Game:
    def __init__(self, player:Player, computer:Player):
        self.player = player
        self.computer = computer
        self.deck = Deck()
        self.menu = {
            1: "Play turn",
            2: "Exit"
        }


    def initial_game(self):
        self.deck.initial_deck()
        self.player.initial_cards(self.deck.cards[:26])
        self.computer.initial_cards(self.deck.cards[26:])


    def _calculate_winner(self, player_card, computer_card):
        if player_card.card_value > computer_card.card_value:
            return "Player"
        elif player_card.card_value < computer_card.card_value:
            return "Computer"
        else:
            return None
        

    def _update_winner_cards(self, winner, player_card, computer_card):
        if winner == 'Player':
            self.player.put_card(player_card)
            self.player.put_card(computer_card)
        elif winner == 'Computer':
            self.computer.put_card(computer_card)
            self.computer.put_card(player_card)
        else:
            self.computer.put_card(computer_card)
            self.player.put_card(player_card)

    
    def play_turn(self):
        player_card = self.player.get_card()
        computer_card = self.computer.get_card()
        winner = self._calculate_winner(player_card, computer_card)
        self._update_winner_cards(winner, player_card, computer_card)
        Printer.display_round_result(player_card,
                                    computer_card,
                                    winner,
                                    self.player.cards.qsize(),
                                    self.computer.cards.qsize())
        

    def run(self):
        self.initial_game()
        Printer.claer_screen()

        continue_playing = True
        while continue_playing:
            Printer.display_menu(self.menu)
            choice = UserInput.ask_choice(1,len(self.menu))
            if choice == 1:
                self.play_turn()
            if choice == 2:
                continue_playing = False
