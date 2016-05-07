import pygame
from pgu import gui


class BetForm:
    # Окно для ввода ставок
    def __init__(self, screen):
        self.rect = pygame.Rect((10, 520, 300, 25))
        self.app = app = gui.App()
        self.bet = 0

        button_bet = gui.Button('Put')
        button_bet.connect(gui.CLICK, self.click_put)
        label = gui.Label('Bet: ')
        self.input_bet = gui.Input()
        tb = gui.Table()

        tb.tr()
        tb.td(label)
        tb.td(self.input_bet)
        tb.td(button_bet)

        app.init(widget=tb, screen=screen, area=self.rect)

    def click_put(self):
        self.bet = self.input_bet.value
        self.input_bet.value = ''
        try:
            self.bet = int(self.bet)
        except ValueError:
            print('Введите число')

    def event(self, event):
        self.app.event(event)

    def paint(self):
        self.app.paint()
