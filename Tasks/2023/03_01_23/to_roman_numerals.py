I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
rome_num = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C',400: 'CD', 500: 'D', 900: 'CM'}
one = 'I'
four = 'IV'
five = 'V'
nine = 'IX'
ten = 'X'
forty = 'XL'
fifty = 'L'
ninty = 'XC'
hundr = 'C'
fourhundr = 'CD'
fivehundr = 'D'
ninehundr = 'CM'


def len_user():
    a = len(str(user))
    return a


def number_one(user):
    b = int(str(user)[0])
    return b




def first_symbol(user):
    if int(user) <= 3:
        x = (one)*user
    elif int(user) == 4:
        x = four
    elif int(user) == 5:
        x = five
    elif int(user) >=6 and int(user) <=8:
        x = five+(one)*(int(user) - 5)
    elif int(user) == 9:
        x = nine
    return x


def second_symbol(user):
    if int(user) >= 10 and int(user) <= 39:
        y = (ten) * number_one(user)
    elif int(user) >= 40 and int(user) <=49:
        y = forty
    elif int(user) >= 50 and int(user) <= 89:
        y = fifty + (ten)*(number_one(user) - 5)
    elif int(user) >= 90 and int(user) <= 99:
        y = ninty
    return y


def third_symbol(user):
    if int(user) >= 100 and int(user) <= 399:
        z = (hundr) * number_one(user)
    elif int(user) >= 400 and int(user) <=499:
        z = fourhundr
    elif int(user) >= 500 and int(user) <= 899:
        z = (fivehundr)* number_one(user)
    elif int(user) >= 900 and int(user) <= 990:
        z = ninehundr
    return z


while True:
    user = input('Input your number -> ')
    if len_user() == 1:
        print(first_symbol(user))
    elif len_user() == 2:
        print(second_symbol(user) + first_symbol(((int(str(user)[1])))))
    elif len_user() == 3:
        print(third_symbol(user) + second_symbol(((int(str(user)[1:3])))) + first_symbol(((int(str(user)[2])))))
    print('If you want o stop press "N", if you want to continue press any button')
    ask = input('Your choise -> ').lower()
    if ask == 'n'.lower():
        break
    else:
        continue







"""
def number_two(user):
    c = int(str(user)[1])
    return c


def number_three(user):
    d = int(str(user)[2])
    return d


def first_symbol(user):
    if one_number(user) <= 3:
        x = (one)*user
    elif one_number(user) == 4:
        x = four
    elif one_number(user) == 5:
        x = five
    elif one_number(user) >=6 and one_number(user) <=8:
        x = five+(one)*(one_number(user) - 5)
    elif one_number(user) == 9:
        x = nine
    return x"""


"""def second_symbol(user):
    if two_numbers(user) >= 10 and two_numbers(user) <= 39:
        y = (ten) * one_number(user)
    elif two_numbers(user) >= 40 and two_numbers(user) <=49:
        y = forty
    elif two_numbers(user) >= 50 and two_numbers(user) <= 89:
        y = fifty + (ten)*(one_number(user) - 5)
    elif two_numbers(user) >= 90 and two_numbers(user) <= 99:
        y = ninty
    return y"""