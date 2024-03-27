import turtle as t

x1, y1, x2, y2 = map(float, input('Введите координаты 1 прямоугольника: ').split())
x3, y3, x4, y4 = map(float, input('Введите координаты 2 прямоугольника: ').split())


def rectangle(upper_x, upper_y, lower_x, lower_y):
    '''
    Function, drawing rectangle.
    :param upper_x: upper left coordinate on OX
    :param upper_y: upper left coordinate on OY
    :param lower_x: lower right coordinate on OX
    :param lower_y: lower right coordinate on OY
    :return: None
    '''

    t.up()
    t.setposition(upper_x, upper_y)
    t.down()
    for i in range(2):
        t.forward(lower_x - upper_x)
        t.right(90)
        t.forward(upper_y - lower_y)
        t.right(90)


rectangle(x1, y1, x2, y2)
rectangle(x3, y3, x4, y4)

if y2 > y3 or y4 > y1 or x2 < x3 or x4 < x1:
    print('Прямоугольники лежат вне друг друга, не касаясь')
elif y1 > y3 and y4 > y2 and x1 < x3 and x4 < x2 or y3 > y1 and y2 > y4 and x3 < x1 and x2 < x4:
    print('Один прямоугольник лежит внутри другого, не касаясь')
elif len({y1, y2, y3, y4}) < 4 or len({x1, x2, x3, x4}) < 4:
    print('Прямоугольники имеют касание')
else:
    print('Прямоугольники имеют пересечение')
