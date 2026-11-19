from .card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        for i in range(2, 14):
            for t in ['H', 'D', 'S', 'C']:
                self.cards.append(Card(i, t))
                
    