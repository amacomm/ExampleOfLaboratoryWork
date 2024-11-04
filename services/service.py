import simpcalc
import time
import threading
import logging


class CancellationToken:
    '''
    Класс токена отмены выполнения задачи.
    '''
    def __init__(self):
        self.__is_canceled = False

    def is_canceled(self) -> bool:
        '''
        Метод проверки отмены задачи.
        Returns:
            True, если задача была отменена.
        '''
        return self.__is_canceled

    def cancel(self) -> None:
        '''
        Метод установки статуса отмены выполнения задачи.
        '''
        self.__is_canceled = True


class Service:
    '''
    Класс простого сервиса.
    '''
    def __init__(self,
                 calculator: simpcalc.Calculator):
        '''
        Конструктор сервиса.
        Args:
            calculator: обработчик задачи.
        '''
        self.__cancellation_token = None
        self.__calculator = calculator
        self.__logger = logging.getLogger(__name__)
        self.__thread = None

    def start(self,
              start_value: float = 0,
              incremental_value: float = 1,
              file_path: str = 'file.txt'):
        '''
        Метод запуска сервиса.
        Args:
            start_value - начальное значение.
            incremental_value - величина изменения.
            file_path - путь до файла записи.
        '''
        if self.__thread is not None:
            error = RuntimeError("Попытка повторного запуска сервиса")
            self.__logger.warning(error)
            raise error
        self.__cancellation_token = CancellationToken()
        self.__thread = threading.Thread(target=self.__run,
                                         args=(start_value,
                                               incremental_value,
                                               file_path,
                                               self.__cancellation_token))
        try:
            self.__thread.start()
            self.__logger.info("Сервис запустился")
        except:
            error = RuntimeError("Не удалось запустить сервис")
            self.__logger.error(error)
            raise error

    def stop(self):
        '''
        Метод остановки сервиса.
        '''
        if self.__thread is None:
            error = RuntimeError("Попытка остановить незапущенный сервис")
            self.__logger.warning(error)
            raise error
        self.__cancellation_token.cancel()
        self.__thread.join()
        self.__thread = None
        self.__logger.info("Сервис завершил работу")

    def __run(self,
              start_value: float = 0,
              incremental_value: float = 1,
              file_path: str = 'file.txt',
              cancellation_token: CancellationToken = CancellationToken()):
        value = start_value
        while (not cancellation_token.is_canceled()):
            value = self.__calculator.add(value, incremental_value)
            try:
                with open(file_path, 'a') as f:
                    f.write(str(value) + '\n')
            except:
                error = RuntimeError("Не удалось записать данные в файл," +
                                     "сервис завершает работу")
                self.__logger.error(error)
                raise error
            time.sleep(1)
