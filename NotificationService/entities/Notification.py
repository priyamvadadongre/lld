
from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def get_content(self):
        pass

class SimpleNotification(Notification):
    def __init__(self, content):
        self.content = content

    def get_content(self):
        return self.content

   




    
