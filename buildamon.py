
import random

mon_strength = ["Regular", "Convergent", "Starter", "God Pokemon", "Fossil", "Pseudo", "Mythical", "Legendary", "Ultra Beast"]
evo_count = [0,1,2,3]
type_count = (0,1,2)
mon_types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison",
    "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]
starter_main_types = ["Fire", "Water", "Grass", "Electric"]
mon_gimmick = ["None", "Mega Evolution", "Z-Move", "Additional Form", "Signiture Move", "Signiture Ability", "Fusion", "Gigantamax", "New Mechanic", "Corrupted", "Shinning", "Shadow"]
gimmick_method = ["Held Item", "Seasonal", "Key Item", "Move", "Location", "Time", "Weather", "Ability"]
aquire_method = ["Route Encounter", "Seasonal", "Ruins", "Hidden Grotto", "Tree", "Cave", "Beach", "Fishing", "Swimming", "Deep Water Swimming",
                "Random World Encounter", "NPC Trade", "Special"]
dragon_shapes = ["Cockatrice", "Wyvern", "Amphithere", "Fae", "Dragon",
                "Wyrm", "Sea Serpent", "Quetzalcoatl", "Lindwurm", "Salamander", "Lung Dragon", "Drake", "Hydra", "Kirin"]
special_aquire_method = ["Story", "Scripted Event", "Post Story Ecounter", "Side Quest Encoutner", "Limited Time Event", "Gift"]
mon_has_cosmetic_forms = False

# Initializes a counter
mon_counter = 0

debug = False

# Mapping gimmicks to specific gimmick methods
gimmick_method_mapping = {
    "Mega Evolution": "Held Item", #Always held item (Mega Stone)
    "Fusion": "Key Item", #Always some sort of key item
    "Gigantamax": "Key Item", #Always key item
    "Z-Move": "Held Item", #Always key item (Z crystal)
    "Signature Move": "Move", #Always the move
    "Signature Ability": "Ability", #Always the ability
}

def rand_mon_strength(): #Picks random mon strength
    global strength
    strength = random.choices(mon_strength, weights=(75,3,15,.5,10,5,1.5,3,3))[0]
    if debug:
        print(f"\nStrength: {strength}")
    return strength

def rand_evo_count(): #Pick random number of evolutinon stages:
    #Basic -> Stage 1 -> Stage 2, Split (Stage 1a, Stage 1b, ect.) or Stage 1 (Stage 2a, Stage 2b, ect.)
    global evolution_stage, evolution_stage_type
    evolution_stage_type = ""
    if "Starter" in strength:
        evolution_stage = 2
        evolution_stage_type = "Two Stage"
    elif "Convergent" in strength:
        evolution_stage = random.choices(evo_count, weights=(0,25,50,0))[0]
        if evolution_stage == 1:
            evolution_stage_type = "One Stage"
        elif evolution_stage == 2:
            evolution_stage_type = "Two Stage"
    else:
        evolution_stage = random.choices(evo_count, weights=(50,25,50,10))[0]
        if debug == True:
            print("Stage Value", evolution_stage)
        if evolution_stage == 0:
            evolution_stage_type = "Basic"
        elif evolution_stage == 1:
            evolution_stage_type = "One Stage"
        elif evolution_stage == 2:
            evolution_stage_type = "Two Stage"
        elif evolution_stage == 3:
            evolution_stage_type = "Split"
            number_of_splits = random.randint(2,4)
            if number_of_splits == 4:
                number_of_splits = 3 + random.randint(1,13)
    if debug == True:
        print(evolution_stage_type)
    return evolution_stage, evolution_stage_type

def rand_type(): #Picks random type
    global monster_type, dragon_shape
    if "Starter" in strength: #Starters always include one of the following [Water, Fire, Grass, Electric]
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
    elif "Fossil" in strength: #Fossil always contains Rock type
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
    if (type_1 or type_2 == "Dragon"): #If dragon type pick type of dragon
        dragon_shape = random.choice(dragon_shapes)
    if debug:
        print(f"Type(s): ", monster_type[0], monster_type[1] if len(monster_type) > 1 else "",
            dragon_shape if "Dragon" in monster_type else "")
    return monster_type, dragon_shape


