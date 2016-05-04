import pygame


class Text:
    def __init__(self, size, text, coords, color_surface=(1, 50, 32), color_text=(0, 0, 0)):
        self.font = pygame.font.Font('freesansbold.ttf', size)
        self.text = text
        self.color_surface = color_surface
        self.color_text = color_text
        self.surface = self.font.render(self.text, True, self.color_text, self.color_surface)
        self.rect_surface = self.surface.get_rect()
        self.rect_surface.center = coords

    @property
    def get_surface(self):
        return self.surface

    @property
    def get_coords(self):
        return self.rect_surface.center
