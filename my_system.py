#!/usr/bin/env python3

from charactersheet.sheet import Charactersheet


class System(Charactersheet):
    @property
    def attribute_ability_mapping(self) -> dict:
        return {
            "Health": [],
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
            ],
        }

    @property
    def max_life(self):
        return self.Health * 4

    @property
    def fight_speed(self):
        return (self.Agilität / 10) + 1
