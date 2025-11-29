from abc import ABC, abstractmethod
import threading

from Decorator.LogFormatter import LogFormatter
from Entites.LogMessage import LogMessage
class LoggerObserver(ABC):
    @abstractmethod
    def update(self, log_message: "LogMessage"):
        pass


class ConsoleLoggerObserver(LoggerObserver):

    def __init__(self, formatter:LogFormatter):
        self.formatter=formatter
        
    def update(self, log_message: "LogMessage"):
        print(f"Console Logger: {log_message.logger_name}  : {self.formatter.format(log_message.message)}") 

class FileLoggerObserver(LoggerObserver):

    def __init__(self, formatter:LogFormatter, file_path: str):
        self.formatter=formatter
        self.file_path = file_path
        self._lock = threading.Lock()

    def update(self, log_message: "LogMessage"):
        with self._lock:
            with open(self.file_path, 'a') as file:
                file.write(f"File Logger: {self.formatter.format(log_message.message)}\n")
