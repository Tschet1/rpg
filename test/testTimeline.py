#!/usr/bin/env python3

import unittest
import random
import tempfile
from pathlib import Path
from datetime import datetime, timedelta
from timeline.timeline import Event, Timeline, save_timeline, load_timeline


class TestTimeline(unittest.TestCase):
    NUM_EVENTS = 15

    def _create_timeline(self):
        tl = Timeline()
        for i in range(1, self.NUM_EVENTS + 1):
            tl.add_event(Event(f"Event {i}", datetime(
                1, 1, i, hour=i, minute=i, second=i)))
        self.assertEqual(len(tl.future), self.NUM_EVENTS)
        self.assertEqual(len(tl.past), 0)
        return tl

    def test_set_now(self):
        tl = self._create_timeline()
        for i in range(1, self.NUM_EVENTS + 1):
            t = datetime(1, 1, i, hour=0)
            tl.now = t
            self.assertEqual(len(tl.future), self.NUM_EVENTS-i+1)
            self.assertEqual(len(tl.past), i-1)

    def test_advance_by_delta(self):
        tl = self._create_timeline()
        for i in range(1, self.NUM_EVENTS + 1):
            events = tl.advance_by_delta(timedelta(days=1))
            self.assertEqual(len(events), 1)
            self.assertEqual(events[0].description, f"Event {i}")
            self.assertEqual(len(tl.future), self.NUM_EVENTS-i)
            self.assertEqual(len(tl.past), i)

        # No events left
        events = tl.advance_by_delta(timedelta(days=1))
        self.assertEqual(len(events), 0)
        self.assertEqual(len(tl.future), 0)
        self.assertEqual(len(tl.past), self.NUM_EVENTS)

    def test_advance_by_larger_delta(self):
        tl = self._create_timeline()

        step_size = 5
        for i in range(1+step_size, step_size, self.NUM_EVENTS + 1):
            events = tl.advance_by_delta(timedelta(days=step_size))
            self.assertEqual(len(events), step_size)
            for j in range(0, step_size):
                self.assertEqual(events[j].description, f"Event {i+j}")
            self.assertEqual(len(tl.future), self.NUM_EVENTS-i)
            self.assertEqual(len(tl.past), i)

    def test_advance_by_larger_delta_or_event(self):
        tl = self._create_timeline()

        step_size = 5
        for i in range(1, self.NUM_EVENTS + 1):
            event = tl.advance_by_delta_or_event(timedelta(days=step_size))
            self.assertEqual(event.description, f"Event {i}")
            self.assertEqual(len(tl.future), self.NUM_EVENTS-i)
            self.assertEqual(len(tl.past), i)

        self.assertEqual(tl.now, event.time)

        # no events left
        end_time = event.time + timedelta(days=step_size)
        event = tl.advance_by_delta_or_event(timedelta(days=step_size))
        self.assertIsNone(event)
        self.assertEqual(len(tl.future), 0)
        self.assertEqual(len(tl.past), 15)
        self.assertEqual(tl.now, end_time)

    def test_advance_to_large_time_or_event(self):
        tl = self._create_timeline()

        end = tl.now + timedelta(days=10 * self.NUM_EVENTS)
        for i in range(1, self.NUM_EVENTS + 1):
            event = tl.advance_to_time_or_event(end)
            self.assertEqual(event.description, f"Event {i}")
            self.assertEqual(len(tl.future), self.NUM_EVENTS-i)
            self.assertEqual(len(tl.past), i)

        self.assertEqual(tl.now, event.time)

        # no events left
        event = tl.advance_to_time_or_event(end)
        self.assertIsNone(event)
        self.assertEqual(len(tl.future), 0)
        self.assertEqual(len(tl.past), 15)
        self.assertEqual(tl.now, end)

    def test_advance_to_time(self):
        tl = self._create_timeline()
        for i in range(1, self.NUM_EVENTS + 1):
            events = tl.advance_to_time(datetime(year=1, month=1, day=i+1))
            self.assertEqual(len(events), 1)
            self.assertEqual(events[0].description, f"Event {i}")
            self.assertEqual(len(tl.future), self.NUM_EVENTS-i)
            self.assertEqual(len(tl.past), i)

        # No events left
        events = tl.advance_by_delta(timedelta(days=1))
        self.assertEqual(len(events), 0)
        self.assertEqual(len(tl.future), 0)
        self.assertEqual(len(tl.past), self.NUM_EVENTS)

        # past
        events = tl.advance_to_time(datetime(year=1, month=1, day=10))
        self.assertEqual(len(events), 0)
        self.assertEqual(len(tl.future), 6)
        self.assertEqual(len(tl.past), 9)

        for i in range(10, self.NUM_EVENTS + 1):
            events = tl.advance_to_time(datetime(year=1, month=1, day=i+1))
            self.assertEqual(len(events), 1)
            self.assertEqual(events[0].description, f"Event {i}")
            self.assertEqual(len(tl.future), self.NUM_EVENTS-i)
            self.assertEqual(len(tl.past), i)

    def test_advance_to_time_big_step(self):
        tl = self._create_timeline()

        step_size = 5
        for i in range(1+step_size, step_size, self.NUM_EVENTS + 1):
            events = tl.advance_to_time(datetime(year=1, month=1, day=i))
            self.assertEqual(len(events), step_size)
            for j in range(0, step_size):
                self.assertEqual(events[j].description, f"Event {i+j}")
            self.assertEqual(len(tl.future), self.NUM_EVENTS-i)
            self.assertEqual(len(tl.past), i)

    def test_advance_to_next_event(self):
        tl = self._create_timeline()

        for i in range(self.NUM_EVENTS):
            event = tl.advance_to_next_event()
            self.assertEqual(event.description, f"Event {i+1}")
            self.assertEqual(len(tl.future), self.NUM_EVENTS-i-1)
            self.assertEqual(len(tl.past), i+1)

        # no events left
        with self.assertRaises(Exception):
            tl.advance_to_next_event()

    def test_print(self):
        tl = self._create_timeline()
        event = tl.advance_to_next_event()
        print(tl)

    def test_not_in_order_adding(self):
        tl = Timeline()
        events = []
        events_ordered = []
        for i in range(1, self.NUM_EVENTS + 1):
            e = Event(f"Event {i}", datetime(
                1, 1, i, hour=i, minute=i, second=i))
            events.append(e)
            events_ordered.append(e)

        random.shuffle(events)

        for event in events:
            tl.add_event(event)

        self.assertEqual(len(tl.future), self.NUM_EVENTS)
        self.assertEqual(len(tl.past), 0)

        # check that events are ordered
        self.assertListEqual(tl.future, events_ordered)

    def test_save(self):
        tl = self._create_timeline()
        with tempfile.TemporaryDirectory() as fol:
            filename = Path(fol) / "testTimeline.pkl"

            save_timeline(filename, tl)

            tl2 = load_timeline(filename)

        self.assertEqual(len(tl2.future), self.NUM_EVENTS)
        self.assertEqual(len(tl2.past), 0)

        self.assertListEqual(tl.future, tl2.future)


if __name__ == '__main__':
    unittest.main()
