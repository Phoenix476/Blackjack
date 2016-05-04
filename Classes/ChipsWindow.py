from Classes.Chip import Chip
import pygame


class ChipsWindow:
    def __init__(self, bankroll=2000):
            self.screen = pygame.Surface((135, 380))
            self.bankroll = bankroll
            self.number_chips = self.count_chips()
            self.chips = [
                Chip(pos=(1, 1), value=1, number=self.number_chips[0]),
                Chip(pos=(1, 60), value=5, number=self.number_chips[1]),
                Chip(pos=(1, 120), value=10, number=self.number_chips[2]),
                Chip(pos=(1, 180), value=25, number=self.number_chips[3]),
                Chip(pos=(1, 240), value=100, number=self.number_chips[4]),
                Chip(pos=(1, 300), value=1000, number=self.number_chips[5]),
            ]

    def count_chips(self):
        # Подсчитывает кол-во фишек у игрока на начало игры
        count_1 = self.bankroll % 10 % 5
        count_5 = self.bankroll % 10 // 5
        count_10 = self.bankroll % 100 % 25 // 10
        count_25 = self.bankroll % 100 // 25
        count_100 = self.bankroll % 1000 // 100
        count_1000 = self.bankroll // 1000
        return count_1, count_5, count_10, count_25, count_100, count_1000

    def update(self, count):
        count = count
        for chip in self.chips:
            self.chips[self.chips.index(chip)].number = count[self.chips.index(chip)]

    def render(self, screen):
        self.screen.fill((1, 50, 32))
        # Отображение фишек
        for chip in self.chips:
            chip.render(self.screen)
        screen.blit(self.screen, (5, 80))