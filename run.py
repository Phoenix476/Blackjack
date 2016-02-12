import pygame
import sys
import os
from Text import Text


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
# Кнопки
hit_me = load_image('Images', 'button-9096.png', 1)
enough = load_image('Images', 'button-9267.png', 1)
# Карты
image_card_1 = load_image('Images/cards', 's8.png', 1)
image_card_2 = load_image('Images/cards', 's5.png', 1)
shirt_card = load_image('Images/cards', 'back.png', 1)

dealer_text = Text(14, 'Dealer', (400, 50))
player_text = Text(14, 'Player', (400, 550))
player_score = Text(12, "8/21", (220, 350))
dealer_score = Text(12, '5/21', (220, 110))
# Шрифты
# fontTextName = pygame.font.Font('freesansbold.ttf', 14)   # Шрифт имени игрока и дилера
# fontTextScore = pygame.font.Font('freesansbold.ttf', 12)  # Шрифт очков
# -----------------------

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.KEYDOWN:  # Событие "Клавиша нажата"
            print('Key Down')
    # # Дилер
    # textSurfaceDealer = fontTextName.render('Dealer', True, (0, 0, 0), (1, 50, 32))
    # textRectDealer = textSurfaceDealer.get_rect()
    # textRectDealer.center = (400, 50)
    # # ------------------------
    # # Имя игрока
    # textSurfacePlayer = fontTextName.render('Player', True, (0, 0, 0), (1, 50, 32))
    # textRectPlayer = textSurfacePlayer.get_rect()
    # textRectPlayer.center = (400, 550)
    # # -------------------------
    # # Очки Дилера
    # textSurfaceScoreDealer = fontTextScore.render('5/21', True, (0, 0, 0), (1, 50, 32))
    # textRectScoreDealer = textSurfaceScoreDealer.get_rect()
    # textRectScoreDealer.center = (220, 150)
    # # -------------------------
    # # Очки Игрока
    # textSurfaceScorePlayer = fontTextScore.render('8/21', True, (0, 0, 0), (1, 50, 32))
    # textRectScorePlayer = textSurfaceScoreDealer.get_rect()
    # textRectScorePlayer.center = (220, 350)

    screen.fill((1, 50, 32))
    # Выводит текст на экран
    screen.blit(dealer_text.get_surface, dealer_text.get_coords)
    screen.blit(player_text.get_surface, player_text.get_coords)
    screen.blit(dealer_score.get_surface, dealer_score.get_coords)
    screen.blit(player_score.get_surface, player_score.get_coords)

    # Выводит карты на экран
    # screen.blit(image_card_1, (250, 150))

    screen.blit(hit_me, (650, 400))
    screen.blit(enough, (650, 330))

    screen.blit(image_card_1, (250, 350))
    screen.blit(image_card_2, (250, 110))
    screen.blit(shirt_card, (650, 110))

    pygame.display.flip()
