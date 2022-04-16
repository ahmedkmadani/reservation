from datetime import datetime
from app.constants.working_hours import WorkingHours

class IsOpenManager:

    def __init__(self, start_time, end_time) -> None:
        self.start_time = start_time
        self.end_time = end_time

    def is_open(self):
        """
        Check if restaurant is open based on the reservation
        end and start time
        """
        start_time_ = datetime.strptime(self.start_time, "%I:%M%p")
        end_time_ = datetime.strptime(self.end_time, "%I:%M%p")
        if (start_time_ >= WorkingHours.start_time) and (end_time_ < WorkingHours.end_time):
            return  True
        return False
