from datetime import datetime

#TODO: MOVE TO DB
class WorkingHours:
    start_time = datetime.strptime("12:00PM", "%I:%M%p")
    end_time = datetime.strptime("11:59PM", "%I:%M%p")
