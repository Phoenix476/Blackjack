from random import shuffle
from utilites import load_image
from Classes.Card import Card


class Deck:
    def __init__(self, pos):
        # ранги
        self.ranks = "23456789tjqka"
        # масти
        self.suits = "dchs"
        # генератор списков создающий колоду из 52 карт
        self.cards = [Card(r, s) for r in self.ranks for s in self.suits]
        # перетасовываем колоду. Не забудьте импортировать функцию shuffle из модуля random
        self.image = load_image('Images/cards', 'back.png', 1)
        self.pos = pos
        shuffle(self.cards)

    def deal_card(self):
        """ Функция сдачи карты """
        return self.cards.pop()

    def new_deck(self):
        self.cards = [Card(r, s) for r in self.ranks for s in self.suits]
        shuffle(self.cards)

    def render(self, screen):
        screen.blit(self.image, self.pos)
