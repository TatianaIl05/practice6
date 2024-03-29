cell_1, cell_2 = input('Введите номера клеток: ').split('-')

match abs(int(cell_1[0], 16) - int(cell_2[0], 16)):
    case 2:
        if abs(int(cell_1[1]) - int(cell_2[1])) == 1:
            print('верно')
        else:
            print('ошибка')
    case 1:
        if abs(int(cell_1[1]) - int(cell_2[1])) == 2:
            print('верно')
        else:
            print('ошибка')
    case _:
        print('ошибка')