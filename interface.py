import pygame
import sys
import os
from Text import Text
from pgu import gui


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


def load_image(path, name, alpha_channel):
    fullname = os.path.join(path, name)  # Указываем путь к папке с картинками
    image = pygame.image.load(fullname)  # Загружаем картинку и сохраняем поверхность (Surface)
    if alpha_channel:
        image = image.convert_alpha()
    else:
        image = image.convert()

    return image


pygame.init()
pygame.font.init()
pygame.display.set_mode((800, 600))
pygame.display.set_caption("Blackjack")
screen = pygame.display.get_surface()
window = GuiWindow()

# # Кнопки
# hit_me = load_image('Images', 'button-9096.png', 1)
# enough = load_image('Images', 'button-9267.png', 1)

# Карты
image_card_1 = load_image('Images/cards', 's8.png', 1)
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
    screen.blit(image_card_1, (250, 350))
    screen.blit(image_card_2, (250, 110))
    screen.blit(shirt_card, (650, 110))
    if window.click == 1:
        screen.blit(load_image('Images/cards', 's6.png', 1), (270, 350))
    if window.click == 2:
        sys.exit()

    window.paint()
    pygame.display.flip()
