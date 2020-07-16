'''Game: Guess the number'''
import random
a = random.randint(1,50)
popitka = 1
while popitka < 7:
    b = int(input('Введите число: '))
    if b == a:
        print('Угадал')
        break
    if b > a:
        print('Меньше')
    if b < a:
        print('Больше')
