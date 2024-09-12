from dataclasses import dataclass, field
from datetime import datetime, date, time
from typing import ClassVar

from app.services.util import generate_unique_id, date_lower_than_today_error, event_not_found_error, \
    reminder_not_found_error, slot_not_available_error


# TODO: Implement Reminder class here
@dataclass
class Reminder:
    EMAIL = "email"
    SYSTEM = "system"

    def __init__(self, date_time: datetime, type: str = EMAIL):
        self.date_time: datetime = date_time
        self.type: str = type

    def __str__(self) -> str:
        return f"Reminder on {self.date_time} of type {self.type}"


# TODO: Implement Event class here
@dataclass
class Event:
    def __init__(self, title: str, description: str, date_: date, start_at: time, end_at: time):
        self.title: str = title
        self.description: str = description
        self.date_: date = date_
        self.start_at: time = start_at
        self.end_at: time = end_at


# TODO: Implement Day class here


# TODO: Implement Calendar class here