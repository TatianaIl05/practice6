n, k, m = map(int, input('Введите количество малышей, детей на карусели, минут: ').split())

whole_time = (n//k)*2*m

if n < k:
    print(m*2)
elif n % k == 0:
    print(whole_time)
else:
    print(whole_time + (n % k)*2*m)
