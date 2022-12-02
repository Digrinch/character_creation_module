from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def CalculateSquareRoot(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Функция вывода ответа."""
    if your_number <= 0:
        return
    num = CalculateSquareRoot(your_number)
    print('Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {num}')


print(message)
calc(25.5)
