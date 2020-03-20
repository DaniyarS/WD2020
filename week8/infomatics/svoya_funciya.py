import random

user_number = int(input('Введи загаданное число: '))

hidden_number = int(random.randrange(0, 100))

def number_guess(x):
    if(x > hidden_number):
        print('Ваше число больше загаданного, попробуй еще раз :-)\n')
        a = int(input())
        number_guess(a)
    elif(x < hidden_number):
        print('Ваше число меньше загаданного, попробуй еще раз :-)\n')
        a = int(input())
        number_guess(a)
    else:
        print('Вы угадали число\n')
        return 0

check = True

while(check == True):
    number_guess(user_number)
    check = False

input()