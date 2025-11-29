import threading

from Entites.LogLevel import LogLevel
from Entites.Logger import Logger


class LogManager:
    _loggers : dict[str, Logger]= {}
    _lock = threading.RLock()
    root_logger = Logger("root", LogLevel.DEBUG, None)
    _loggers["root"] = root_logger
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            with cls._lock:
                if not hasattr(cls, 'instance'):
                    cls.instance = super().__new__(cls)

       
        return cls.instance
    
    def get_logger(self, name: str):
        if name in self._loggers:
            return self._loggers[name]
        else:
            return self._create_logger(name)
        
    def _create_logger(self, name: str) -> Logger:
        self._lock.acquire()
        if name not in self._loggers:
            filename = name.split('.')[-1]
            parent_name = '.'.join(name.split('.')[:-1]) if '.' in name else "root"
            if parent_name=="root":
                new_logger = Logger(filename, LogLevel.DEBUG, self.root_logger)
                self._loggers[name] = new_logger
            else:
                new_logger = Logger(filename, LogLevel.DEBUG, self.get_logger(parent_name))
            self._loggers[name] = new_logger
                
        self._lock.release()
        return self._loggers[name]
            
        
    def shutdown(self):
        for logger in self._loggers.values():
            logger.async_processor.shutdown()


    def set_root_level(self, level: LogLevel):
        self.root_logger.set_level(level)    

    def get_root_logger(self) -> Logger:
        return self.root_logger
    



