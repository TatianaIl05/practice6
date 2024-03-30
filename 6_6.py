n, k, m = map(int, input('Введите количество малышей, детей на карусели, минут: ').split())

all_rides = 2*n
times_count = all_rides//k

if all_rides % k != 0:
    times_count += 1
if n < k:
    times_count = 2

print(times_count*m)
