import pygame
import sys
import os


def load_image(name, alpha_channel):
    fullname = os.path.join('Images', name)  # Указываем путь к папке с картинками

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
# Карты
image_card_1 = load_image('imgserver (1).png', 1)
# Шрифты
fontTextName = pygame.font.Font('freesansbold.ttf', 14)   # Шрифт имени игрока и дилера
fontTextScore = pygame.font.Font('freesansbold.ttf', 12)  # Шрифт очков
# -----------------------

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.KEYDOWN:  # Событие "Клавиша нажата"
            print('Key Down')
    # Дилер
    textSurfaceDealer = fontTextName.render('Dealer', True, (0, 0, 0), (1, 50, 32))
    textRectDealer = textSurfaceDealer.get_rect()
    textRectDealer.center = (400, 50)
    # ------------------------
    # Имя игрока
    textSurfacePlayer = fontTextName.render('Player', True, (0, 0, 0), (1, 50, 32))
    textRectPlayer = textSurfacePlayer.get_rect()
    textRectPlayer.center = (400, 550)
    # -------------------------
    # Очки Дилера
    textSurfaceScoreDealer = fontTextScore.render('5/21', True, (0, 0, 0), (1, 50, 32))
    textRectScoreDealer = textSurfaceScoreDealer.get_rect()
    textRectScoreDealer.center = (220, 150)
    # -------------------------
    # Очки Игрока
    textSurfaceScorePlayer = fontTextScore.render('8/21', True, (0, 0, 0), (1, 50, 32))
    textRectScorePlayer = textSurfaceScoreDealer.get_rect()
    textRectScorePlayer.center = (220, 350)

    screen.fill((1, 50, 32))
    # Выводит текст на экран
    screen.blit(textSurfaceScoreDealer, textRectScoreDealer)
    screen.blit(textSurfaceScorePlayer, textRectScorePlayer)
    screen.blit(textSurfaceDealer, textRectDealer)
    screen.blit(textSurfacePlayer, textRectPlayer)

    # Выводит карты на экран
    screen.blit(image_card_1, (250, 150))

    pygame.display.flip()
