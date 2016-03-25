import sys
import pygame
from pgu import gui
from Player import Player
from Dealer import Dealer
from Deck import Deck
from Text import Text
from utilites import load_image
import time

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
    global window
    player.clean_hand()
    dealer.clean_hand()
    deck.new_deck()
    window.click = STOP


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

    if player.get_score() == 21:
        winnings += 1
        # print('Выигрышей:%s' % winnings)
        new_game(dealer, player, deck)
    if player.get_score() > 21:
        losses += 1
        # print('Проигрышей:%s' % losses)
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

    screen.blit(Text(12, 'Проигано раздач:%s' % losses, (30, 555)).get_surface,
                Text(12, 'Проигано раздач:%s' % losses, (30, 555)).get_coords)

    # Отрисока карт
    player.render(screen)
    dealer.render(screen)
    screen.blit(shirt_card, (650, 110))

    window.paint()
    pygame.display.flip()
