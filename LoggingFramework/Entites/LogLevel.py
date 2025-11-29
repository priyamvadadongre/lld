from enum import Enum


class LogLevel(Enum):
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    CRITICAL = 5

    def is_higher_or_equal(self, other_level: "LogLevel") -> bool:
        return self.value >= other_level.value

