def Privet():
    print("Привет!")
    print("Это игра крестики-нолики")
    print("Формат ввода: x y")
    print("х - это номер строки")
    print("y - это номер столбца")
    print("Вводите координаты через пробел ")

pole = [[' '] * 3 for i in range(3)]


def visual_pole():

    print("   "'0 1 2')
    for i in range(3):
        row = ' '.join(pole[i])
        print(f'{i}  {row}')

def vopros():
    while True:
        step = input("         Ваш ход: ").split()

        if len(step) != 2:
            print(" Введите две координаты! ")
            continue

        x, y = step

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if pole[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y

def step_win():
    win_step = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for step in win_step:
        signs = []
        for c in step:
            signs.append(pole[c[0]][c[1]])
        if signs == ["X", "X", "X"]:
            print("Выиграл X")
            return True
        if signs == ["0", "0", "0"]:
            print("Выиграл 0")
            return True
    return False


Privet()

number = 0

while True:
    number += 1
    visual_pole()
    if number % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = vopros()

    if number % 2 == 1:
        pole[x][y] = "X"
    else:
        pole[x][y] = "0"

    if step_win():
        break

    if number == 9:
        print(" Ничья!")
        break

