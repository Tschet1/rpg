#!/usr/bin/env python3

import pickle
import bisect
from pathlib import Path
from datetime import datetime, timedelta


class Event(object):
    def __init__(self, description: str, time: datetime, visibility: list = [], state=None):
        super().__init__()

        self.description = description
        self.time = time

        self.visibility = None if len(visibility) == 0 else visibility
        self.state = state

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
        self.__now_idx = 0
        self.__prev_idx = 0

    @property
    def past(self):
        return self.__events[0:self.__now_idx]

    def get_filtered_past(self, visibility):
        return [ev for ev in self.past if visibility in ev.visibility]

    @property
    def future(self):
        return self.__events[self.__now_idx:]

    def get_filtered_future(self, visibility):
        return [ev for ev in self.future if visibility in ev.visibility]

    def add_event(self, event: Event, fifo: bool = True):
        if event.time < self.now:
            self.__now_idx += 1

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
        self.__prev_idx = self.__now_idx
        self.__now_idx = bisect.bisect_left(self.__events, now)

    def _advance_event(self) -> Event:
        if len(self.future) == 0:
            raise Exception("No events scheduled")

        evt = self.future[0]
        idx = self.__now_idx
        self.now = evt.time
        self.__now_idx = idx + 1
        return evt

    def _get_new_events(self) -> list[Event]:
        ind_o = self.__prev_idx
        ind_n = self.__now_idx

        if ind_n > ind_o:
            return self.__events[ind_o: ind_n]
        else:
            return []

    def _new_events_in_time(self, time: datetime) -> bool:
        ind_o = self.__now_idx
        ind_n = bisect.bisect_left(self.__events, time)
        return ind_o != ind_n

    def advance_to_time(self, time: datetime) -> list[Event]:
        self.now = time
        return self._get_new_events()

    def advance_by_delta(self, delta: timedelta) -> list[Event]:
        return self.advance_to_time(self.now + delta)

    def advance_to_time_or_event(self, time: datetime) -> Event:
        if self._new_events_in_time(time):
            return self._advance_event()

        self.now = time
        return None

    def advance_by_delta_or_event(self, delta: timedelta) -> Event:
        return self.advance_to_time_or_event(self.now + delta)

    def advance_to_next_event(self) -> Event:
        return self._advance_event()

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
