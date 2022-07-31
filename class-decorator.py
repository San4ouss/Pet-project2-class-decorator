import time
from functools import wraps


class CheckTime:
    """Класс-декоратор для замера времени работы функции"""

    def __init__(self, times):
        self.times = times  # локальная переменная, определяющая количество прогонов измеряемой функции

    def __call__(self, func):
        @wraps(func)  # сохраняем имя и описание проверяемой функции
        def wrapper(*args, **kwargs):
            start_time = time.time()
            for i in range(self.times):
                func(*args, **kwargs)
            end_time = time.time()
            dt = end_time - start_time
            return f"Функция {func.__name__} выполняет свою работу за {round(dt, 3)} секунд " \
                   f"при количестве прогонов равное {self.times} раз"

        return wrapper

    def __setattr__(self, key, value):
        if key == "times" and type(value) is not int:
            raise AttributeError("Значение times должно иметь тип int")
        object.__setattr__(self, key, value)


@CheckTime(times=2)
def list_compr():
    """Создание списка с помощью list comprehensions"""
    return [i for i in range(10000000)]


@CheckTime(times=2)
def loop_for():
    """Создание списка с помощью цикла for"""
    lst = []
    for i in range(10000000):
        lst.append(i)
    return lst


@CheckTime(times=2)
def generator():
    """Создание генератора со значениями"""
    return (i for i in range(10000000))


print(list_compr())
print(loop_for())
print(generator())

print(loop_for.__name__)
print(list_compr.__doc__)
print(generator.__doc__)
