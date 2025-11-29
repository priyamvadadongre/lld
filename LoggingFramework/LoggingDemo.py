class LoggingDemo:
    @staticmethod
    def demo():
        from Entites.LogLevel import LogLevel
        from Observer.LoggerObserver import ConsoleLoggerObserver, FileLoggerObserver
        from LogManager import LogManager
        from Decorator.LogFormatter import SimpleLogFormatter,TimeStampLogFormatter
        # root logger setup
        logging_manager = LogManager()
        app_logger = logging_manager.get_logger("com.app.logger")
        print(f"Acquired logger: {app_logger.get_name()}")
         # Set log levels
        app_logger.set_level(LogLevel.WARNING)
        console_logger = ConsoleLoggerObserver(formatter=SimpleLogFormatter())
        file_logger = FileLoggerObserver( formatter=TimeStampLogFormatter(), file_path="app.log")

        # Attach observers to loggers
        root_logger = logging_manager.get_root_logger()
        root_logger.attach(console_logger)
        app_logger.attach(console_logger)
        app_logger.attach(file_logger)

        # Logging messages
        root_logger.debug("This is a debug message from root logger.")
        root_logger.error("This is an error message from root logger.")
        app_logger.info("This is an info message from AppLogger.")
        app_logger.warning("This is a warning message from AppLogger.")
        app_logger.critical("This is a critical message from AppLogger.")
        # release locks
        logging_manager._lock.release()
        import time
        time.sleep(2)  # Wait for async logs to be processed
        # Shutdown async processors
        logging_manager.shutdown()

if __name__ == "__main__":
    LoggingDemo.demo()
