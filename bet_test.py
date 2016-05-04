import pygame
import sys

from Classes.ChipsWindow import ChipsWindow


pygame.init()
pygame.font.init()
pygame.display.set_mode((800, 600))
pygame.display.set_caption("Test_bet")
screen = pygame.display.get_surface()

chips = ChipsWindow()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.KEYDOWN:  # Событие "Клавиша нажата"
            print('Key Down')
        if e.type == pygame.MOUSEBUTTONUP and e.button == 1:
            mX, mY = pygame.mouse.get_pos()
            print(mX, mY)

    screen.fill((1, 50, 32))

    chips.render(screen)

    pygame.display.flip()
