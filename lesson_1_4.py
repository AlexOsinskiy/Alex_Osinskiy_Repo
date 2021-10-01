print('Введите число')
a = int(input())
p = 0
r = 0
while a > 0:
    p = a % 10
    a = a // 10
    if p == 9:
        r = p
        break
    elif p > r:
        r = p
        continue
print(f" Самая большая цифра в числе {r}")
