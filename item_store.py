#!/usr/bin/env python3
from objects.item import *
from die.dices import *

ITEMS = [
    Dagger(name="Holzdolch",        value=10,  weight=1,  required_skill=1, damage=D4, crit_chance=19, crit_mult=3, crit_effect="", dual_wield_skill=3),
    Dagger(name="Bronzedolch",      value=30,  weight=2,  required_skill=2, damage=D6, crit_chance=19, crit_mult=3, crit_effect="", dual_wield_skill=5),
    Dagger(name="Eisendolch",       value=50,  weight=3,  required_skill=3, damage=D6, crit_chance=19, crit_mult=3, crit_effect="", dual_wield_skill=6),
    Dagger(name="Knochendolch",     value=200, weight=3,  required_skill=6, damage=D8, crit_chance=19, crit_mult=3, crit_effect="", dual_wield_skill=10),
    Dagger(name="Demeritiumdolch",  value=500, weight=1,  required_skill=6, damage=D8, crit_chance=19, crit_mult=3, crit_effect="", dual_wield_skill=10),

    Sword(name="Holzschwert",        value=50,   weight=3,  required_skill=1, damage=D6,  crit_chance=20, crit_mult=2, crit_effect="", dual_wield_skill=6),
    Sword(name="Bronzeschwert",      value=100,  weight=6,  required_skill=2, damage=D8,  crit_chance=20, crit_mult=2, crit_effect="", dual_wield_skill=8),
    Sword(name="Eisenschwert",       value=120,  weight=8,  required_skill=3, damage=D10, crit_chance=20, crit_mult=2, crit_effect="", dual_wield_skill=12),
    Sword(name="Knochenschwert",     value=400,  weight=12, required_skill=7, damage=D12, crit_chance=20, crit_mult=2, crit_effect="", dual_wield_skill=18),
    Sword(name="Demeritiumschwert",  value=1000, weight=10, required_skill=7, damage=D12, crit_chance=20, crit_mult=2, crit_effect="", dual_wield_skill=18),

    TwoHandedWeapon(name="Holzzweihänder",        value=50,   weight=6,  required_skill=1, damage=D8,  crit_chance=20, crit_mult=2, crit_effect="", reach=1),
    TwoHandedWeapon(name="Bronzezweihänder",      value=150,  weight=12, required_skill=2, damage=D10, crit_chance=20, crit_mult=2, crit_effect="", reach=1),
    TwoHandedWeapon(name="Eisenzweihänder",       value=200,  weight=15, required_skill=3, damage=D12, crit_chance=20, crit_mult=2, crit_effect="", reach=1),
    TwoHandedWeapon(name="Knochenzweihänder",     value=600,  weight=18, required_skill=6, damage=D20, crit_chance=20, crit_mult=2, crit_effect="", reach=1),
    TwoHandedWeapon(name="Demeritiumzweihänder",  value=1200, weight=14, required_skill=6, damage=D20, crit_chance=20, crit_mult=2, crit_effect="", reach=1),

    TwoHandedWeapon(name="Holzspeer",        value=50,   weight=3,  required_skill=1, damage=D6,  crit_chance=20, crit_mult=2, crit_effect="", reach=2),
    TwoHandedWeapon(name="Bronzespeer",      value=150,  weight=5,  required_skill=2, damage=D8, crit_chance=20, crit_mult=2, crit_effect="", reach=2),
    TwoHandedWeapon(name="Eisenspeer",       value=200,  weight=7,  required_skill=3, damage=D10, crit_chance=20, crit_mult=2, crit_effect="", reach=2),
    TwoHandedWeapon(name="Knochenspeer",     value=600,  weight=10, required_skill=6, damage=D12, crit_chance=20, crit_mult=2, crit_effect="", reach=2),
    TwoHandedWeapon(name="Demeritiumspeer",  value=1200, weight=8,  required_skill=6, damage=D12, crit_chance=20, crit_mult=2, crit_effect="", reach=2),

    TwoHandedWeapon(name="Holzdreizack",        value=50,   weight=4,  required_skill=3,  damage=D8,  crit_chance=20, crit_mult=2, crit_effect="", reach=2),
    TwoHandedWeapon(name="Bronzedreizack",      value=150,  weight=6,  required_skill=5,  damage=D10, crit_chance=20, crit_mult=2, crit_effect="",  reach=2),
    TwoHandedWeapon(name="Eisendreizack",       value=200,  weight=8,  required_skill=8,  damage=D12, crit_chance=20, crit_mult=2, crit_effect="", reach=2),
    TwoHandedWeapon(name="Knochendreizack",     value=600,  weight=12, required_skill=12, damage=D20, crit_chance=20, crit_mult=2, crit_effect="", reach=2),
    TwoHandedWeapon(name="Demeritiumdreizack",  value=1200, weight=10, required_skill=12, damage=D20, crit_chance=20, crit_mult=2, crit_effect="", reach=2),

    TwoHandedWeapon(name="Holz-Streitaxt",        value=50,   weight=8,  required_skill=4,  damage=D8,  crit_chance=20, crit_mult=2, crit_effect="", reach=2),
    TwoHandedWeapon(name="Bronze-Streitaxt",      value=150,  weight=14, required_skill=5,  damage=D10, crit_chance=20, crit_mult=2, crit_effect="",  reach=2),
    TwoHandedWeapon(name="Eisen-Streitaxt",       value=200,  weight=18, required_skill=8,  damage=D12, crit_chance=20, crit_mult=2, crit_effect="", reach=2),
    TwoHandedWeapon(name="Knochen-Streitaxt",     value=600,  weight=24, required_skill=12, damage=D20, crit_chance=20, crit_mult=2, crit_effect="", reach=2),
    TwoHandedWeapon(name="Demeritium-Streitaxt",  value=1200, weight=22, required_skill=12, damage=D20, crit_chance=20, crit_mult=2, crit_effect="", reach=2),

    Whip(name="Peitsche", value=100,  weight=2,  required_skill=2, damage=D6, crit_chance=20, crit_mult=2, crit_effect="", reach=3, dual_wield_skill=4),
    Whip(name="Peitsche", value=100,  weight=2,  required_skill=2, damage=D6, crit_chance=20, crit_mult=2, crit_effect="", reach=3, dual_wield_skill=4),

    Bow(name="Bogen",         value=50,   weight=4,  required_skill=1,  damage=D4,  crit_chance=19, crit_mult=2, crit_effect="", reach=8),
    Bow(name="Jagdbogen",     value=100,  weight=5,  required_skill=2,  damage=D6,  crit_chance=19, crit_mult=2, crit_effect="", reach=10),
    Bow(name="Langbogen",     value=150,  weight=6,  required_skill=4,  damage=D8,  crit_chance=19, crit_mult=2, crit_effect="", reach=10),
    Bow(name="Streitbogen",   value=200,  weight=8,  required_skill=6,  damage=D12, crit_chance=19, crit_mult=2, crit_effect="", reach=12),
    Bow(name="Kompositbogen", value=800,  weight=12, required_skill=8,  damage="D14 + 2", crit_chance=18, crit_mult=2, crit_effect="", reach=14),
    Bow(name="Knochenbogen",  value=1500, weight=18, required_skill=12, damage="D14 + 2", crit_chance=19, crit_mult=3, crit_effect="", reach=18),
    Bow(name="Metallbogen",   value=1800, weight=20, required_skill=16, damage=D12, crit_chance=20, crit_mult=2, crit_effect="", reach=2),

    #Crossbow("Armbrust", value, weight, required_skill, damage, crit_chance, crit_mult, crit_effect, reach, name, value, weight, required_skill, damage, crit_chance, crit_mult, crit_effect, reach)(name="Armbrust",             value=50,   weight=6,  required_skill=1,  damage=D4,  crit_chance=20, crit_mult=2, crit_effect="", reach=6),
    #Crossbow("Armbrust", value, weight, required_skill, damage, crit_chance, crit_mult, crit_effect, reach, name, value, weight, required_skill, damage, crit_chance, crit_mult, crit_effect, reach)(name="Beschlagene Armbrust", value=100,  weight=8,  required_skill=4,  damage=D8,  crit_chance=20, crit_mult=2, crit_effect="", reach=8),
    #Crossbow("Armbrust", value, weight, required_skill, damage, crit_chance, crit_mult, crit_effect, reach, name, value, weight, required_skill, damage, crit_chance, crit_mult, crit_effect, reach)(name="Kriegsarmbrust",       value=300,  weight=10, required_skill=6,  damage=D10, crit_chance=20, crit_mult=2, crit_effect="", reach=8),
    #Crossbow("Armbrust", value, weight, required_skill, damage, crit_chance, crit_mult, crit_effect, reach, name, value, weight, required_skill, damage, crit_chance, crit_mult, crit_effect, reach)(name="Knochenarmbrust",      value=800,  weight=12, required_skill=12, damage=D12, crit_chance=20, crit_mult=2, crit_effect="", reach=9),
    #Crossbow("Armbrust", value, weight, required_skill, damage, crit_chance, crit_mult, crit_effect, reach, name, value, weight, required_skill, damage, crit_chance, crit_mult, crit_effect, reach)(name="Einhornarmbrust",      value=2000, weight=16, required_skill=16, damage=D20, crit_chance=20, crit_mult=2, crit_effect="", reach=8),

    ThrowingWeapons("Stein",    value=0,  weight=1, required_skill=1, damage=D2, crit_chance=20, crit_mult=2, crit_effect="", reach=4),
    ThrowingWeapons("Bierglas", value=5,  weight=1, required_skill=1, damage=D2, crit_chance=19, crit_mult=2, crit_effect="", reach=4),
    ThrowingWeapons("Wurfdolch",value=10, weight=1, required_skill=2, damage=D4, crit_chance=19, crit_mult=2, crit_effect="", reach=6),
    ThrowingWeapons("Wurfbeil", value=20, weight=2, required_skill=3, damage=D6, crit_chance=20, crit_mult=2, crit_effect="", reach=6),

    #ThrowingWeapons("Stein", 10, 1, 1, , CRI_chance, crit_mult, crit_effect, reach, name, value, weight, required_skill, damage, crit_chance, crit_mult, crit_effect, reach)
]
