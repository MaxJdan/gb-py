m = int(input('Введите сумму чисел: '))
n = int(input('Введите произведение чисел: '))
x = (m-int((m**2-4*n)**0.5))//2
y = m - x
print(f'числа Пети{x, y}')