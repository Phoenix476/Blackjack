import pygame
from Classes.Text import Text
from my_events import *


class StatusWindow:
    def __init__(self, screen):
        self.screen = screen
        self.surface = pygame.Surface((265, 100))
        self.rect = self.surface.get_rect()
        self.stat = None

    def render(self, screen):
        self.surface.fill((106, 90, 205))
        self.surface.blit(self.text.get_surface, self.text.get_coords)
        screen.blit(self.surface, (265, 215))

    def set_status(self, status):
        if status == 11:
            self.stat = 'Win'
        if status == 10:
            self.stat = 'Lose'

    def event(self, event):
        if event.type == SHOW_STATUS:
            self.render(self.screen)

    @property
    def text(self):
        dx = 80
        dy = 20
        return Text(40, 'You {}!'.format(self.stat),
                    (self.rect.center[0] - dx, self.rect.center[1] - dy),
                    color_surface=(106, 90, 205))
