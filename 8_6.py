import math

number_count = int(input('Введите номер цифры: '))

if number_count <= 10:
    print(number_count - 1)

elif 10 < number_count <= 190:
    if number_count % 2 == 1:
        print(math.ceil((number_count // 10) / 2))
    else:
        print(((number_count - 12) // 2) % 10)

elif 190 < number_count <= 490:
    if number_count % 3 == 2:
        print(1)
    elif number_count % 3 == 0:
        print((number_count - 192) // 30)
    else:
        print(((number_count - 193) // 3) % 10)

# Проверка

x = '0'
for i in range(1, 201):
    x += str(i)
print(x[number_count-1])
