#!/usr/bin/env python3

from charactersheet.sheet import Charactersheet
from objects.item import SingleHandMeleeWeapon, RangedWeapon, TwoHandedWeapon
from numpy import mean


class System(Charactersheet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.weapon = None

    @property
    def attribute_ability_mapping(self) -> dict:
        return {
            "Gesundheit": [],
            "Tragekapazität": [],
            "Agilität": [
                "Rennen",
            ],
            "Stärke": [
                "Klettern & Springen",
                "Schwimmen",
                "Zähigkeit",
                "Einschüchtern",
                "Fauskampf",
            ],
            "Geschicklichkeit": [
                "Reiten",
                "Heimlichkeit",
                "Schlösser Knacken",
                "Parieren",
                "Reflexe",
            ],
            "Intelligenz": [
                "Tränke",
                "Erste Hilfe",
                "Improvisieren",
                "Kulturelles Wissen",
                "Naturkunde",
                "Gerätebedienung"
            ],
            "Sinnesstärke": [
                "Wahrnehmung",
                "Spuren lesen",
                "Menschenkenntnis"
            ],
            "Soziales": [
                "Überreden",
                "Feilschen",
                "Täuschen und Lügen",
                "Willensstärke"
            ],
            "Fernkampf": [
                "Wurfwaffen",
                "Bogen",
                "Armbrüste"
            ],
            "Einhandwaffen": [
                "Dolche",
                "Schwerter",
                "Degen",
                "Käulen"
            ],
            "Zweihandwaffen": [
                "Breitschwerter",
                "Stangenwaffen",
                "Äxte",
            ],
        }

    @property
    def max_life(self):
        return self.Gesundheit * 4

    @property
    def fight_speed(self):
        return (self.Agilität / 10) + 1

    @property
    def max_carry_weight(self):
        return self.Tragekapazität * 5 + 5

    @property
    def defense_ranged(self):
        return self.Reflexe

    @property
    def defense_melee(self):
        return self.Parieren

    @property
    def attack(self):
        at = self.abilities[self.weapon.related_skill].attribut
        return at.value + round(mean([int(ab) for ab in at.abilities.values()]))

    @property
    def dmg(self):
        # TODO: fix:
        #   why ITEMS as list?

        ability = self.abilities[self.weapon.related_skill]
        attribut = ability.attribut
        return self.weapon.damage + attribut.value // 5
