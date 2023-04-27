a = int(input("Введите число: "))
b = int(input("В какую степень возвести число: "))

def deg(a, b):
  if b == 1:
    return a
  if b != 1:
    return a * deg(a, b - 1)


print(deg(a, b))