'''
Модуль класса простого калькулятора для выполнения
математических операций.
'''
import numpy as np


class Calculator:
    '''
    Класс простого калькулятора для выполнения
    основных математических операций.
    '''
    def __init__(self):
        pass

    def add(self,
            x1: int | float | np.ndarray,
            x2: int | float | np.ndarray) -> int | float | np.ndarray:
        '''
        Метод сложения двух величин.

        Args:
            x1: аргумент слева от знака сложения.
            x2: аргумент справа от знака сложения.

        Returns:
            Сумма двух аргументов.
        '''
        return x1 + x2

    def multiply(self,
                 x1: int | float | np.ndarray,
                 x2: int | float | np.ndarray) -> int | float | np.ndarray:
        '''
        Метод перемножения двух величин.

        Args:
            x1: аргумент слева от знака умножения.
            x2: аргумент справа от знака умножения.

        Returns:
            Произведение двух аргументов.
        '''
        return x1 * x2

    def subtract(self,
                 x1: int | float | np.ndarray,
                 x2: int | float | np.ndarray) -> int | float | np.ndarray:
        '''
        Метод получения разности двух величин.

        Args:
            x1: аргумент слева от знака 'минус'.
            x2: аргумент справа от знака 'минус'.

        Returns:
            Разность двух аргументов.
        '''
        return x1 - x2

    def divide(self,
               x1: int | float | np.ndarray,
               x2: int | float | np.ndarray) -> int | float | np.ndarray:
        '''
        Метод деления двух величин.

        Args:
            x1: аргумент слева от знака деления.
            x2: аргумент справа от знака деления.

        Returns:
            Частное двух аргументов.
        '''
        if x2 != 0:
            return x1 / x2
        else:
            raise ValueError("Аргумент справа от знака деления " +
                             "не может быть равен нулю")


if __name__ == "__main__":
    pass
