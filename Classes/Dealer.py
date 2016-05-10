from Classes.Hand import Hand
from my_events import *
from Classes.Text import Text


class Dealer:
    def __init__(self, position):
        self.hand = Hand()
        self.pos = position  # Позиция следующей карты
        self.standard_pos = position
        self.score = 0
        self.deck = None

    def add_cards(self, deck):
        # Добавляет карты дилеру, пока сумма очков карт не превысит 17
        while self.score < 17:
            self.hand.add_card(deck.deal_card(), self.pos)
            self.score = self.hand.get_value()
            self.pos = [self.pos[0]+20, self.pos[1]+0]

    def render(self, screen):
        self.hand.render(screen)
        screen.blit(self.text_score.get_surface, self.text_score.get_coords)
        screen.blit(self.text_name.get_surface, self.text_name.get_coords)

    def event(self, event):
        if event.type == DEALER_ADD_CARDS:
            self.add_cards(self.deck)

    def set_deck(self, deck):
        self.deck = deck

    def get_score(self):
        # Возвращает очки
        return self.score

    def clean_hand(self):
        self.hand = Hand()
        self.score = 0
        self.pos = self.standard_pos

    @property
    def text_score(self):
        dx = 50
        return Text(12, "21/{}".format(self.score), (self.standard_pos[0] - dx, self.standard_pos[1]))

    @property
    def text_name(self):
        dx = 90
        dy = 60
        return Text(14, 'Dealer', (self.standard_pos[0] + dx, self.standard_pos[1] - dy))


