from datetime import datetime
import threading

from Entites import LogLevel


class LogMessage:
    def __init__(self,message:str,log_level:LogLevel,logger_name:str):
        # final keyword  in python is not available but we can use naming convention
        self.message=message
        self.log_level=log_level
        self.timestamp=datetime.now()
        self.logger_name=logger_name
        self.thread_name=threading.current_thread().name 

    def get_message(self):
        return self.message 
    
    def get_log_level(self):
        return self.log_level   
    
    def get_timestamp(self):
        return self.timestamp
    
    def get_logger_name(self):
        return self.logger_name

    def get_thread_name(self):
        return self.thread_name

        


    