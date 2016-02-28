import pygame
import sys
import random
from utilites import load_image
from Card import Card
from Text import Text
from pgu import gui

SUITS = ('c', 's', 'd', 'h')
RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 't', 'j', 'q', 'k', 'a')


class GuiWindow:
    def __init__(self):
        self.rect = pygame.Rect((600, 330, 175, 100))
        self.app = app = gui.App()
        self.click = 0

        def click_hit():
            CLICKED_BUTTON = 1
            window.clicked_button(CLICKED_BUTTON)
            print('1')
        button_hit_me = gui.Button('Hit me')
        button_hit_me.connect(gui.CLICK, click_hit)

        def click_enough():
            CLICKED_BUTTON = 2
            window.clicked_button(CLICKED_BUTTON)
            print('2')
        button_enough = gui.Button('Enough')
        button_enough.connect(gui.CLICK, click_enough)

        tb = gui.Table()
        tb.tr()
        tb.td(button_hit_me)
        tb.tr()
        tb.td(button_enough)
        app.init(widget=tb, screen=screen, area=self.rect)

    def event(self, event):
        self.app.event(event)

    def clicked_button(self, CLICKED_BUTTON):
        self.click = CLICKED_BUTTON

    def paint(self):
        self.app.paint()


pygame.init()
pygame.font.init()
pygame.display.set_mode((800, 600))
pygame.display.set_caption("Blackjack")
screen = pygame.display.get_surface()
window = GuiWindow()


# Карты
deck = []
coords_player = [250, 350]
# image_card_1 = load_image('Images/cards', 's8.png', 1)
image_card_2 = load_image('Images/cards', 's5.png', 1)
shirt_card = load_image('Images/cards', 'back.png', 1)

# Текст
dealer_text = Text(14, 'Dealer', (400, 50))
player_text = Text(14, 'Player', (400, 550))
player_score = Text(12, "8/21", (220, 350))
dealer_score = Text(12, '5/21', (220, 110))

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

    screen.fill((1, 50, 32))
    # Выводит текст на экран
    screen.blit(dealer_text.get_surface, dealer_text.get_coords)
    screen.blit(player_text.get_surface, player_text.get_coords)
    screen.blit(dealer_score.get_surface, dealer_score.get_coords)
    screen.blit(player_score.get_surface, player_score.get_coords)

    # Карты
    for card in deck:
        card[0].render(screen, card[1])
    screen.blit(image_card_2, (250, 110))
    screen.blit(shirt_card, (650, 110))
    if window.click == 1:
        # Если нажата кнопка hit me, игроку добавляют ещё одну случайную карту
        deck.append((Card(suit=random.choice(SUITS), rank=random.choice(RANKS)), coords_player))
        coords_player = [coords_player[0]+20, coords_player[1]+0]
        window.click = 0
    if window.click == 2:
        sys.exit()

    window.paint()
    pygame.display.flip()
