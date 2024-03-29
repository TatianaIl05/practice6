cell = input('Введите номер клетки: ')

match cell[0]:
    case 'b' | 'd' | 'f' | 'h':
        if int(cell[1]) % 2 == 0:
            print('чёрный')
        else:
            print('белый')
    case _:
        if int(cell[1]) % 2 == 0:
            print('белый')
        else:
            print('чёрный')
