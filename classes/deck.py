from .card import Card
import random


class Deck:
    def __init__(self):
        self.cards = []


    def create_deck(self):
        for i in range(2, 15):
            for t in ['H', 'D', 'S', 'C']:
                self.cards.append(Card(i, t))
                

    def rand_deck(self):
        for _ in range(1000):
            i = random.randint(0, 51)
            j = random.randint(0, 51)
            while i == j:
                j = random.randint(0, 51)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]


    def initial_deck(self):
        self.cards = []
        self.create_deck()
        self.rand_deck()
    