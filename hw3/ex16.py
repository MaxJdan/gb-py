from random import randint
N = [randint(1, 9) for _ in range(int(input('Введите размер массива: ')))]
print(N)
print('Встречается', N.count(int(input('Введите искомое число: '))), 'раз')