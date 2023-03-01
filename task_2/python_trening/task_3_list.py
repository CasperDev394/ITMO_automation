a = [5, 10, 15, 29, 25, 30, 35, 40]

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

# Изменение элемента
b = [11, 12, 13]
b[2] = 4
print(b)


test_list = ['один', 'два', 'три', 'четыре', 'пять']


for elem in test_list:  # Цикл по списку
    print(elem)

print(len(test_list))  # Получить длину списка

test_list.append('шесть')  # Добавить значение в список
print(test_list)

