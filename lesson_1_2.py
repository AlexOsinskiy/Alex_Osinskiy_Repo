print('Введите количество секунд')
a = int(input())
h = a // 3600
m = a // 60 % 60
s = a % 60
print(f'{h:02d}:{m:02d}:{s:02d}')
