from Classes.Chip import Chip
import pygame


class ChipsWindow:
    def __init__(self):
            self.screen = pygame.Surface((135, 380))
            self.chips = [
                Chip('chip1.png', (1, 1), 1, 1),
                Chip('chip5.png', (1, 60), 5, 2),
                Chip('chip10.png', (1, 120), 10, 1),
                Chip('chip25.png', (1, 180), 1, 5),
                Chip('chip100.png', (1, 240), 1, 1),
                Chip('chip1000.png', (1, 300), 1, 1),
            ]
            self.chips[0].number += 10

    def count_chips(self, bankroll):
        # Подсчитывает кол-во фишек у игрока
        count_1 = bankroll % 10 % 5
        count_5 = bankroll % 10 // 5
        count_10 = bankroll % 100 % 25 // 10
        count_25 = bankroll % 100 // 25
        count_100 = bankroll % 1000 // 100
        count_1000 = bankroll // 1000
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