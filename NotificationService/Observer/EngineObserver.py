from .NotificationObserver import NotificationObserver
from entities.Notification import Notification


class NotificationEngineObserver(NotificationObserver):
    def __init__(self):
        self.strategies=[]

    def add_strategy(self,strategy:NotificationObserver):
        self.strategies.append(strategy)

    def update(self, notification: Notification):
        content= notification.get_content()
        print(f"Notification Engine received notification: {content}")
        for strategy in self.strategies:
            strategy.send_notification(notification)