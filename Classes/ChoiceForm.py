import pygame
from pgu import gui
from my_events import *


class ChoiceForm:
    def __init__(self, screen):
        self.rect = pygame.Rect((500, 330, 175, 100))
        self.app = app = gui.App()
        self.click = 0
        button_hit_me = gui.Button('Hit me')
        button_hit_me.connect(gui.CLICK, self.click_hit)
        button_enough = gui.Button('Enough')
        button_enough.connect(gui.CLICK, self.click_enough)
        tb = gui.Table()
        tb.tr()
        tb.td(button_hit_me)
        tb.tr()
        tb.td(button_enough)
        app.init(widget=tb, screen=screen, area=self.rect)

    def click_hit(self):
        new_Event = pygame.event.Event(PLAYER_ADD_CARD)
        pygame.event.post(new_Event)

    def click_enough(self):
        new_Event = pygame.event.Event(DEALER_ADD_CARDS)
        pygame.event.post(new_Event)

    def event(self, event):
        self.app.event(event)

    def clicked_button(self, clicked_button):
        self.click = clicked_button

    def paint(self):
        self.app.paint()
