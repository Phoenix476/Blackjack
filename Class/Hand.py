class Hand(object):
    def __init__(self, name):
        # имя игрока
        self.name = name
        # Изначально рука пустая
        self.cards = []

    def add_card(self, card):
        """ Добавляет карту на руку """
        self.cards.append(card)

    def get_value(self):
        """ Метод получения числа очков на руке """
        result = 0
        # Количество тузов на руке.
        aces = 0
        for card in self.cards:
            result += card.card_value()
            # Если на руке есть туз - увеличиваем количество тузов
            if card.get_rank() == "A":
                aces += 1
        # Решаем считать тузы за 1 очко или за 11
        if result + aces * 10 <= 21:
            result += aces * 10
        return result

    def __str__(self):
        text = "%s's contains:\n" % self.name
        for card in self.cards:
            text += str(card) + " "
        text += "\nHand value: " + str(self.get_value())
        return text
