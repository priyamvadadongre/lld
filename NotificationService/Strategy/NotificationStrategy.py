from abc import ABC, abstractmethod


class NotificationStrategy(ABC):
    @abstractmethod 
    def send_notification(self, notification):
        pass


class EmailNotificationStrategy(NotificationStrategy):
    def send_notification(self, notification):
        print(f"Sending Email Notification: {notification.get_content()}")  

class SMSNotificationStrategy(NotificationStrategy):
    def send_notification(self, notification):
        print(f"Sending SMS Notification: {notification.get_content()}")

class PushNotificationStrategy(NotificationStrategy): 
    def send_notification(self, notification):
        print(f"Sending Push Notification: {notification.get_content()}")