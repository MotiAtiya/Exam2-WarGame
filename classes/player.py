import queue

class Player:
    def __init__(self, player_name:str):
        self.player_name = player_name
        self.cards = queue.Queue()

    def initial_cards(self, cards:list):
        for card in cards:
            self.cards.put(card)

    