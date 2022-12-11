import random
import task3
def create_username():
    print('Привет, это игра  конфетки')
    global player1, player2, player_in_list
    player1, player2 = input('Введите имя игрока '), input('Введите имя игрока ')
    player_in_list = [player1.capitalize(), player2.capitalize()]


def game( ):
    global count, maximum
    count = 0
    candy = int(input('Сколько конфет разыграем?'))
    maximum = int(input('Максимальное ко-во конфет за ход?'))

    while candy > 0:
        print(f'{player_in_list[count % 2]} твой ход!')
        actions = int(input())
        if actions > candy or actions > maximum:
            print(f'Ты взял слишком много конфет, попробуй еще раз')
            attempt = 3
            while attempt > 0:
                if candy >= actions <= maximum:
                    break
                print(f'Давай еще раз, у тебя осталось {attempt} попыток')
                actions = int(input())
                attempt -= 1
            else:
                return print(f'У тебя не осталось попыток ')

        candy -= actions
        if candy > 0:
            print(f'Осталось {candy} конфет')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return player_in_list[not count % 2]




create_username()

win = game()
if not win:
    print('Никто не выйграл')
else:
    print(f'Победитель {win}')
