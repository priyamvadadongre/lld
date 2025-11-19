from abc import abstractmethod
from entities.Notification import Notification


class NotificationDecorator(Notification):
    def __init__(self, wrapped_notification: Notification):
        self.wrapped_notification = wrapped_notification

    @abstractmethod
    def get_content(self):
        pass

class UrgentNotificationDecorator(NotificationDecorator):
    def get_content(self):
        return "[URGENT] " + self.wrapped_notification.get_content()
    
class PromotionalNotificationDecorator(NotificationDecorator):
    def get_content(self):
        return self.wrapped_notification.get_content() + " [Don't miss our special offers!]"
    
class ReminderNotificationDecorator(NotificationDecorator):
    def get_content(self):
        return "Reminder: " + self.wrapped_notification.get_content()   
    