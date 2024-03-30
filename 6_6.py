n, k, m = map(int, input('Введите количество малышей, детей на карусели, минут: ').split())

total_rides = 2*n
times_count = total_rides//k

if total_rides % k != 0:
    times_count += 1

print(times_count*m)
