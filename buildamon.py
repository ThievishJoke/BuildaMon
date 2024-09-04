
import random

mon_strength = ["Regular", "Convergent", "Starter", "God Pokemon", "Fossil", "Pseudo", "Mythical", "Legendary"]
evo_count = [0,1,2,3]
type_count = (0,1,2)
mon_types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison",
    "Ground", "Flying", "Phychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]
starter_main_types = ["Fire", "Water", "Grass", "Electric"]
mon_gimmick = ["None", "Mega Evolution", "Additional Form", "Signiture Move", "Signiture Ability", "Fusion", "Gigantamax", "New Mechanic", "Corrupted", "Shinning"]
gimmick_method = ["Held Item", "Seasonal", "Key Item", "Move", "Location", "Time", "Weather", "Ability"]
aquire_method = ["Route Encounter", "Seasonal", "Ruins", "Hidden Grotto", "Tree", "Cave", "Beach", "Fishing", "Swimming", "Deep Water Swimming",
                "Random World Encounter", "NPC Trade", "Special"]
special_aquire_method = ["Story", "Scripted Event", "Post Story Ecounter", "Side Quest Encoutner", "Limited Time Event", "Gift"]
mon_has_cosmetic_forms = False

debug = False

def rand_mon_strength():
    global strength
    strength = random.choices(mon_strength, weights=(75,3,15,.5,10,5,1.5,3))
    if debug == True:
        print(f"\n{strength}")
    return strength

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
    global gimmick_use_method
    global mon_has_cosmetic_forms
    special = (0, 10, 45, 25, 15, 5, 0, 5, 5, 5)
    if "God Pokemon" in strength:
        w = special
    elif "Mythical" in strength:
        w = special
    elif "Legendary" in strength:
        w = special
    else:
        w = (50, 20, 20, 15, 10, 5, 15, 5, 5, 5)
    mons_gimmick = random.choices(mon_gimmick, weights=(w))
    gimmick = (random.choice(mons_gimmick))
    if "None" in gimmick:
        pass
    elif "Mega Evolution" in gimmick:
        gimmick_use_method = gimmick_method[0]
    elif "Fusion" in gimmick:
        gimmick_use_method = gimmick_method[2]
    elif "Gigantamax" in gimmick:
        gimmick_use_method = gimmick_method[2]
    elif "Signiture Move" in gimmick:
        gimmick_use_method = gimmick_method[3]
    elif "Ability" in gimmick:
        while "Ability" in gimmick_use_method:
            gimmick = random.choices(gimmick_method)
            print(gimmick)
    else:
        gimmick_use_method = random.choices(gimmick_method)

    form_option = [True, False]
    mon_has_cosmetic_forms = random.choices(form_option, weights=(5,95), k=1)[0]

    if debug == True:
        print("Gimmick: ", gimmick)

def rand_aquire_method():
    global method_to_aquire
    method_to_aquire = random.choices(aquire_method)
    if "Starter" in strength:
        method_to_aquire = special_aquire_method[5]
    if "Special" in method_to_aquire:
        method_to_aquire = random.choices(special_aquire_method)
    return method_to_aquire

def rand_stat_distribution():
    global distribution_lean
    stat_distibution_leans = ["HP", "Atk", "Def", "Sp. Atk", "Sp.Def", "Speed"]
    distribution_lean = random.choice(stat_distibution_leans)

def gen_mon():
    rand_mon_strength()
    rand_evo_count()
    rand_type()
    rand_mon_gimmick()
    rand_aquire_method()
    rand_stat_distribution()

    pokemon = {
        "Category ": strength,
        "Evolution": evolution_stage,
        "Evolution Type": evolution_stage_type,
        "Type 1": monster_type[0],
    }

    if len(monster_type) > 1:
        pokemon["Type 2"] = monster_type[1]

    pokemon["Gimmick"] = gimmick
    if "None" in gimmick:
        pass
    else:
        pokemon["Gimmick Use Method"] = gimmick_use_method
    pokemon["Aquire Method"] = method_to_aquire

    if mon_has_cosmetic_forms == True:
        pokemon["Has Cosmetic Forms"] = mon_has_cosmetic_forms
    
    pokemon["Stat Distribution Lean"] = distribution_lean

    return pokemon

for x in range(5):
    random_pokemon = gen_mon()
    print()
    print("Randomly Generated Pokémon:")
    for key, value in random_pokemon.items():
        print(f"{key}: {value}")

