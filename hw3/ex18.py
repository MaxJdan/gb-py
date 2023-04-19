from random import randint
input_s = [randint(-100, 100) for _ in range(int(input('Введите размер массива: ')))]
print(input_s)
x = int(input("Введите число x: "))
n = len(input_s)
print(f"Кол-во элементов {n}")
min = input_s[0]
for i in range(n):
        if abs(input_s[i] - x) < abs(min - x):
            min = input_s[i]
print (f"самый близкий по величине элемент это {min}")