def rand_mon_gimmick(): #Pick random mon gimmick with exceptions
    global gimmick, gimmick_use_method, mon_has_cosmetic_forms
    
    gimmick_weights = [60, 20, 15, 20, 20, 10, 5, 20, 5, 5, 5, 5] if strength not in ["God Pokemon", "Mythical", "Legendary"] else [0, 10, 20, 45, 35, 20, 5, 0, 5, 5, 5, 5]
    
    mons_gimmick = random.choices(mon_gimmick, weights=(gimmick_weights))

    if "Ultra Beast" in strength: #Ultra Beast always have Beast Boost as their ability
        gimmick = "Beast Boost"
        gimmick_use_method = "Ability"
    else:
        gimmick = (random.choice(mons_gimmick))
        #print("Gimmick", gimmick)

    if gimmick in gimmick_method_mapping:
        gimmick_use_method = gimmick_method_mapping[gimmick]
        #print("Silly Gimmicks", gimmick_use_method)
    else:
        gimmick_use_method = random.choices(gimmick_method)[0]
        #print("3", gimmick_use_method)

    form_option = [True, False]
    mon_has_cosmetic_forms = random.choices(form_option, weights=(5,95), k=1)[0]
    
    if debug:
        print(f"Gimmick: {gimmick}, Cosmetic Forms: {mon_has_cosmetic_forms}") #Gimmick Use Method: {gimmick_use_method}

def rand_aquire_method(): #Pick random aquire method with exceptions
    global method_to_aquire
    method_to_aquire = random.choices(aquire_method)[0]
    if "Starter" in strength:
        method_to_aquire = special_aquire_method[5]
    if "Ultra Beast" in strength:
        method_to_aquire = "Ultra Wormhole"
    if "Special" in method_to_aquire:
        method_to_aquire = random.choices(special_aquire_method)
    return method_to_aquire

def rand_stat_distribution(): #Determine mons distribution lean and base stat total
    global distribution_lean, distribution_lean_2, base_stat_total
    stat_distibution_leans = ["HP", "Atk", "Def", "Sp. Atk", "Sp.Def", "Speed"]
    def rand_stat_lean():
        rand_distribution_lean = random.choice(stat_distibution_leans)
        return rand_distribution_lean
    distribution_lean = rand_stat_lean()
    if evolution_stage == 0:
        base_stat_total = random.randint(250, 575)
    if evolution_stage == 1:
        base_stat_total = random.randint(270, 675)
    if evolution_stage == 2:
        base_stat_total = random.randint(295, 650)
    if evolution_stage == 3:
        base_stat_total = random.randint(195, 550)
    if "Starter" in strength:
        base_stat_total = 528
    # if mon is legendary roll a second stat lean (can be identical to first)
    if "Legendary" in strength:
        distribution_lean_2 = rand_stat_lean()
        base_stat_total = random.randint(300, 800)

def rand_mon_color(): #Pick random listed color
    global mon_color
    mon_color = random.choice(["Red", "Red-Orange", "Orange", "Orange-Yellow", "Yellow", "Yellow-Green", "Green", "Cyan",
                        "Blue", "Indigo", "Violet", "Black", "Grey", "White"])

def gen_mon():
    global mon_counter
    rand_mon_strength()
    rand_evo_count()
    rand_type()
    rand_mon_gimmick()
    rand_aquire_method()
    rand_stat_distribution()
    rand_mon_color()

    pokemon = {
        "Category ": strength,
        "Evolutions": evolution_stage,
        "Evolution Type": evolution_stage_type,
        "Type 1": monster_type[0],
    }

    if len(monster_type) > 1:
        pokemon["Type 2"] = monster_type[1]
    
    if "Dragon" in monster_type:
        pokemon["Dragon Shape"] = dragon_shape

    pokemon["Gimmick"] = gimmick
    if "None" in gimmick:
        pass
    else:
        pokemon["Gimmick Use Method"] = gimmick_use_method

    pokemon["Aquire Method"] = method_to_aquire

    if mon_has_cosmetic_forms == True:
        pokemon["Has Cosmetic Forms"] = mon_has_cosmetic_forms
    
    if "Legendary" in strength:
        pokemon["Stat Distribution Lean"] = distribution_lean
        pokemon["Stat Distribution Lean 2"] = distribution_lean_2
        pokemon["Base Stat Total"] = base_stat_total
    else:
        pokemon["Stat Distribution Lean"] = distribution_lean
        pokemon["Base Stat Total"] = base_stat_total

    pokemon["Mon Color"] = mon_color
    mon_counter += 1
    
    return pokemon

rand_val = int(input("Insert the number of Mon you want to generate: "))
for x in range(rand_val):
    random_pokemon = gen_mon()
    print()
    # Increment the counter for the next Pokémon
    print("Randomly Generated Pokémon", mon_counter, ":")
    print("---------------------------")
    for key, value in random_pokemon.items():
        print(f"{key:23s}: {value}")

