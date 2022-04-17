from datetime import datetime
from app.constants.working_hours import WorkingHours, TimeFormat


class IsOpenManager:
    def __init__(self, start_time, end_time) -> None:
        self.start_time = start_time
        self.end_time = end_time

    def is_open(self):
        """
        Check if restaurant is open based on the reservation
        end and start time
        """
        return (
            True
            if (
                datetime.strptime(self.start_time, TimeFormat.time_format)
                >= WorkingHours.start_time
            )
            and (
                datetime.strptime(self.end_time, TimeFormat.time_format)
                < WorkingHours.end_time
            )
            else False
        )


class ConvertTime:
    """
    convet time from hh:mm AM/PM to same as foramt in DB hh:mm:ss
    """

    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def convertTo24(self):
        start_time_ = datetime.strptime(self.start_time, "%I:%M%p").time()
        end_time_ = datetime.strptime(self.end_time, "%I:%M%p").time()

        return start_time_, end_time_
