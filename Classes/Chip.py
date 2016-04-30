from utilites import load_image
from Classes.Text import Text


class Chip:
    def __init__(self, image, pos, value, number):
        self.image = load_image('Images/chips', image)
        self.pos = pos
        self.number = number
        self.value = value

    @property
    def text_image(self):
        h = self.image.get_rect().h
        w = self.image.get_rect().w
        dx = 5
        return Text(20, "x{}".format(self.number), (self.pos[0] + h + dx, self.pos[1] + w/3))

    def render(self, screen):
        screen.blit(self.image, self.pos)
        screen.blit(self.text_image.get_surface, self.text_image.get_coords)
