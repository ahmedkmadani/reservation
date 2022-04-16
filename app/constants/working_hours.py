from datetime import datetime


class TimeFormat:
    time_format = "%I:%M%p"


# TODO: MOVE TO DB
class WorkingHours:
    start_time = datetime.strptime("12:00PM", TimeFormat.time_format)
    end_time = datetime.strptime("11:59PM", TimeFormat.time_format)
