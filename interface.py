import sys
import pygame
from pgu import gui
from Player import Player
from Dealer import Dealer
from Deck import Deck
from Text import Text
from utilites import load_image

STOP = 0
MORE = 1
ENOUGH = 2
CHECK = 3


class GuiWindow:
    def __init__(self):
        self.rect = pygame.Rect((500, 330, 175, 100))
        self.app = app = gui.App()
        self.click = 0

        def click_hit():
            clicked_button = MORE
            window.clicked_button(clicked_button)
        button_hit_me = gui.Button('Hit me')
        button_hit_me.connect(gui.CLICK, click_hit)

        def click_enough():
            clicked_button = ENOUGH
            window.clicked_button(clicked_button)
        button_enough = gui.Button('Enough')
        button_enough.connect(gui.CLICK, click_enough)

        def click_check():
            clicked_button = CHECK
            window.clicked_button(clicked_button)
        button_check = gui.Button('Check')
        button_check.connect(gui.CLICK, click_check)

        tb = gui.Table()
        tb.tr()
        tb.td(button_hit_me)
        tb.tr()
        tb.td(button_enough)
        tb.tr()
        tb.td(button_check)
        app.init(widget=tb, screen=screen, area=self.rect)

    def event(self, event):
        self.app.event(event)

    def clicked_button(self, clicked_button):
        self.click = clicked_button

    def paint(self):
        self.app.paint()


def new_game(dealer, player, deck):
    # Начинает новую раздачу
    global window
    player.clean_hand()
    dealer.clean_hand()
    deck.new_deck()
    window.click = STOP


def count_chips(bankroll):
    # Подсчитывает кол-во фишек у игрока
    count_1 = bankroll % 10 % 5
    count_5 = bankroll % 10 // 5
    count_10 = bankroll % 100 % 25 // 10
    count_25 = bankroll % 100 // 25
    count_100 = bankroll % 1000 // 100
    count_1000 = bankroll // 1000
    return count_1, count_5, count_10, count_25, count_100, count_1000


pygame.init()
pygame.font.init()
pygame.display.set_mode((800, 600))
pygame.display.set_caption("Blackjack")
screen = pygame.display.get_surface()
window = GuiWindow()

# Позиции
pos_player = [254, 350]
pos_dealer = [254, 110]

in_game = True

losses = 0
winnings = 0

# Карты
player = Player(position=pos_player)
dealer = Dealer(position=pos_dealer)
deck = Deck()
shirt_card = load_image('Images/cards', 'back.png', 1)

bankroll = 4896
print('Кол-во фишек: 1 - %s, 5 - %s, 10 - %s, 25 - %s, 100 - %s, 1000 - %s' % count_chips(bankroll))

# Текст
dealer_text = Text(14, 'Dealer', (400, 50))
player_text = Text(14, 'Player', (400, 550))

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.KEYDOWN:  # Событие "Клавиша нажата"
            print('Key Down')
        if e.type == pygame.MOUSEBUTTONUP and e.button == 1:
            mX, mY = pygame.mouse.get_pos()
            print(mX, mY)
        window.event(e)

    if window.click == MORE:
            # Если нажата кнопка hit me, игроку добавляют ещё одну случайную карту
            player.update(deck)
            window.click = STOP

    if window.click == ENOUGH:
            # Если нажата кнопка enough, начинается раздача карт дилеру
            dealer.update(deck)
            window.click = STOP

    while window.click == CHECK:
        # Временная кнопка. При нажатии проверяет условия у дилера.
        if dealer.get_score() > 21:
            winnings += 1
            new_game(dealer, player, deck)
            break
        if dealer.get_score() < player.get_score():
            winnings += 1
            new_game(dealer, player, deck)
            break
        if dealer.get_score() > player.get_score():
            losses += 1
            new_game(dealer, player, deck)
            break
        if dealer.get_score() == player.get_score():
            losses += 1
            new_game(dealer, player, deck)
            break

    # FIXME: если с добавлением последней карты игроку очков становится больше, либо равно 21, последняя
    # добавленная карта у игрока не успевает отобразиться
    if player.get_score() == 21:
        winnings += 1
        new_game(dealer, player, deck)
    if player.get_score() > 21:
        losses += 1
        new_game(dealer, player, deck)

    screen.fill((1, 50, 32))
    # Выводит текст на экран
    screen.blit(dealer_text.get_surface, dealer_text.get_coords)
    screen.blit(player_text.get_surface, player_text.get_coords)

    # Вывод очков на экран
    screen.blit(Text(12, "%s/21" % dealer.get_score(), (220, 110)).get_surface,
                Text(12, "%s/21" % dealer.get_score(), (220, 110)).get_coords)

    screen.blit(Text(12, "%s/21" % player.get_score(), (220, 350)).get_surface,
                Text(12, "%s/21" % player.get_score(), (220, 350)).get_coords)

    # Вывод кол-ва побед и поражений
    screen.blit(Text(12, 'Выиграно раздач:%s' % winnings, (30, 570)).get_surface,
                Text(12, 'Выиграно раздач:%s' % winnings, (30, 570)).get_coords)

    screen.blit(Text(12, 'Проиграно раздач:%s' % losses, (30, 555)).get_surface,
                Text(12, 'Проиграно раздач:%s' % losses, (30, 555)).get_coords)

    # Ставки
    screen.blit(Text(12, 'Банкролл: %s$' % bankroll, (690, 570)).get_surface,
                Text(12, 'Банкролл: %s$' % bankroll, (690, 570)).get_coords)

    # screen.blit(Text(12, 'Проиграно раздач:%s' % losses, (30, 555)).get_surface,
    #             Text(12, 'Проиграно раздач:%s' % losses, (30, 555)).get_coords)

    # Отрисока карт
    player.render(screen)
    dealer.render(screen)
    screen.blit(shirt_card, (650, 110))

    window.paint()
    pygame.display.flip()
