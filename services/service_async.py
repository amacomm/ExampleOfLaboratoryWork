import simpcalc
import asyncio
import aiofiles
import logging


class CancellationToken:
    '''
    Class for task cancellation.
    '''
    def __init__(self):
        self.__is_canceled = False

    def is_canceled(self) -> bool:
        '''
        Check if the task was canceled.
        Returns:
            True if the task is canceled.
        '''
        return self.__is_canceled

    def cancel(self) -> None:
        '''
        Mark the task as canceled.
        '''
        self.__is_canceled = True


class ServiceAsync:
    '''
    A simple service class using asyncio.
    '''
    def __init__(self, calculator: simpcalc.Calculator):
        '''
        Constructor for the service.
        Args:
            calculator: Task handler (simpcalc.Calculator).
        '''
        self.__cancellation_token = None
        self.__calculator = calculator
        self.__logger = logging.getLogger(__name__)
        self.__task = None

    async def start(self, start_value: float = 0, incremental_value: float = 1, file_path: str = 'file.txt'):
        '''
        Start the service asynchronously.
        Args:
            start_value - Initial value for calculations.
            incremental_value - Increment value for each step.
            file_path - Path to the file where results will be written.
        '''
        if self.__task is not None:
            error = RuntimeError("Attempt to start running service")
            self.__logger.warning(error)
            raise error
        self.__cancellation_token = CancellationToken()
        self.__loop = asyncio.get_event_loop()
        self.__task = asyncio.create_task(self.__run(start_value, incremental_value, file_path, self.__cancellation_token))
        self.__logger.info("Service started")

    async def stop(self):
        '''
        Stop the service by cancelling the task.
        '''
        if self.__task is None:
            error = RuntimeError("Attempt to stop service before it starts")
            self.__logger.warning(error)
            raise error
        self.__cancellation_token.cancel()
        await self.__task  # Wait for the task to finish
        self.__task = None
        self.__logger.info("Service is terminated")

    async def __run(self, start_value: float, incremental_value: float, file_path: str, cancellation_token: CancellationToken):
        '''
        The main running loop for the service.
        '''
        value = start_value
        while not cancellation_token.is_canceled():
            value = await asyncio.to_thread(self.__calculator.add, value, incremental_value)
            try:
                # Writing to the file asynchronously
                async with aiofiles.open(file_path, 'a') as f:
                    await f.write(f"{value}\n")
            except Exception as error:
                self.__logger.error(f"Unable to write into file, service is being terminated: {error}")
                break
            await asyncio.sleep(1)
