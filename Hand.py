

class Hand(object):
    def __init__(self):
        # Изначально рука пустая
        self.cards = []

    def add_card(self, card, coord):
        """ Добавляет карту на руку """
        self.cards.append((card, coord))

    def get_value(self):
        """ Метод получения числа очков на руке """
        result = 0
        # Количество тузов на руке.
        aces = 0
        for card in self.cards:
            result += card[0].card_value()
            # Если на руке есть туз - увеличиваем количество тузов
            if card[0].get_rank() == "a":
                aces += 1
        # Решаем считать тузы за 1 очко или за 11
        if result + aces * 10 <= 21:
            result += aces * 10
        return result

    def render(self, screen):
        for card in self.cards:
            card[0].render(screen, card[1])

