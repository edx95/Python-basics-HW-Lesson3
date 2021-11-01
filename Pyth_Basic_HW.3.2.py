# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_data(name, surname, year, city, email, phone):
    print(f'Имя пользователя: {name}, фамилия: {surname}, год рождения: {year}, город проживания: {city}, '
          f'e-mail: {email}, телефон: {phone}.')


user_data(name=input('Имя: '), surname=input('Фамилия: '), year=input('Год рождения: '), city=input('Город: '),
          email=input('e-mail: '), phone=input('Телефон: '))

# V2

user = {'имя': '', 'фамилию': '', 'год рождения': '', 'город': '', 'email': '', 'телефон': ''}
for data in user.keys():
    user[data] = input(f'Введите {data}: ')

user_data(name=user['имя'], surname=user['фамилию'], year=user['год рождения'], city=user['город'], email=user['email'],
          phone=user['телефон'])