from Classes.Chip import Chip
from Functions.ParseOnChips import parse_on_chips
from Classes.Text import Text
import pygame


class ChipsWindow:
    def __init__(self, bankroll=2000):
            self.screen = pygame.Surface((200, 450))
            self.bankroll = bankroll
            self.number_chips = list(parse_on_chips(self.bankroll))
            self.chips = [
                Chip(pos=(1, 1), value=1, number=self.number_chips[0]),
                Chip(pos=(1, 60), value=5, number=self.number_chips[1]),
                Chip(pos=(1, 120), value=10, number=self.number_chips[2]),
                Chip(pos=(1, 180), value=25, number=self.number_chips[3]),
                Chip(pos=(1, 240), value=100, number=self.number_chips[4]),
                Chip(pos=(1, 300), value=1000, number=self.number_chips[5]),
            ]

    def update(self):
        for chip in self.chips:
            self.chips[self.chips.index(chip)].number = self.number_chips[self.chips.index(chip)]

    def render(self, screen):
        self.screen.fill((1, 50, 32))
        # Отображение фишек
        for chip in self.chips:
            chip.render(self.screen)
        self.screen.blit(self.text_bankroll.get_surface, self.text_bankroll.get_coords)
        screen.blit(self.screen, (5, 80))

    def change_bankroll(self):
        self.bankroll = sum(list([chip.number * chip.value for chip in self.chips]))

    @property
    def text_bankroll(self):
        return Text(15, 'Bankroll: {}$'.format(self.bankroll), (1, 400))
