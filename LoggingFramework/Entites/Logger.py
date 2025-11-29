from .LogLevel import LogLevel
from .AsyncProcessor import AsyncProcessor
from .LogMessage import LogMessage
from Observer.LogSubject import LoggerSubject


class Logger(LoggerSubject):
    def __init__(self, name: str, level: LogLevel,parent_logger: "Logger" = None):
        self.name = name
        self.level = level
        self.parent_logger = parent_logger
        self.additive = True
        self.async_processor = AsyncProcessor()
        super().__init__()

    def get_name(self):
        return self.name
    def get_level(self):
        return self.level
    def get_parent_logger(self):
        return self.parent_logger
    def is_additive(self):
        return self.additive
    
    def set_level(self, level: LogLevel):
        self.level = level  

    def set_additive(self, additive: bool):
        self.additive = additive    

    def log(self, msg:str, level:LogLevel):
        if level.is_higher_or_equal(self.level):
            from Entites.LogMessage import LogMessage
            log_message = LogMessage(msg, level, self.name)
            self.notify_observers(log_message)

        
        if self.additive and self.parent_logger:
            self.parent_logger.log(msg, level)


    def notify_observers(self, log_message: LogMessage):
        self.async_processor.process_async(self.notify, log_message)

    def debug(self, msg:str):
        self.log(msg, LogLevel.DEBUG)

    def info(self, msg:str):
        self.log(msg, LogLevel.INFO)    

    
    def warning(self, msg:str):
        self.log(msg, LogLevel.WARNING)

    def error(self, msg:str):
        self.log(msg, LogLevel.ERROR)

    def critical(self, msg:str):
        self.log(msg, LogLevel.CRITICAL)

    

    

    

