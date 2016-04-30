import pygame
from Classes.Text import Text


class StatusWindow:
    def __init__(self):
        self.screen = pygame.Surface((265, 100))
        self.rect = self.screen.get_rect()
        self.stat = None

    def render(self, screen):
        self.screen.fill((106, 90, 205))
        screen.blit(self.screen, (265, 215))
        screen.blit(self.text.get_surface, self.text.get_coords)

    @property
    def text(self, status=1):
        if status:
            self.stat = 'Win'
        if not status:
            self.stat = 'Lose'
        return Text(14, 'You {}!'.format(self.stat), self.rect.center)
