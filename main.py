"""
by: LarsCD2002
started: 6/1/2024

SOURCES
    - Nebulous: Fleet Command (inspiration for ship/system stats)
    - https://www.youtube.com/watch?v=bImISkF76T8 (inspiration for ship/system stats)


"""

"""
FileIO testing
Testing if importing data works right 
"""
from src.engine.utilities.file_IO.dataloader import Dataloader

STATIC_DATA = Dataloader().load_all_data()
print(STATIC_DATA)

print("""-------------------------------- [VESSEL INFO] --------------------------------

[USS CLASS DESTROYER]

OVERALL HP:     (801/1250)    [/////////////////////......]
POWER OUTPUT:   (670/800)     [///////////////////////....]
POWER USAGE:    (670/800)     [///////////////////////....]
SIGNATURE:      (80/100)      [///////////////////////....]

[MODULE]        [STATUS]    [WARNINGS]  [DANGERS]
REACTOR         ONLINE      LOW POWER   CRITICAL 
CONTROL         ONLINE
THRUSTERS       ONLINE      DAMAGED
SENSORS         OFFLINE     NO POWER
WEAPONS         ONLINE      DAMAGED

-------------------------------- [PRIMARY MODULES] --------------------------------
OVERALL HP:         801/1250    [/////////////////////......]

MODULES
<REACTOR (CFR 800 REACTOR)>
- HP:               (180/200)     [///////////////////////////]
- POWER OUTPUT:     (670/800)     [///////////////////////....]

<DRIVE (VULCAN 2 MEDIUM DRIVE)>
- HP:               (300/300)     [///////////////////////////]
- JUMP RANGE:       (20/20) ly    [///////////////////////////]
- POWER USAGE:      (670/800)     [///////////////////////....]


-------------------------------- [DEFENCE MODULES] --------------------------------
OVERALL HP:         801/1250    [/////////////////////......]

<SHIELD (CFR 800 REACTOR)>
- HP:               180/200     [///////////////////////////]
- POWER OUTPUT:     670/800     [///////////////////////....]
- POWER USAGE:      670/800     [///////////////////////....]

<ARMOR (CFR 800 REACTOR)>
- HP:               180/200     [///////////////////////////]
- POWER OUTPUT:     670/800     [///////////////////////....]

<HULL (CFR 800 REACTOR)>
- HP:               180/200     [///////////////////////////]
- POWER OUTPUT:     670/800     [///////////////////////....]


-------------------------------- [COMBAT MODULES] --------------------------------
OVERALL HP:         801/1250    [/////////////////////......]


[1] <WEAPON (TT10 Cannon)> [☒ DESTROYED ☒]
- HP:               0/70        [...........................]
- AMMO HOLD:        670/800     [///////////////////////....]
- POWER USAGE:      670/800     [///////////////////////....]
[2] <WEAPON (TT10 Cannon)> [🔃 RELOADING 🔃]
- HP:               12/70       [//////.....................]
- AMMO HOLD:        0/24        [...........................]
- POWER USAGE:      670/800     [///////////////////////....]
[3] <WEAPON (PDS 10 Defence)>
- HP:               10/10       [///////////////////////////]
- AMMO HOLD:        670/800     [///////////////////////....]
- POWER USAGE:      670/800     [///////////////////////....]

[4] <MAGAZINE (20mm Small Magazine)>
- HP:               180/200     [///////////////////////////]
- AMMO HOLD:        2780/5000   [///////////////............]
[5] <MAGAZINE (50mm Small Magazine)>
- HP:               180/200     [///////////////////////////]
- AMMO HOLD:        22/140      [///........................]
[6] <MAGAZINE (50mm Small Magazine)>
- HP:               180/200     [///////////////////////////]
- AMMO HOLD:        140/140     [///////////////////////////]



-------------------------------- [MANEUVERING MODULES] --------------------------------
OVERALL HP:         801/1250    [/////////////////////......]

<CONTROL (CFR 800 REACTOR)> -
- HP:               180/200     [///////////////////////////]
- POWER OUTPUT:     670/800     [///////////////////////....]
- POWER USAGE:      670/800     [///////////////////////....]

<THRUSTER (CFR 800 REACTOR)>
- HP:               180/200     [///////////////////////////]
- POWER OUTPUT:     670/800     [///////////////////////....]
- POWER USAGE:      670/800     [///////////////////////....]
<THRUSTER (CFR 800 REACTOR)>
- HP:               180/200     [///////////////////////////]
- POWER OUTPUT:     670/800     [///////////////////////....]
- POWER USAGE:      670/800     [///////////////////////....]
""")

"""
Creating classes
Testing if creation of all classes works
"""
input('\n[ENTER]: EXIT')
