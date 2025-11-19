from entities.Notification import SimpleNotification
from Observer.NotificationSubject import NotificationSubject
from Observer.EngineObserver import NotificationEngineObserver
from Strategy.NotificationStrategy import EmailNotificationStrategy, SMSNotificationStrategy, PushNotificationStrategy

class NotificationSystem:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def send_system_notification(self, content):
        
        # Create notification
        notification = SimpleNotification(content)

        # Setup subject and observers
        subject = NotificationSubject()
        engine_observer = NotificationEngineObserver()

        # Add strategies to the observer
        engine_observer.add_strategy(EmailNotificationStrategy())
        engine_observer.add_strategy(SMSNotificationStrategy())
        engine_observer.add_strategy(PushNotificationStrategy())

        # Register observer with the subject
        subject.register_observer(engine_observer)

        # Notify observers
        subject.notify_observers(notification)


    

if __name__ == "__main__":
    notification_system = NotificationSystem()
    notification_system.send_system_notification("This is a test notification.")