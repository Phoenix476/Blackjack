import pygame
from pygame import *
from Classes.Text import Text
from my_events import *


class StatusWindow:
    def __init__(self, cb):
        self.surface = pygame.Surface((265, 100))
        self.rect = self.surface.get_rect()
        self.stat = None
        self.cb = cb

    def render(self, screen):
        self.surface.fill((106, 90, 205))
        self.surface.blit(self.text.get_surface, self.text.get_coords)
        self.surface.blit(self.text_continue.get_surface, self.text_continue.get_coords)
        self.draw()
        screen.blit(self.surface, (265, 215))

    def set_status(self, status):
        if status == 1:
            self.stat = 'win'
        if status == 0:
            self.stat = 'lose'

    def draw(self):
        width = 15
        pygame.draw.lines(self.surface, (0, 0, 0), False, [(0, 0), (0, 99),
                                                                 (264, 99), (264, 0), (0, 0)], width)

    def event(self, event):
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            self.on_click()

    def on_click(self):
        self.cb()

    @property
    def text(self):
        dx = 60
        dy = 20
        return Text(30, 'You {}!'.format(self.stat),
                    (self.rect.center[0] - dx, self.rect.center[1] - dy),
                    color_surface=(106, 90, 205))

    @property
    def text_continue(self):
        dx = 110
        dy = 10
        return Text(16, 'Please click to continue game',
                    (self.rect.center[0] - dx, self.rect.center[1] + dy),
                    color_surface=(106, 90, 205))


if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Blackjack")
    screen = pygame.display.get_surface()

    def a():
        return

    window = StatusWindow(a)
    window.set_status(1)
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            window.event(e)
        window.render(screen)
        pygame.display.flip()
