
import random

mon_strength = ["Regular", "Convergent", "Starter", "God Pokemon", "Fossil", "Pseudo", "Mythical", "Legendary"]
evo_count = [0,1,2,3]
type_count = (0,1,2)
mon_types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison",
    "Ground", "Flying", "Phychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]
starter_main_types = ["Fire", "Water", "Grass", "Electric"]
mon_gimmick = ["None", "Mega Evolution", "Additional Form", "Signiture Move", "Signiture Ability", "Gigantamax", "New Mechanic", "Corrupted", "Shinning"]

def rand_mon_strength():
    global strength
    strength = random.choices(mon_strength, weights=(75,3,15,.5,10,5,1.5,3))
    if debug == True:
        print(f"\n{strength}")
    return strength

debug = False

def rand_evo_count():
    global evolution_stage
    global evolution_stage_type
    evolution_stage_type = ""

    if "Starter" in strength:
        evolution_stage = 2
        evolution_stage_type = "Two Stage"
    else:
        evolution_stage = random.choices(evo_count, weights=(50,25,50,5))[0]
        if debug == True:
            print("Stage Value", evolution_stage)

        if evolution_stage == 0:
            evolution_stage_type = "Basic"
        elif evolution_stage == 1:
            evolution_stage_type = "One Stage"
        elif evolution_stage == 2:
            evolution_stage_type = "Two Stage"
        elif evolution_stage == 3:
            evolution_stage_type = "Three Stage"
    if debug == True:
        print(evolution_stage_type)
    return evolution_stage, evolution_stage_type

def rand_type():
    global monster_type
    if "Starter" in strength:
        a = random.choices(type_count, weights=(0, 50, 50))
        z = (random.choice(a))
        if debug == True:
            print("Type Count: ", z)
        type_1 = random.choice(starter_main_types)
        type_2 = random.choice(mon_types)
        while type_2 == type_1:
            type_2 = random.choice(mon_types)
        monster_type = (type_1, type_2)
        if debug == True:
            print("Type(s): ", monster_type)
    elif "Fossil" in strength:
        a = random.choices(type_count, weights=(0, 50, 50))
        z = (random.choice(a))
        if debug == True:
            print("Type Count: ", z)
        type_1 = (mon_types[12])
        type_2 = random.choice(mon_types)
        while type_2 == type_1:
            type_2 = random.choice(mon_types)
        monster_type = (type_1, type_2)
        if debug == True:
            print("Type(s): ", monster_type)
    else:
        a = random.choices(type_count, weights=(.5, 49.75, 49.75))
        z = (random.choice(a))
        if debug == True:
            print("Type Count: ", z)
        type_1 = random.choice(mon_types)
        type_2 = random.choice(mon_types)
        while type_2 == type_1:
            type_2 = random.choice(mon_types)
        if z == 2:
            monster_type = (type_1, type_2)
        else:
            monster_type = (type_1,)
    if debug == True:
        print("Type(s): ", monster_type[0], monster_type[1] if len(monster_type) > 1 else "")
    return monster_type

def rand_mon_gimmick():
    global gimmick
    special = (0, 10, 45, 25, 15, 0, 5, 5, 5)
    if "God Pokemon" in strength:
        w = special
    elif "Mythical" in strength:
        w = special
    elif "Legendary" in strength:
        w = special
    else:
        w = (50, 20, 20, 15, 10, 15, 5, 5, 5)
    mons_gimmick = random.choices(mon_gimmick, weights=(w))
    gimmick = (random.choice(mons_gimmick))
    if debug == True:
        print("Gimmick: ", gimmick)

def gen_mon():
    rand_mon_strength()
    rand_evo_count()
    rand_type()
    rand_mon_gimmick()

    pokemon = {
        "Category ": strength,
        "Evolution": evolution_stage,
        "Evolution Type": evolution_stage_type,
        "Type 1": monster_type[0],
    }

    if len(monster_type) > 1:
        pokemon["Type 2"] = monster_type[1]

    pokemon["Gimmick"] = gimmick
    return pokemon

for x in range(5):
    random_pokemon = gen_mon()
    print()
    print("Randomly Generated Pokémon:")
    for key, value in random_pokemon.items():
        print(f"{key}: {value}")

