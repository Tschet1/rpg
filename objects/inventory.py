#!/usr/bin/env python3

import copy
from objects.item import Item
from collections import defaultdict
from typing import Union

class Inventory(object):
    class InventoryItem(object):
        def __init__(self, item, value_known=False, stats_known=False, count=1):
            super().__init__()
            self.name = item.name
            self.value_known = value_known
            self.stats_known = stats_known
            self.count = count
            self.item = item

        def learn_value(self):
            self.value_known = True

        def learn_stats(self):
            self.stats_known = True

        def add(self, count=1):
            self.count += count

        def remove(self, count=1):
            if self.count < count:
                raise Exception(f"Tried to remove {count} {self.name} but only has {self.count}")
            self.count -= count


    def __init__(self, logger):
        super().__init__()
        self.__logger = logger
        self.__items = {}

    def add_item(self, item: Item, count: int = 1):
        if count <= 0:
            raise Exception(f"Must add at least one piece of {item.name}")

        if not item.name in self.__items:
            self.__items[item.name] = Inventory.InventoryItem(item)

        self.__items[item.name].add(count)
        self.__logger.log(f"Received {count} {item.name}")

    def remove_item(self, item: Union[str, Item], count: int = 1):
        name = item if isinstance(item, str) else item.name

        if not name in self.__items:
            raise Exception(f"{item.name} not in inventory.")

        self.__items[name].remove(count)
        self.__logger.log(f"Removed {count} {item.name}")

    def learn_value(self, item: Union[str, Item]):
        name = item if isinstance(item, str) else item.name

        if not name in self.__items:
            raise Exception(f"{item.name} not in inventory.")

        self.__items[name].learn_value()
        self.__logger.log(f"Learned the value of {item.name}")

    def learn_stats(self, item: Union[str, Item]):
        name = item if isinstance(item, str) else item.name

        if not name in self.__items:
            raise Exception(f"{item.name} not in inventory.")

        self.__items[name].learn_stats()
        self.__logger.log(f"Learned the stats of {item.name}")

    @property
    def items_full(self):
        return [
            (
                it.name,
                it.item.value,
                it.item.weight,
                it.item.info,
                it.count)
                    for it in self.__items.values()
        ]

    @property
    def items(self):
        return [
            (
                it.name,
                it.item.value if it.value_known else "?",
                it.item.weight,
                it.item.info if it.stats_known else "?",
                it.count
            )
                    for it in self.__items.values()
        ]

    # Way to access items. Get function with name?
