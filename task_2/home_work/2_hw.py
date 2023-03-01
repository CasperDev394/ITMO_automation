def task_1() -> None:
    a_1: int = 123
    a_2: float = 1.23
    a_3: str = '123'
    a_4: list = [1, 2, 3]
    a_5: bool = True

    print('type a_1 = ', type(a_1))
    print('type a_2 = ', type(a_2))
    print('type a_3 = ', type(a_3))
    print('type a_4 = ', type(a_4))
    print('type a_5 = ', type(a_5))


task_1()


def task_2() -> None:
    a = [1, 2, 3, 5, 8, 13, 21]
    print(a[0:3])
    # Последовательность - фибоначчи


task_2()


def task_3(i: int) -> int:
    return i**2


print(task_3(3))
