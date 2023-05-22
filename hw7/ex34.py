def fun(words):
    return sum(1 for i in words if i in 'аеёиоуыэюя')
song = "пара-ра-рам рам-пам-папам па-ра-па-да"
s = song.lower().split()
t = fun(s[0])
if all([fun(i) == t for i in s]):
    print('Парам пам-пам')
else:
    print('Пам парам')