from sys import argv

name, time, salary, bonus = argv
try:
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    res = time * salary + bonus
    print(f'заработная плата сотрудника  {res}')
except ValueError:
    print('Not a number')


def sal():
    try:
            time = float(input('Выработка в часах '))
            salary = int(input('Ставка в у.е. '))
            bonus = int(input('Премия в у.е. '))
            res = time * salary + bonus
            print(f'заработная плата сотрудника  {res}')
    except ValueError:
        return print('Not a number')
sal()