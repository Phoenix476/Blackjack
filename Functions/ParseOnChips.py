def parse_on_chips(bankroll):
    # Подсчитывает кол-во фишек с банкролла
    bankroll -= 1
    count_1 = (bankroll % 10 % 5)+1
    count_5 = bankroll % 10 // 5
    count_10 = bankroll % 100 % 25 // 10
    count_25 = bankroll % 100 // 25
    count_100 = bankroll % 1000 // 100
    count_1000 = bankroll // 1000
    return count_1, count_5, count_10, count_25, count_100, count_1000
