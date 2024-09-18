import customtkinter
from CTkListbox import *

customtkinter.set_appearance_mode("system")
custom_theme = open("pink.json", "r")
customtkinter.set_default_color_theme("pink.json")

import random

# Methods and Variables

mon_strength = ["Regular", "Convergent", "Starter", "God Pokemon",
                "Fossil", "Pseudo", "Mythical", "Legendary", "Ultra Beast"]
evo_count = [0, 1, 2, 3] #Not Implemented
type_count = (0, 1, 2) #Not Implemented
mon_types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting",
             "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost",
             "Dragon", "Dark", "Steel", "Fairy"]
starter_main_types = ["Fire", "Water", "Grass", "Electric"]
mon_gimmick = ["None", "Mega Evolution", "Z-Move", "Additional Form",
               "Signature Move", "Signiture Ability", "Fusion", "Gigantamax",
               "New Mechanic", "Corrupted", "Shinning", "Shadow"]
gimmick_method = ["Held Item", "Seasonal", "Key Item",
                  "Move", "Location", "Time", "Weather", "Ability"]
aquire_method = ["Route Encounter", "Seasonal Route Encounter", "Ruins", # Special aquire method and aquire method is not implemented
                 "Hidden Grotto", "Tree", "Cave", "Beach", "Fishing",
                 "Swimming", "Deep Water Swimming", "Random World Encounter",
                 "NPC Trade", "Special", "Urban", "Industrial"]
special_aquire_method = ["Story", "Scripted Event", "Post Story Encounter",
                         "Side Quest Encounter", "Limited Time Event", "Gift"]
dragon_shapes = ["Cockatrice", "Wyvern", "Amphithere", "Fae", "Dragon", #Dragon Shapes is not implemented
                 "Wyrm", "Sea Serpent", "Quetzalcoatl", "Lindwurm",
                 "Salamander", "Lung Dragon", "Drake", "Hydra", "Kirin"]
region_orgin_mainline = ["Kanto", "Sevii Islands", "Johto", "Hoenn", "Sinnoh", #Region of origin is not implemented
                          "Battle Zone", "Hisui", "Unova", "Kalos", "Alola",
                          "Galar", "Paldea", "Kitakami"]
region_orgin_side_series = ["Orre", "Fiore", "Almia", "Oblivia", "Ransei", 
                            "Ransei Kingdoms", "Pasio", "Lental"]
region_orgin_anime_exclusive = ["Orange Islands"]
evolution_methods = ["Level Up", "Friendship", "Trade", "Evolution Stone", "Item", "Location", "Time", "Move"] #Not Implemented

# Mapping gimmicks to specific gimmick methods
gimmick_method_mapping = {
    "Mega Evolution": "Held Item",  # Always held item (Mega Stone, Origin Orb)
    "Fusion": "Key Item",  # Always some sort of key item
    "Gigantamax": "Key Item",  # Always key item
    "Z-Move": "Held Item",  # Always key item (Z crystal)
    "Signature Move": "Move",  # Always the move
    "Signature Ability": "Ability",  # Always the ability
}

class CustomCTkListbox(CTkListbox):
    def clear_selection(self):
        self.selection_clear(0, self.size() - 1)

    def set_selection(self, value):
        # Simulate selection by updating the display or internal state
        for index in range(self.size()):
            if self.get(index) == value:
                # Highlight or otherwise indicate the item
                self.selection_set(index)
                break

class CustomCTkListbox(CTkListbox):
    def clear_selection(self):
        # Use internal state or flags to simulate clearing
        pass

    def set_selection(self, value):
        # Use internal state or flags to simulate setting selection
        pass

# Function to center the window
def center_window(window, width=500, height=550):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    position_top = int(screen_height / 2 - height / 2)
    position_right = int(screen_width / 2 - width / 2)
    window.geometry(f'{width}x{height}+{position_right}+{position_top}')

