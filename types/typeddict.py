# PEP 589: TypedDict

from datetime import datetime
from typing import TypedDict


class Event(TypedDict):
    event_id: str
    timestamp: datetime


Event(event_id="1234", timestamp=datetime.now())
