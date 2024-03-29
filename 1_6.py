radius = 6.5
length, width = map(float, input('Введите длину и ширину покрытия: ').split('x'))
if length**2 + width**2 <= 4*radius**2:
    print('да')
else:
    print('нет')
