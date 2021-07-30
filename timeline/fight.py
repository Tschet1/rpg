#!/usr/bin/env python3

import bisect
from timeline.timeline import Timeline, Event
from objects.person import Person
from datetime import timedelta


class Fight(Timeline):
    def add_person(self, person: Person):
        self.add_event(Event(person.name, self.now +
                       timedelta(milliseconds=1), state=person))
        # TODO make sure that person is not already added

    def get_next_combatant(self):
        evt = self.advance_to_next_event()
        name = evt.description
        fight_speed = (1/evt.state.fight_speed)

        # schedule the next fight
        self.add_event(
            Event(name, self.now + timedelta(seconds=fight_speed), state=evt.state))

        if evt.state is not None:
            return evt.state
        return name

    def remove_combatant(self, person: Person):
        future_start = self._Timeline__now_idx
        self._Timeline__events[future_start:] = list(
            filter(lambda evt: evt.state != person, self._Timeline__events[future_start:]))
