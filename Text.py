import pygame


class Text:
    def __init__(self, size, text, coords):
        self.font = pygame.font.Font('freesansbold.ttf', size)
        self.surface = self.font.render(text, True, (0, 0, 0), (1, 50, 32))
        self.rect_surface = self.surface.get_rect()
        self.rect_surface.center = coords

    @property
    def get_surface(self):
        return self.surface

    @property
    def get_coords(self):
        return self.rect_surface.center
