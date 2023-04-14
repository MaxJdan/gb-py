print("Введи 3-значное число")
n = int(input())
a = n // 100
b = n % 100 // 10
c = n % 10
print(int(a + b + c))