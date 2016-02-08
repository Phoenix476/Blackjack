class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank  # Ранг карты(Туз, король и т.д.)
        self.suit = suit  # Масть карты (черви, пики и т.д.)

    def card_value(self):
        # Возращает очки
        if self.rank in '10JQK':
            # По 10 за десятку, валета, даму и короля
            return 10
        else:
            # Возвращает нужное число очков за любую другую карту
            # Туз изначально дает одно очко.
            return " A23456789".index(self.rank)

    def get_rank(self):
        # Возвращает ранг карты
        return self.rank

    def __str__(self):
        # Выводит масть и ранг карты (print)
        return "%s%s" % (self.rank, self.suit)