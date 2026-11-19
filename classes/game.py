from .player import Player
from .deck import Deck
from .printer import Printer


class Game:
    def __init__(self, player:Player, computer:Player):
        self.player = player
        self.computer = computer
        self.deck = Deck()
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
        while self.player.cards.qsize() and self.computer.cards.qsize():
            self.play_turn()

