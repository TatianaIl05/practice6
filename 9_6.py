import turtle as t

x_center_1, y_center_1, radius_1 = map(float, input('Введите координаты центра и радиус первой окружности: ').split())
x_center_2, y_center_2, radius_2 = map(float, input('Введите координаты центра и радиус второй окружности: ').split())

t.up()
t.setposition(x_center_1, y_center_1 - radius_1)
t.down()
t.circle(radius_1)

t.up()
t.setposition(x_center_2, y_center_2 - radius_2)
t.down()
t.circle(radius_2)

t.up()
t.setposition(x_center_2, y_center_2)

if t.distance(x_center_1, y_center_1) > radius_1 + radius_2:
    print('Окружности лежат одна вне другой, не касаясь')
elif t.distance(x_center_1, y_center_1) == radius_1 + radius_2:
    print('Окружности имеют внешнее касание')
elif t.distance(x_center_1, y_center_1) == max(radius_1, radius_2) - min(radius_1, radius_2):
    print('Окружности имеет внутреннее касание')
elif t.distance(x_center_1, y_center_1) < max(radius_1, radius_2) - min(radius_1, radius_2):
    print('Одна окружность лежит внутри другой, не касаясь')
else:
    print('Окружности пересекаются')
