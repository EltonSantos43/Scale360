from enum import Enum
from datetime import date

class DayType(Enum):
    WORK = "WORK"
    OFF = "OFF"
    COMP_OFF = "COMP_OFF"
    HOLIDAY = "HOLIDAY"

class DayAssignment:
    def __init__(self, day: date, day_type: DayType, shift: str | None = None):
        if not isinstance(day, date):
            raise ValueError("day must be a date instance")

        if not isinstance(day_type, DayType):
            raise ValueError("day_type must be a Daytype")

        self.day = day
        self.type = day_type
        self.shift = shift

    def __repr__(self):
        return f"<DayAssignment {self.day} {self.type.name}>"
