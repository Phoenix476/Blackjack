import pygame
from pgu import gui
from Functions.ParseOnChips import parse_on_chips

BET_MADE = 2
WIN = 1
LOSE = 0


class BetForm:
    # Окно для ввода ставок

    def __init__(self, screen, bankroll=2000):
        self.rect = pygame.Rect((10, 520, 300, 25))
        self.app = app = gui.App()
        self.bet = 0
        self.bankroll = bankroll
        self.number_chips = None
        self.status = None

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
        if self.status != BET_MADE:
            self.bet = self.input_bet.value
            self.input_bet.value = ''
            try:
                self.bet = int(self.bet)
            except ValueError:
                self.bet = 0
                print('Введите число')
                return
            if self.bet > self.bankroll:
                self.bet = 0
                print('Ставка должна быть меньше банкролла')
                return
            if self.bet == 0:
                print('Сделайте ставку')
            self.number_chips = list(parse_on_chips(self.bet))
            self.status = BET_MADE
        else:
            print('Ставка сделана, завершите игру, чтобы сделать новую стаку')

    def change_count_chips(self):
        if self.number_chips is not None:
            if self.status == WIN:
                self.number_chips = list(map(lambda x: x*2, self.number_chips))
            if self.status == LOSE:
                self.number_chips = list(map(lambda x: x*-1, self.number_chips))
        self.number_chips = None
        self.bet = None
        self.status = None

    def event(self, event):
        self.app.event(event)

    def paint(self):
        self.app.paint()
