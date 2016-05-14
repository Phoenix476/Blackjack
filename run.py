import sys
import pygame
from pygame import *

from Classes.Dealer import Dealer
from Classes.Deck import Deck
from Classes.Player import Player
from Classes.ChipsWindow import ChipsWindow
from Classes.ChoiceForm import ChoiceForm
from Classes.StatusWindow import StatusWindow
from Classes.BetForm import BetForm


def end_game(stat):
    global window
    clock = pygame.time.Clock()
    clock.tick(0.5)
    window = StatusWindow(new_game)
    window.set_status(stat)
    # 1 - выигрышь, 0 - проигрышь
    bets.status = stat
    bets.change_bet()
    if bets.bet is not None:
        # chips.number_chips = list(map(lambda x, y: x+y, chips.number_chips, bets.number_chips))
        chips.bankroll += bets.bet
    chips.update()
    # bets.number_chips = None
    # chips.change_bankroll()
    bets.bankroll = chips.bankroll
    bets.bet = None


def new_game():
    global window
    # Начинает новую раздачу
    player.clean_hand()
    dealer.clean_hand()
    deck.new_deck()
    player.add_card(deck)
    window = None

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

bankroll = 3000

player = Player(pos_player)
player.set_deck(deck)

dealer = Dealer(pos_dealer)
dealer.set_deck(deck)

chips = ChipsWindow(bankroll)
choice = ChoiceForm(screen)
bets = BetForm(screen, bankroll)
window = None

player.add_card(deck)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        choice.event(e)
        bets.event(e)
        if bets.bet:
            # Пока игрок не сделал ставку, карты при нажатии кнопки не будут раздаваться
            player.event(e)
            dealer.event(e)
        if window:
            window.event(e)

    screen.fill((1, 50, 32))
    player.render(screen)
    dealer.render(screen)
    deck.render(screen)
    chips.render(screen)
    bets.paint()
    choice.paint()
    if window:
        window.render(screen)

    pygame.display.flip()

    if player.get_score() == 21:
        # Если у игрока блэк-джек (21 очко) - он выигрывает
        end_game(1)
    if player.get_score() > 21:
        # Если у игрока перебор - он проигрывает
        end_game(0)
    # if player.hand.cards[0].get_rank() == 'a' and player.hand.cards[1].get_rank() == 'a':
    #     # Если у игрока первые две карты - тузы, он автоматически выигрывает
    #     end_game(1)
    if dealer.get_score() >= 17:
        if dealer.get_score() > 21:
            # Если у дилера перебор - игрок выигрывает
            end_game(1)
        elif dealer.get_score() == 21:
            # Если у дилера блэк-джек (21 очко) - игрок проигрывает
            end_game(0)
        elif dealer.get_score() > player.get_score():
            # Если у дилера больше очков, чем у игрока - игрок проигрывает
            end_game(0)
        elif dealer.get_score() == player.get_score():
            # Если 'ровно' - игрок проигрывает
            end_game(0)
        elif dealer.get_score() < player.get_score():
            # Если у дилера меньше очков, чем у игрока - игрок выигрывает
            end_game(1)
