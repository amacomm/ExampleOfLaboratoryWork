'''
Модуль класса простого калькулятора для выполнения
математических операций.
'''
import numpy as np
import logging


class Calculator:
    '''
    Класс простого калькулятора для выполнения
    основных математических операций.
    '''
    def __init__(self):
        self.__logger = logging.getLogger(__name__)

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
        self.__logger.debug(f"{x1} + {x2}")
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
        self.__logger.debug(f"{x1} * {x2}")
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
        self.__logger.debug(f"{x1} - {x2}")
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
            self.__logger.debug(f"{x1} / {x2}")
            return x1 / x2
        else:
            error = ValueError("Аргумент справа от знака деления " +
                               "не может быть равен нулю")
            self.__logger.warning(error)
            raise error


if __name__ == "__main__":
    pass
