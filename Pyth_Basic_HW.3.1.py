# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def fun_div(val_a, val_b):
    try:
        var_div = val_a / val_b
    except ZeroDivisionError:
        print('Мы делим на ноль!')
        return 'Деление на ноль невозможно!'
    else:
        return var_div


try:
    var_print = (
        f"Результат Деления: {fun_div(int(input('Введите делимое число: ')), int(input('Введите делитель: ')))}")
except ValueError:
    print('Вы ввели не число!')
else:
    print(var_print)



# V2
def div_func(arg_1, arg_2):
    return arg_1 / arg_2


try:
    print(div_func(int(input('Введите делимое >> ')), int(input('Введите делитель >> '))))
except ZeroDivisionError:
    print('На ноль делить нельзя!')

