from random import shuffle

from Classes.Card import Card


class Deck(object):
    def __init__(self):
        # ранги
        self.ranks = "23456789tjqka"
        # масти
        self.suits = "dchs"
        # генератор списков создающий колоду из 52 карт
        self.cards = [Card(r, s) for r in self.ranks for s in self.suits]
        # перетасовываем колоду. Не забудьте импортировать функцию shuffle из модуля random
        shuffle(self.cards)

    def deal_card(self):
        """ Функция сдачи карты """
        return self.cards.pop()

    def new_deck(self):
        self.cards = [Card(r, s) for r in self.ranks for s in self.suits]
        shuffle(self.cards)
