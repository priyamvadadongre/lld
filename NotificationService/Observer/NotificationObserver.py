from abc import ABC, abstractmethod

from entities.Notification import Notification


class NotificationObserver(ABC):
    @abstractmethod
    def update(self, notification: Notification):
        pass