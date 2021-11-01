# Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    numbers = [a, b, c]
    numbers.remove(min(numbers))
    return sum(numbers)


num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
num_3 = int(input('Введите третье число: '))
result = my_func(num_1, num_2, num_3)
print('Сумма двух наибольших чисел ', result)


# V2

def my_func(arg_1, arg_2, arg_3):
    sorted_list = sorted([arg_1, arg_2, arg_3])
    return sorted_list[2] + sorted_list[1]


print(my_func(int(input('Введите первое число >> ')), int(input('Введите второе число >> ')), int(input('Введите '
                                                                                                        'третье число'
                                                                                                        ' >> '))))
