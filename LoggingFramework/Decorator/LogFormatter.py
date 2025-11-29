from abc import ABC, abstractmethod


class LogFormatter(ABC):
    @abstractmethod
    def format(self, message: str) -> str:
        pass


class SimpleLogFormatter(LogFormatter):
    def format(self, message: str) -> str:
        return f"[LOG]: {message}"
    
class TimeStampLogFormatter(LogFormatter):
    def format(self, message: str) -> str:
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"[{timestamp}] [LOG]: {message}"
