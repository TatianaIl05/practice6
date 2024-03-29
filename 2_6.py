hole_length, hole_width = map(float, input('Введите длину и ширину отверстия: ').split('x'))
brick_length, brick_width, brick_height = map(float, input('Введите длину, ширину и высоту кирпича: ').split('x'))

min_brick_1 = min(brick_length, min(brick_width, brick_height))
max_brick = max(brick_length, max(brick_width, brick_height))
min_brick_2 = brick_length + brick_width + brick_height - min_brick_1 - max_brick

if min_brick_1 <= min(hole_length, hole_width) and min_brick_2 <= max(hole_length, hole_width):
    print('да')
else:
    print('нет')
