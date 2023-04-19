import random
from random import randint

col_coin = int(input('введите количество монет: '))
x = 0
y = 0
coins = [0, 1]
for _ in range(col_coin):
    random.shuffle(coins)
    print(f'монета{coins}')
    if int(coins[0]) == 0:
        x += 1
    if int(coins[0]) == 1:
        y += 1
print(f'всего монет {x, y}')
if x > y:
    ans = y
else:
    ans = x
print(f"минимальное количество монет, которые нужно перевернуть {ans}")