k = int(input('Введите количество суши: '))

answer = 'нет'

for i in range(k//5):
    for j in range(k//7):
        if k == 5*i + 7*j:
            answer = 'да'

print(answer)
