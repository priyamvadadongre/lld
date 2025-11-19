from .NotificationObserver import NotificationObserver
from entities.Notification import Notification


class LoggingObserver(NotificationObserver):
    def update(self, notification: Notification):
        print(f"Logging Notification: {notification.get_content()}")

