'''Game: Guess the number'''
import random
random_number = random.randint(1,50)
attempt_counter = 0
while attempt_counter <= 5:
    number = int(input('Введите число: '))
    attempt_counter+=1
    if number == random_number:
        print('Угадал')
        break
    if number > random_number:
        print('Меньше')
    if number < random_number:
        print('Больше')
