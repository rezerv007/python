name = input('enter name')
surname = input('enter surname')
year = int(input('enter year'))
city = input('enter city')
email = input('enter email')
telephone = input('input telephone')


def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(surname='Yakimov', name='Egor', year='1993', city='Moscow', email='nrs3@inbox.ru',
              telephone='8-999-999-99-99'))
