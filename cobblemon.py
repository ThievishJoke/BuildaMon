#from buildamon import mon_types,evolution_methods
import random

mon_types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting",
             "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost",
             "Dragon", "Dark", "Steel", "Fairy"]

# Config
debug = False

type_count = (1,2)
dex_num = 6500

def rand_type():
    global monster_type
    a = random.choices(type_count, weights=(50, 50))
    z = (random.choice(a))
    if debug:
        print("Type Count: ", z)
    type_1 = random.choice(mon_types)
    type_2 = random.choice(mon_types)
    while type_2 == type_1:
        type_2 = random.choice(mon_types)
    if z == 2:
        monster_type = (type_1, type_2)
    else:
        monster_type = (type_1,)

def name_mon():
    global name, pokedex_name
    name = str(input("Insert a name for the mon: "))
    pokedex_name = name.lower()

def gender():
    global gender_ratio
    gender_ratio = float(input("Insert the gender ratio: "))

def dex_size():
    global height, weight
    height = int(input("Insert the height: "))
    weight = int(input("Insert the weight: "))

def mon_info():
    global labels, aspects, abilities, egg_groups
    labels = list(input("Insert labels: "))
    aspects = list(input("Optionaly add aspects: ")),
    abilities = list(input("Add an ability: ")),
    egg_groups = list(input("If breedable add egg groups: ")),

def mon_stats():
    global healthpoints, attack, defence, special_attack, special_defense, speed
    global healthpoint_yield, attack_yield, defence_yield, special_attack_yield, special_defense_yield, speed_yield
    global xp_yield, xp_group, catch_rate, egg_cycles, basefriendship
    global size_scale, hb_width, hb_height, fix_hb, can_fly
    #implement manual input and "presets"
    #Base Stats
    healthpoints = int(input("set the hp: "))
    attack = int(input("set the attack: "))
    defence = int(input("set the defence: "))
    special_attack = int(input("set the special attack: "))
    special_defense = int(input("set the special defense: "))
    speed = int(input("set the speed: "))

    #Ev Yield
    healthpoint_yield = int(input("set the hp yield: "))
    attack_yield = int(input("set the attack yield: "))
    defence_yield = int(input("set the defence yield: "))
    special_attack_yield = int(input("set the special attack yield: "))
    special_defense_yield = int(input("set the special defense yield: "))
    speed_yield = int(input("set the speed yield: "))

    #Other 
    xp_yield  = int(input("set the xp yield: "))
    xp_group = str(input("set the xp group: "))
    catch_rate = int(input("set the catch rate: "))
    egg_cycles = int(input("set the egg cycles: "))
    basefriendship = int(input("set the base friendship: "))
    size_scale = float(input("set the size scale: "))
    hb_width = float(input("set the hit box width: "))
    hb_height = float(input("set the hit box height: "))
    fix_hb = bool(input("set if the size is fixed: "))
    can_fly = bool(input("set if the mon can fly: "))

def build_mon():
    rand_type()
    print(monster_type[0], monster_type[1])
    name_mon()
    gender()
    dex_size()
    mon_info()
    mon_stats()

build_mon()

pokemon = {
    "implemented ": True,
    "nationalPokedexNumber": dex_num,
    "name": name,
    "primaryType": monster_type[0],
    "secondaryType": monster_type[1],
    "maleRatio": gender_ratio,
    "height": height,
    "weight": weight,
    "pokedex": ["cobblemon.species.{pokedex_name}.desc"
    ],
    "labels": [
        labels
    ],
    "aspects": [aspects],
    "abilities": [
        abilities
    ],
    "eggGroups": [
        egg_groups
    ],
    "baseStats": {
        "hp": healthpoints,
        "attack": attack,
        "defence": defence,
        "special_attack": special_attack,
        "special_defense": special_defense,
        "speed": speed
    },
    "evYield": {
        "hp": healthpoint_yield,
        "attack": attack_yield,
        "defence": defence_yield,
        "special_attack": special_attack_yield,
        "special_defense": special_defense_yield,
        "speed": speed_yield
    },
    "baseExperienceYield": xp_yield,
    "experienceGroup": xp_group,
    "catchRate": catch_rate,
    "eggCycles": egg_cycles,
    "baseFriendship": basefriendship,
    "baseScale": size_scale,
    "hitbox": {
        "width": hb_width,
        "height": hb_height,
        "fixed": fix_hb
    },
    "behavior":  {
        "moving": {
            "fly": {
                "canFly": can_fly
            }
        }
    }#,
    #"drops": {
    #    "ammount": drops_amount,
    #    "entries": [
    #        {
    #            "item": item_id,
    #            "quantityRange": quantity_range,
    #            "percentage": drop_percentage
    #        }
    #    ]
    #},
    #"moves": [
    #    "{level:move_name}",
    #    "{egg.move_name}",
    #    "{tm.move_name}",
    #    "{tutor:move_name}"
    #],
    #"evolutions": [
    #    {
    #        "id": evolution_id,
    #        "variant": evolution_method,
    #        "result": evolution_name,
    #        "consumeHeldItem": bool,
    #        "learnableMoves": [
    #            "{move_name}"
    #        ],
    #        "requirements": [
    #            {
    #                "variant": evolution_variant,
    #                "": addtional_requirements
    #            }
    #        ]
    #    }
    #]
}

print(pokemon)