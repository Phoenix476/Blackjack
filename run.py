import sys
import pygame
from pygame import *

from Classes.Dealer import Dealer
from Classes.Deck import Deck
from Classes.Player import Player
from Classes.ChipsWindow import ChipsWindow
from Classes.ChoiceForm import ChoiceForm
from Classes.StatusWindow import StatusWindow


def new_game(stat):
    status.set_status(stat)
    status.render(screen)
    clock = pygame.time.Clock()
    clock.tick(3)
    # 1 - выигрышь, 0 - проигрышь
    # Начинает новую раздачу
    player.clean_hand()
    dealer.clean_hand()
    deck.new_deck()
    player.add_card(deck)

pygame.init()
pygame.font.init()
pygame.display.set_mode((800, 600))
pygame.display.set_caption("Blackjack")
screen = pygame.display.get_surface()

# Позиции
pos_player = [254, 350]
pos_dealer = [254, 110]
pos_deck = [650, 110]

deck = Deck(pos_deck)

player = Player(pos_player)
player.set_deck(deck)

dealer = Dealer(pos_dealer)
dealer.set_deck(deck)

chips = ChipsWindow()
choice = ChoiceForm(screen)
status = StatusWindow(screen)

player.add_card(deck)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.KEYDOWN:  # Событие "Клавиша нажата"
            print('Key Down')
        if e.type == pygame.MOUSEBUTTONUP and e.button == 1:
            mX, mY = pygame.mouse.get_pos()
            print(mX, mY)
        choice.event(e)
        player.event(e)
        dealer.event(e)
        status.event(e)

    screen.fill((1, 50, 32))
    player.render(screen)
    dealer.render(screen)
    deck.render(screen)
    chips.render(screen)
    choice.paint()

    pygame.display.flip()

    if player.get_score() == 21:
        new_game(1)
    if player.get_score() > 21:
        new_game(0)
    if dealer.get_score() >= 17:
        print(dealer.get_score())
        if dealer.get_score() > 21:
            new_game(1)
        if dealer.get_score() == 21:
            new_game(0)
        if dealer.get_score() > player.get_score():
            new_game(0)
        if dealer.get_score() == player.get_score():
            new_game(0)
        if dealer.get_score() < player.get_score():
            new_game(1)