def start():
    guo_health = randint(200, 1000)
    qing_health= randint(200, 1000)
    current_player = ["qing", "guo"][randint(0, 1)]
    while True:
        hitorheal = input (f"qing vs guo ⚔: {current_player}'s turn: ")
        if (hitorheal == 'hit'):
            if (current_player == 'qing'):
                guo_health -= randint(50,80)
            else:
                qing_health -= randint(50,80)

            if guo_health < 0 or qing_health < 0:
                print('game over')
                break
        elif hitorheal == 'heal':
            if current_player == 'qing':
                qing_health += randint(50,60)
            else:
                guo_health += randint(50,60)
        if current_player == 'qing':
            current_player = 'guo'
        else:
            current_player = 'qing'
        print(f"guo: {guo_health} | qing: {qing_health}")
