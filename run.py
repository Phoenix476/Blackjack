import pygame
import sys
import random

pygame.init()
pygame.display.set_mode((800, 600))
screen = pygame.display.get_surface()
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()