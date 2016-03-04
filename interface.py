import pygame
import sys
import time
from utilites import load_image
from Deck import Deck
from Hand import Hand
from Text import Text
from pgu import gui


class GuiWindow:
    def __init__(self):
        self.rect = pygame.Rect((600, 330, 175, 100))
        self.app = app = gui.App()
        self.click = 0

        def click_hit():
            clicked_button = 1
            window.clicked_button(clicked_button)
            print('1')
        button_hit_me = gui.Button('Hit me')
        button_hit_me.connect(gui.CLICK, click_hit)

        def click_enough():
            clicked_button = 2
            window.clicked_button(clicked_button)
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

    def clicked_button(self, clicked_button):
        self.click = clicked_button

    def paint(self):
        self.app.paint()


pygame.init()
pygame.font.init()
pygame.display.set_mode((800, 600))
pygame.display.set_caption("Blackjack")
screen = pygame.display.get_surface()
window = GuiWindow()


# Карты
player_hand = Hand()
dealer_hand = Hand()
coord_player = [254, 350]
coord_dealer = [250, 110]
deck = Deck()
shirt_card = load_image('Images/cards', 'back.png', 1)

# Очки
score_player = 0
score_dealer = 0

# Текст
dealer_text = Text(14, 'Dealer', (400, 50))
player_text = Text(14, 'Player', (400, 550))
# player_score_text = Text(12, "0/21", (220, 350))
# dealer_score = Text(12, '5/21', (220, 110))

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

    if window.click == 1:
        # Если нажата кнопка hit me, игроку добавляют ещё одну случайную карту
        player_hand.add_card(deck.deal_card(), coord_player)
        coord_player = [coord_player[0]+20, coord_player[1]+0]
        # score_player = sum(map(lambda card: card[0].card_value(), player_cards)) # подсчитывает очки у игрока
        score_player = player_hand.get_value()
        window.click = 0
    if window.click == 2:
        while score_dealer < 17:
            dealer_hand.add_card(deck.deal_card(), coord_dealer)
            score_dealer = dealer_hand.get_value()
            coord_dealer = [coord_dealer[0]+20, coord_dealer[1]+0]
        window.click = 0

    screen.fill((1, 50, 32))
    # Выводит текст на экран
    screen.blit(dealer_text.get_surface, dealer_text.get_coords)
    screen.blit(player_text.get_surface, player_text.get_coords)

    screen.blit(Text(12, "%s/21" % score_dealer, (220, 110)).get_surface,
                Text(12, "%s/21" % score_dealer, (220, 110)).get_coords)

    screen.blit(Text(12, "%s/21" % score_player, (220, 350)).get_surface,
                Text(12, "%s/21" % score_player, (220, 350)).get_coords)

    # Отрисока карт
    player_hand.render(screen)
    screen.blit(shirt_card, (650, 110))
    dealer_hand.render(screen)

    window.paint()
    pygame.display.flip()
