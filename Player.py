from Hand import Hand


class Player:
    def __init__(self, position, name="no name"):
        self.name = name
        self.pos = position
        self.standard_pos = position
        self.hand = Hand()
        self.score = 0

    def update(self, deck):
        # Добавляет карту игроку, увеличивает кол-во очков
        self.hand.add_card(deck.deal_card(), self.pos)
        self.score = self.hand.get_value()
        self.pos = [self.pos[0]+20, self.pos[1]+0]

    def get_score(self):
        # Возвращает очки
        return self.score

    def render(self, screen):
        self.hand.render(screen)

    def clean_hand(self):
        self.hand = Hand()
        self.score = 0
        self.pos = self.standard_pos

