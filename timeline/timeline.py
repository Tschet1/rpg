#!/usr/bin/env python3

import pickle
import bisect
from pathlib import Path
from datetime import datetime, timedelta


class Event(object):
    def __init__(self, description: str, time: datetime, visibility: list = []):
        super().__init__()

        self.description = description
        self.time = time

        self.visibility = None if len(visibility) == 0 else visibility

    def __str__(self):
        return f"{str(self.time)}: {self.description}"

    def __lt__(self, other):
        if isinstance(other, datetime):
            return self.time < other
        return self.time < other.time

    def __le__(self, other):
        if isinstance(other, datetime):
            return self.time <= other
        return self.time <= other.time

    def __gt__(self, other):
        if isinstance(other, datetime):
            return self.time > other
        return self.time > other.time

    def __ge__(self, other):
        if isinstance(other, datetime):
            return self.time >= other
        return self.time >= other.time

    def __eq__(self, other):
        return self.time == other.time and self.description == other.description

    def __ne__(self, other):
        return self.time != other.time or self.description != other.description


class Timeline(object):
    def __init__(self):
        super().__init__()

        self.__events = []
        self.__now = datetime(year=1, month=1, day=1)

    @property
    def past(self):
        return self.__events[0:bisect.bisect(self.__events, Event("", self.__now))]

    def get_filtered_past(self, visibility):
        return [ev for ev in self.past if visibility in ev.visibility]

    @property
    def future(self):
        return self.__events[bisect.bisect(self.__events, Event("", self.__now)):]

    def get_filtered_future(self, visibility):
        return [ev for ev in self.future if visibility in ev.visibility]

    def add_event(self, event: Event, fifo: bool = True):
        if fifo:
            bisect.insort(self.__events, event)
        else:
            bisect.insort_left(self.__events, event)

    @property
    def now(self):
        return self.__now

    @now.setter
    def now(self, now: datetime):
        self.__now = now

    def _get_new_events(self, old_time: datetime, new_time: datetime) -> list[Event]:
        ind_o = bisect.bisect(self.__events, old_time)
        ind_n = bisect.bisect(self.__events, new_time)

        if ind_n > ind_o:
            return self.__events[ind_o: ind_n]
        else:
            return []

    def advance_to_time(self, time: datetime) -> list[Event]:
        events = self._get_new_events(self.__now, time)
        self.now = time
        return events

    def advance_by_delta(self, delta: timedelta) -> list[Event]:
        return self.advance_to_time(self.now + delta)

    def advance_to_time_or_event(self, time: datetime) -> Event:
        events = self._get_new_events(self.__now, time)
        if len(events) > 0:
            event = events[0]
            self.now = event.time
            return event

        self.now = time
        return None

    def advance_by_delta_or_event(self, delta: timedelta) -> Event:
        return self.advance_to_time_or_event(self.now + delta)

    def advance_to_next_event(self) -> Event:
        if len(self.future) == 0:
            raise Exception("No events scheduled")

        event = self.future[0]
        self.now = event.time
        return event

    def __str__(self):
        ev = self.past + [Event("<=============== now",
                                self.__now)] + self.future
        ev = [str(e) for e in ev]
        return '\n'.join(ev)


def load_timeline(filename: Path) -> Timeline:
    with open(filename, 'rb') as fil:
        return pickle.load(fil)


def save_timeline(filename: Path, timeline: Timeline):
    with open(filename, 'wb') as fil:
        pickle.dump(timeline, fil)
