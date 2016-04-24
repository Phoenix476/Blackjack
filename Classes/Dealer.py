from Classes.Hand import Hand


class Dealer:
    def __init__(self, position):
        self.hand = Hand()
        self.pos = position
        self.standard_pos = position
        self.score = 0

    def update(self, deck):
        # Добавляет карты дилеру, пока сумма очков карт не превысит 17
        while self.score < 17:
            self.hand.add_card(deck.deal_card(), self.pos)
            self.score = self.hand.get_value()
            self.pos = [self.pos[0]+20, self.pos[1]+0]

    def render(self, screen):
        for card in self.hand.cards:
            card[0].render(screen, card[1])

    def get_score(self):
        # Возвращает очки
        return self.score

    def clean_hand(self):
        self.hand = Hand()
        self.score = 0
        self.pos = self.standard_pos

