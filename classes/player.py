import queue
from .card import Card


class Player:
    def __init__(self, player_name:str) -> None:
        self.player_name = player_name
        self.cards = queue.Queue()

    def initial_cards(self, cards:list) -> None:
        for card in cards:
            self.cards.put(card)

    def get_card(self) -> Card:
        return self.cards.get()

    def put_card(self, card:Card) -> None:
        self.cards.put(card)

    