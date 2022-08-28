#!/usr/bin/env python3
from abc import ABC, abstractmethod
from logger import Logger


class Bonus(object):
    def __init__(self, value: int, explanation: str):
        super().__init__()
        self.__value = value
        self.__explanation = explanation

    @property
    def value(self):
        return self.__value

    def __str__(self):
        if self.value > 0:
            return f"+{self.value} ({self.__explanation}) "
        return f"{self.value} ({self.__explanation}) "

    def __int__(self):
        return self.__value


class Characteristic(object):
    def __init__(self, name: str):
        super().__init__()
        self.__name = name
        self.__value = 0
        self.__bonus = []
        self.__max_value = 20

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val: int):
        self.__value = val

    def increase_value(self):
        if self.__value >= self.__max_value:
            raise ValueError("Cannot increase value above maximum")

        self.__value += 1

    def decrease_value(self):
        if self.__value - 1 < 0:
            raise ValueError("Cannot decrease value below zero.")

        self.__value -= 1

    def add_bonus(self, value: int, explanation: str):
        if value < 0:
            raise ValueError("value must be positive")

        self.__bonus.append(Bonus(value=value, explanation=explanation))

    def add_malus(self, value: int, explanation: str):
        if value < 0:
            raise ValueError("value must be positive")

        self.__bonus.append(Bonus(value=-value, explanation=explanation))

    @property
    def name(self):
        return self.__name

    @property
    def bonus(self):
        return self.__bonus

    @property
    def bonus_value(self):
        return sum([int(b) for b in self.__bonus])

    @property
    def total_value(self):
        return self.value + self.bonus_value

    def __str__(self):
        return self.name

    def __int__(self):
        return self.value

    def __float__(self):
        return float(self.value)

    def __mul__(self, other):
        return int(self) * other

    def __rmul__(self, other):
        return int(self) * other

    def __floordiv__(self, other):
        return int(self) // other

    def __truediv__(self, other):
        return float(self) / other

    def __rmul__(self, other):
        return int(self) * other

    def __repr__(self):
        return f"{self.name}: {self.value}"


class Attribut(Characteristic):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.abilities = {}

    def addAbility(self, ability: "Ability"):
        self.abilities[ability.name] = ability


class Ability(Characteristic):
    def __init__(self, name: str, attribut: Attribut):
        super().__init__(name)
        self.__attribut = attribut

    @property
    def attribut(self):
        return self.__attribut

    @property
    def maxed(self):
        return self.value >= self.attribut.value

    def increase_value(self):
        if self.maxed:
            raise ValueError(
                f"Ability {self.name} is at its current max. Increase {self.attribut.name} first.")
        super().increase_value()


class Charactersheet(ABC):
    @property
    @abstractmethod
    def attribute_ability_mapping(self) -> dict:
        pass

    @property
    @abstractmethod
    def max_life(self):
        pass

    @property
    @abstractmethod
    def max_carry_weight(self):
        pass

    @property
    @abstractmethod
    def defense_ranged(self):
        pass

    @property
    @abstractmethod
    def defense_melee(self):
        pass

    @property
    @abstractmethod
    def attack(self):
        pass

    @property
    @abstractmethod
    def dmg(self):
        pass

    @property
    def fight_speed(self):
        return 1

    def __init__(self):
        # TODO: can logger be None?
        # add baseclass: Loggable
        self._attributes = {}
        self._abilities = {}
        self.level = 0

        for attribute_name, ability_names in self.attribute_ability_mapping.items():
            attribut = Attribut(attribute_name)
            for ability_name in ability_names:
                ability = Ability(ability_name, attribut)
                self._abilities[ability.name] = ability
                attribut.addAbility(ability)
                setattr(self, str(ability), ability)

            setattr(self, str(attribut), attribut)
            self._attributes[attribut.name] = attribut

    @property
    def attributes(self):
        return self._attributes

    @property
    def abilities(self):
        return self._abilities
