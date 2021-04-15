#!/usr/bin/env python3

class Bonus(object):
    def __init__(self, value: int, explanation: str):
        super().__init__()
        self.__value = value
        self.__explanation = explanation

    @property
    def value(self):
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
        return self.__value + sum([bonus.value for bonus in self.__bonus])

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

    def __repr__(self):
        return self.name


class Atribut(Characteristic):
    pass


class Ability(Characteristic):
    def __init__(self, name: str, atribut: Atribut):
        super().__init__(name)
        self.__atribut = atribut

    @property
    def atribut(self):
        return self.__atribut

    @property
    def maxed(self):
        return self.value >= self.atribut.value

    def increase_value(self):
        if self.maxed:
            raise ValueError(
                f"Ability {self.name} is at its current max. Increase {self.atribut.name} first.")
        super().increase_value()


class Charactersheet(object):
    def __init__(self, atribute_ability_mapping: dict):
        self._atributes = []
        self._abilities = []

        for atribute_name, ability_names in atribute_ability_mapping.items():
            atribut = Atribut(atribute_name)
            for ability_name in ability_names:
                self._abilities.append(Ability(ability_name, atribut))
            self._atributes.append(atribut)

    @property
    def atributes(self):
        return self._atributes

    @property
    def abilities(self):
        return self._abilities
