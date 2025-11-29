from Observer import LoggerObserver

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Observer.LoggerObserver import LoggerObserver
class LoggerSubject:
    def __init__(self): 
        self.observers: list[LoggerObserver] = []

    def attach(self, observer:LoggerObserver):
        self.observers.append(observer)

    def detach(self, observer:LoggerObserver ):
        self.observers.remove(observer)

    def notify(self, log_message):
        for observer in self.observers:
            observer.update(log_message)