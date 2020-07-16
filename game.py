'''Game: Guess the number'''
import random

random_number = random.randint(1,50)
attempt_counter = 0
print('Игра, угадай число от 1 до 50')
while attempt_counter < 6:
    number = int(input('Введите число: '))
    attempt_counter+=1
    if number == random_number:
        print('Угадал')
        break
    if number > random_number:
        print('Меньше')
    if number < random_number:
        print('Больше')
    if number != random_number and attempt_counter == 6:
        print(f'Ты проиграл число было: {random_number}')
