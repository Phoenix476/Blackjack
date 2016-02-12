from Hand import Hand
from Deck import Deck


def new_game():
    # создаем колоду
    d = Deck()
    # задаем "руки" для игрока и дилера
    player_hand = Hand("Player")
    dealer_hand = Hand("Dealer")
    # сдаем две карты игроку
    player_hand.add_card(d.deal_card())
    player_hand.add_card(d.deal_card())
    # сдаем одну карту дилеру
    dealer_hand.add_card(d.deal_card())
    print(dealer_hand)
    print("="*20)
    print(player_hand)
    # Флаг проверки необходимости продолжать игру
    in_game = True
    # набирать карты игроку имеет смысл только если у него на руке меньше 21 очка
    while player_hand.get_value() < 21:
        ans = input("Hit or stand? (h/s) ")
        if ans == "h":
            player_hand.add_card(d.deal_card())
            print(player_hand)
            # Если у игрока перебор - дилеру нет смысла набирать карты
            if player_hand.get_value() > 21:
                print("You lose")
                in_game = False
        else:
            print("You stand!")
            break
    print("=" * 20)
    if in_game:
        # По правилам дилер обязан набирать карты пока его счет меньше 17
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(d.deal_card())
            print(dealer_hand)
            # Если у дилера перебор играть дальше нет смысла - игрок выиграл
            if dealer_hand.get_value() > 21:
                print("Dealer bust")
                in_game = False
    if in_game:
        # Ни у кого не было перебора - сравниваем количество очков у игрока и дилера.
        # В нашей версии если у дилера и игрока равное количество очков - выигрывает казино
        if player_hand.get_value() > dealer_hand.get_value():
            print("You win")
        else:
            print("Dealer win")

while True:
    new_game()
