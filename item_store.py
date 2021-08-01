#!/usr/bin/env python3
from objects.item import *
from die.dices import *

ITEMS = [
    Dagger(name="Holzdolch",        related_skill="Dolche", value=10,  weight=1,  required_skill=1, damage=D4, crit_chance=19, crit_mult=3, crit_effect="", dual_wield_skill=3),
    Dagger(name="Bronzedolch",      related_skill="Dolche", value=30,  weight=2,  required_skill=2, damage=D6, crit_chance=19, crit_mult=3, crit_effect="", dual_wield_skill=5),
    Dagger(name="Eisendolch",       related_skill="Dolche", value=50,  weight=3,  required_skill=3, damage=D6, crit_chance=19, crit_mult=3, crit_effect="", dual_wield_skill=6),
    Dagger(name="Knochendolch",     related_skill="Dolche", value=200, weight=3,  required_skill=6, damage=D8, crit_chance=19, crit_mult=3, crit_effect="", dual_wield_skill=10),
    Dagger(name="Demeritiumdolch",  related_skill="Dolche", value=500, weight=1,  required_skill=6, damage=D8, crit_chance=19, crit_mult=3, crit_effect="", dual_wield_skill=10),

    Sword(name="Holzschwert",       related_skill="Schwerter", value=50,   weight=3,  required_skill=1, damage=D6,  crit_chance=20, crit_mult=2, crit_effect="", dual_wield_skill=6),
    Sword(name="Bronzeschwert",     related_skill="Schwerter", value=100,  weight=6,  required_skill=2, damage=D8,  crit_chance=20, crit_mult=2, crit_effect="", dual_wield_skill=8),
    Sword(name="Eisenschwert",      related_skill="Schwerter", value=120,  weight=8,  required_skill=3, damage=D10, crit_chance=20, crit_mult=2, crit_effect="", dual_wield_skill=12),
    Sword(name="Knochenschwert",    related_skill="Schwerter", value=400,  weight=12, required_skill=7, damage=D12, crit_chance=20, crit_mult=2, crit_effect="", dual_wield_skill=18),
    Sword(name="Demeritiumschwert", related_skill="Schwerter", value=1000, weight=10, required_skill=7, damage=D12, crit_chance=20, crit_mult=2, crit_effect="", dual_wield_skill=18),

    TwoHandedWeapon(name="Holzzweihänder",       related_skill="Breitschwert", value=50,   weight=6,  required_skill=1, damage=D8,  crit_chance=20, crit_mult=2, crit_effect="", reach=1),
    TwoHandedWeapon(name="Bronzezweihänder",     related_skill="Breitschwert", value=150,  weight=12, required_skill=2, damage=D10, crit_chance=20, crit_mult=2, crit_effect="", reach=1),
    TwoHandedWeapon(name="Eisenzweihänder",      related_skill="Breitschwert", value=200,  weight=15, required_skill=3, damage=D12, crit_chance=20, crit_mult=2, crit_effect="", reach=1),
    TwoHandedWeapon(name="Knochenzweihänder",    related_skill="Breitschwert", value=600,  weight=18, required_skill=6, damage=D20, crit_chance=20, crit_mult=2, crit_effect="", reach=1),
    TwoHandedWeapon(name="Demeritiumzweihänder", related_skill="Breitschwert", value=1200, weight=14, required_skill=6, damage=D20, crit_chance=20, crit_mult=2, crit_effect="", reach=1),

    TwoHandedWeapon(name="Holzspeer",        related_skill="Stangenwaffen", value=50,   weight=3,  required_skill=1, damage=D6,  crit_chance=20, crit_mult=2, crit_effect="", reach=2),
    TwoHandedWeapon(name="Bronzespeer",      related_skill="Stangenwaffen", value=150,  weight=5,  required_skill=2, damage=D8, crit_chance=20, crit_mult=2, crit_effect="", reach=2),
    TwoHandedWeapon(name="Eisenspeer",       related_skill="Stangenwaffen", value=200,  weight=7,  required_skill=3, damage=D10, crit_chance=20, crit_mult=2, crit_effect="", reach=2),
    TwoHandedWeapon(name="Knochenspeer",     related_skill="Stangenwaffen", value=600,  weight=10, required_skill=6, damage=D12, crit_chance=20, crit_mult=2, crit_effect="", reach=2),
    TwoHandedWeapon(name="Demeritiumspeer",  related_skill="Stangenwaffen", value=1200, weight=8,  required_skill=6, damage=D12, crit_chance=20, crit_mult=2, crit_effect="", reach=2),

    TwoHandedWeapon(name="Holzdreizack",       related_skill="Stangenwaffen", value=50,   weight=4,  required_skill=3,  damage=D8,  crit_chance=20, crit_mult=2, crit_effect="", reach=2),
    TwoHandedWeapon(name="Bronzedreizack",     related_skill="Stangenwaffen", value=150,  weight=6,  required_skill=5,  damage=D10, crit_chance=20, crit_mult=2, crit_effect="",  reach=2),
    TwoHandedWeapon(name="Eisendreizack",      related_skill="Stangenwaffen", value=200,  weight=8,  required_skill=8,  damage=D12, crit_chance=20, crit_mult=2, crit_effect="", reach=2),
    TwoHandedWeapon(name="Knochendreizack",    related_skill="Stangenwaffen", value=600,  weight=12, required_skill=12, damage=D20, crit_chance=20, crit_mult=2, crit_effect="", reach=2),
    TwoHandedWeapon(name="Demeritiumdreizack", related_skill="Stangenwaffen", value=1200, weight=10, required_skill=12, damage=D20, crit_chance=20, crit_mult=2, crit_effect="", reach=2),

    TwoHandedWeapon(name="Holz-Streitaxt",       related_skill="Äxte", value=50,   weight=8,  required_skill=4,  damage=D8,  crit_chance=20, crit_mult=2, crit_effect="", reach=2),
    TwoHandedWeapon(name="Bronze-Streitaxt",     related_skill="Äxte", value=150,  weight=14, required_skill=5,  damage=D10, crit_chance=20, crit_mult=2, crit_effect="",  reach=2),
    TwoHandedWeapon(name="Eisen-Streitaxt",      related_skill="Äxte", value=200,  weight=18, required_skill=8,  damage=D12, crit_chance=20, crit_mult=2, crit_effect="", reach=2),
    TwoHandedWeapon(name="Knochen-Streitaxt",    related_skill="Äxte", value=600,  weight=24, required_skill=12, damage=D20, crit_chance=20, crit_mult=2, crit_effect="", reach=2),
    TwoHandedWeapon(name="Demeritium-Streitaxt", related_skill="Äxte", value=1200, weight=22, required_skill=12, damage=D20, crit_chance=20, crit_mult=2, crit_effect="", reach=2),

    Whip(name="Peitsche", related_skill="Dolche", value=100,  weight=2,  required_skill=2, damage=D6, crit_chance=20, crit_mult=2, crit_effect="", reach=3, dual_wield_skill=4),
    Whip(name="Peitsche", related_skill="Dolche", value=100,  weight=2,  required_skill=2, damage=D6, crit_chance=20, crit_mult=2, crit_effect="", reach=3, dual_wield_skill=4),

    Bow(name="Bogen",         related_skill="Bogen", value=50,   weight=4,  required_skill=1,  damage=D4,  crit_chance=19, crit_mult=2, crit_effect="", reach=8),
    Bow(name="Jagdbogen",     related_skill="Bogen", value=100,  weight=5,  required_skill=2,  damage=D6,  crit_chance=19, crit_mult=2, crit_effect="", reach=10),
    Bow(name="Langbogen",     related_skill="Bogen", value=150,  weight=6,  required_skill=4,  damage=D8,  crit_chance=19, crit_mult=2, crit_effect="", reach=10),
    Bow(name="Streitbogen",   related_skill="Bogen", value=200,  weight=8,  required_skill=6,  damage=D12, crit_chance=19, crit_mult=2, crit_effect="", reach=12),
    Bow(name="Kompositbogen", related_skill="Bogen", value=800,  weight=12, required_skill=8,  damage="D14 + 2", crit_chance=18, crit_mult=2, crit_effect="", reach=14),
    Bow(name="Knochenbogen",  related_skill="Bogen", value=1500, weight=18, required_skill=12, damage="D14 + 2", crit_chance=19, crit_mult=3, crit_effect="", reach=18),
    Bow(name="Metallbogen",   related_skill="Bogen", value=1800, weight=20, required_skill=16, damage=D12, crit_chance=20, crit_mult=2, crit_effect="", reach=2),

    #Crossbow("Armbrust", value, weight, required_skill, damage, crit_chance, crit_mult, crit_effect, reach, name, value, weight, required_skill, damage, crit_chance, crit_mult, crit_effect, reach)(name="Armbrust",             value=50,   weight=6,  required_skill=1,  damage=D4,  crit_chance=20, crit_mult=2, crit_effect="", reach=6),
    #Crossbow("Armbrust", value, weight, required_skill, damage, crit_chance, crit_mult, crit_effect, reach, name, value, weight, required_skill, damage, crit_chance, crit_mult, crit_effect, reach)(name="Beschlagene Armbrust", value=100,  weight=8,  required_skill=4,  damage=D8,  crit_chance=20, crit_mult=2, crit_effect="", reach=8),
    #Crossbow("Armbrust", value, weight, required_skill, damage, crit_chance, crit_mult, crit_effect, reach, name, value, weight, required_skill, damage, crit_chance, crit_mult, crit_effect, reach)(name="Kriegsarmbrust",       value=300,  weight=10, required_skill=6,  damage=D10, crit_chance=20, crit_mult=2, crit_effect="", reach=8),
    #Crossbow("Armbrust", value, weight, required_skill, damage, crit_chance, crit_mult, crit_effect, reach, name, value, weight, required_skill, damage, crit_chance, crit_mult, crit_effect, reach)(name="Knochenarmbrust",      value=800,  weight=12, required_skill=12, damage=D12, crit_chance=20, crit_mult=2, crit_effect="", reach=9),
    #Crossbow("Armbrust", value, weight, required_skill, damage, crit_chance, crit_mult, crit_effect, reach, name, value, weight, required_skill, damage, crit_chance, crit_mult, crit_effect, reach)(name="Einhornarmbrust",      value=2000, weight=16, required_skill=16, damage=D20, crit_chance=20, crit_mult=2, crit_effect="", reach=8),

    ThrowingWeapons("Stein",    related_skill="Wurfwaffen", value=0,  weight=1, required_skill=1, damage=D2, crit_chance=20, crit_mult=2, crit_effect="", reach=4),
    ThrowingWeapons("Bierglas", related_skill="Wurfwaffen", value=5,  weight=1, required_skill=1, damage=D2, crit_chance=19, crit_mult=2, crit_effect="", reach=4),
    ThrowingWeapons("Wurfdolch",related_skill="Wurfwaffen", value=10, weight=1, required_skill=2, damage=D4, crit_chance=19, crit_mult=2, crit_effect="", reach=6),
    ThrowingWeapons("Wurfbeil", related_skill="Wurfwaffen", value=20, weight=2, required_skill=3, damage=D6, crit_chance=20, crit_mult=2, crit_effect="", reach=6),

    #ThrowingWeapons("Stein", 10, 1, 1, , CRI_chance, crit_mult, crit_effect, reach, name, value, weight, required_skill, damage, crit_chance, crit_mult, crit_effect, reach)
]