# Function to generate random Pokémon with adjusted values
def generate_random_pokemon():
    selected_strengths = [mon_strength_listbox.get(i) for i in mon_strength_listbox.curselection()]
    selected_types_1 = [type_1_listbox.get(i) for i in type_1_listbox.curselection()]
    selected_types_2 = [type_2_listbox.get(i) for i in type_2_listbox.curselection()]

    selected_gimmicks = [gimmick for gimmick, var in gimmick_vars.items() if var.get()]

    if selected_strengths:
        strength = random.choice(selected_strengths)
    else:
        strength = random.choice(mon_strength)  # Default to random if none selected

    if selected_types_1:
        type_1 = random.choice(selected_types_1)
    else:
        type_1 = random.choice(mon_types)

    if selected_types_2:
        type_2 = random.choice(selected_types_2)
    else:
        type_2 = random.choice(mon_types)

    gimmick = random.choice(selected_gimmicks) if selected_gimmicks else "None"

    # Check if the gimmick has a specific method, else choose randomly
    if gimmick in gimmick_method_mapping:
        acquire_method = gimmick_method_mapping[gimmick]
        
        # Update internal state or visual feedback
        method_listbox.selection_clear()  # Clear selection state
        method_listbox.update()  # Force UI update if necessary
        # Simulate selection visually if required
        output_text.set(f"Selected Method: {acquire_method}")

        # Disable interaction
        method_listbox.bind("<Button-1>", lambda e: "break")
        method_listbox.bind("<Key>", lambda e: "break")
    else:
        # Enable interaction
        method_listbox.unbind("<Button-1>")
        method_listbox.unbind("<Key>")

        selected_methods = [method_listbox.get(i) for i in method_listbox.curselection()]
        acquire_method = random.choice(selected_methods) if selected_methods else random.choice(gimmick_method)

    # Display generated Pokémon
    output_text.set(f"Generated Pokémon:\nStrength: {strength}\n"
                    f"Type 1: {type_1}\nType 2: {type_2}\n"
                    f"Gimmick: {gimmick}\nGimmick Method: {acquire_method}")

def enforce_gimmick_rules():
    selected_gimmicks = [gimmick for gimmick, var in gimmick_vars.items() if var.get()]

    if selected_gimmicks:
        for gimmick in selected_gimmicks:
            if gimmick in gimmick_method_mapping:
                acquire_method = gimmick_method_mapping[gimmick]

                # Update internal state or visual feedback
                method_listbox.selection_clear()  # Clear selection state
                method_listbox.update()  # Force UI update if necessary
                # Simulate selection visually if required
                output_text.set(f"Simulated Selection: {acquire_method}")
                
                # Disable interaction
                method_listbox.bind("<Button-1>", lambda e: "break")
                method_listbox.bind("<Key>", lambda e: "break")
                return

    # Enable interaction
    method_listbox.unbind("<Button-1>")
    method_listbox.unbind("<Key>")

# Main window
root = customtkinter.CTk()
root.title("Pokémon Randomizer")

# Center the window
center_window(root, 600, 550)

# Multi-selection Listbox for Mon Strength
customtkinter.CTkLabel(root, text="Select Mon Strength(s):").grid(row=0, column=0, padx=5, pady=5)
mon_strength_listbox = CTkListbox(root, multiple_selection=True, height=20)
mon_strength_listbox.grid(row=0, column=1)
for strength in mon_strength:
    mon_strength_listbox.insert(customtkinter.END, strength)

# Multi-selection Listbox for Type 1
customtkinter.CTkLabel(root, text="Select Type 1(s):").grid(row=1, column=0, padx=5, pady=5)
type_1_listbox = CTkListbox(root, multiple_selection=True, height=20)
type_1_listbox.grid(row=1, column=1)
for type_ in mon_types:
    type_1_listbox.insert(customtkinter.END, type_)

# Multi-selection Listbox for Type 2
customtkinter.CTkLabel(root, text="Select Type 2(s):").grid(row=2, column=0, padx=5, pady=5)
type_2_listbox = CTkListbox(root, multiple_selection=True, height=20)
type_2_listbox.grid(row=2, column=1)
for type_ in mon_types:
    type_2_listbox.insert(customtkinter.END, type_)

# Gimmick Checkboxes
customtkinter.CTkLabel(root, text="Select Gimmicks:").grid(row=4, column=0, padx=5, pady=5)
gimmick_vars = {}
for i, gimmick in enumerate(mon_gimmick):
    var = customtkinter.BooleanVar(value=False)
    gimmick_vars[gimmick] = var
    cb = customtkinter.CTkCheckBox(root, text=gimmick, variable=var, command=enforce_gimmick_rules)  # Use CTkCheckBox
    cb.grid(row=3+i//2, column=1+(i % 2), padx=5, pady=5)

# Multi-selection Listbox for Gimmick Method
customtkinter.CTkLabel(root, text="Select Gimmick Method(s):").grid(row=9, column=0, padx=5, pady=5)
method_listbox = CustomCTkListbox(root, multiple_selection=True, height=20)
method_listbox.grid(row=9, column=1)
for method in gimmick_method:
    method_listbox.insert(customtkinter.END, method)

# Button to generate Pokémon
generate_button = customtkinter.CTkButton(root, text="Generate Pokémon", command=generate_random_pokemon)
generate_button.grid(row=10, column=0, columnspan=2, pady=10)

# Label to display the output
output_text = customtkinter.StringVar()
output_label = customtkinter.CTkLabel(root, textvariable=output_text, anchor="w", justify="left")
output_label.grid(row=11, column=0, columnspan=2, padx=5, pady=5)

# Run the GUI
root.mainloop()