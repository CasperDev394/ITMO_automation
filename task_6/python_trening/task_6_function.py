# определяем функцию
def add(x, y):
    return x + y


# вызываем функцию
print(add(1, 2))


# вызываем функцию с другими аргументами
print(add('I a', 'm tester'))


# Обязательные и необязательные аргументы
def arg(a, b, c=2, d=3):
    return a + b + c + d


print(arg(1, 1, 1, 1))

print(arg(2, 2))

print(arg(2, 2, '1', 1))


# def arg(a=1, b=2, c, d):
#     return a + b + c + d


# порядок аргументов
def range_arg(a, b, c, d):
    return a + ' ' + b + ' ' + c + ' ' + d


print(range_arg('1', '2', '3', '4'))

print(range_arg('1', '2', d='3', c='4'))


# задача
def task_func(a=(1, 2, 3, 4)):
    return a[1]


print(task_func())


def compute_surface(radius, pi=3.14159):
    return pi * radius * radius


print(compute_surface(2))

