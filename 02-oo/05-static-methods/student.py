class Duration:
    def __init__(self, *, duration_in_seconds):
        self.__duration_in_seconds = duration_in_seconds

    @property
    def seconds(self):
        return self.__duration_in_seconds

    @property
    def minutes(self):
        return self.__duration_in_seconds / 60

    @property
    def hours(self):
        return self.__duration_in_seconds / 3600

    @staticmethod
    def from_seconds(value):
        return Duration(duration_in_seconds=value)

    @staticmethod
    def from_minutes(value):
        return Duration(duration_in_seconds=value * 60)

    @staticmethod
    def from_hours(value):
        return Duration(duration_in_seconds=value * 3600)
