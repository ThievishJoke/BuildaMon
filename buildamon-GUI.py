import tkinter as tk
from tkinter import ttk
import random

# Original variables
mon_strength = ["Regular", "Convergent", "Starter", "God Pokemon", "Fossil", "Pseudo", "Mythical", "Legendary"]
mon_types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison",
             "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]
mon_gimmick = ["None", "Mega Evolution", "Additional Form", "Signature Move", "Signature Ability", "Fusion", 
               "Gigantamax", "New Mechanic", "Corrupted", "Shining"]
gimmick_method = ["Held Item", "Seasonal", "Key Item", "Move", "Location", "Time", "Weather", "Ability"]

# Mapping gimmicks to specific gimmick methods
gimmick_method_mapping = {
    "Mega Evolution": "Held Item",
    "Fusion": "Key Item",
    "Gigantamax": "Key Item",
    "Signature Move": "Move",
    "Signature Ability": "Ability",
}

# Function to center the window
def center_window(window, width=400, height=300):
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
        method_listbox.selection_clear(0, tk.END)  # Clear other selections
        method_listbox.selection_set(gimmick_method.index(acquire_method))  # Select the forced method
        method_listbox.config(state="disabled")  # Disable listbox for forced method
    else:
        method_listbox.config(state="normal")
        selected_methods = [method_listbox.get(i) for i in method_listbox.curselection()]
        acquire_method = random.choice(selected_methods) if selected_methods else random.choice(gimmick_method)
    
    # Display generated Pokémon
    output_text.set(f"Generated Pokémon:\nStrength: {strength}\n"
                    f"Type 1: {type_1}\nType 2: {type_2}\n"
                    f"Gimmick: {gimmick}\nGimmick Method: {acquire_method}")

# Function to enforce gimmick method rules
def enforce_gimmick_rules():
    selected_gimmicks = [gimmick for gimmick, var in gimmick_vars.items() if var.get()]
    for gimmick in selected_gimmicks:
        if gimmick in gimmick_method_mapping:
            method_listbox.selection_clear(0, tk.END)  # Clear other selections
            method_listbox.selection_set(gimmick_method.index(gimmick_method_mapping[gimmick]))  # Force select method
            method_listbox.config(state="disabled")  # Disable if method is forced
            return
    method_listbox.config(state="normal")  # Enable method selection otherwise

# Main window
root = tk.Tk()
root.title("Pokémon Randomizer")

# Center the window
center_window(root, 600, 500)

# Multi-selection Listbox for Mon Strength
ttk.Label(root, text="Select Mon Strength(s):").grid(row=0, column=0, padx=5, pady=5)
mon_strength_listbox = tk.Listbox(root, selectmode="multiple", height=5)
mon_strength_listbox.grid(row=0, column=1)
for strength in mon_strength:
    mon_strength_listbox.insert(tk.END, strength)

# Multi-selection Listbox for Type 1
ttk.Label(root, text="Select Type 1(s):").grid(row=1, column=0, padx=5, pady=5)
type_1_listbox = tk.Listbox(root, selectmode="multiple", height=5)
type_1_listbox.grid(row=1, column=1)
for type_ in mon_types:
    type_1_listbox.insert(tk.END, type_)

# Multi-selection Listbox for Type 2
ttk.Label(root, text="Select Type 2(s):").grid(row=2, column=0, padx=5, pady=5)
type_2_listbox = tk.Listbox(root, selectmode="multiple", height=5)
type_2_listbox.grid(row=2, column=1)
for type_ in mon_types:
    type_2_listbox.insert(tk.END, type_)

# Gimmick Checkboxes
ttk.Label(root, text="Select Gimmicks:").grid(row=3, column=0, padx=5, pady=5)
gimmick_vars = {}
for i, gimmick in enumerate(mon_gimmick):
    var = tk.BooleanVar(value=False)
    gimmick_vars[gimmick] = var
    cb = ttk.Checkbutton(root, text=gimmick, variable=var, command=enforce_gimmick_rules)
    cb.grid(row=3+i//2, column=1+(i % 2), padx=5, pady=5)

# Multi-selection Listbox for Gimmick Method
ttk.Label(root, text="Select Gimmick Method(s):").grid(row=7, column=0, padx=5, pady=5)
method_listbox = tk.Listbox(root, selectmode="multiple", height=5)
method_listbox.grid(row=7, column=1)
for method in gimmick_method:
    method_listbox.insert(tk.END, method)

# Button to generate Pokémon
generate_button = ttk.Button(root, text="Generate Pokémon", command=generate_random_pokemon)
generate_button.grid(row=8, column=0, columnspan=2, pady=10)

# Label to display the output
output_text = tk.StringVar()
output_label = ttk.Label(root, textvariable=output_text, anchor="w", justify="left")
output_label.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

# Run the GUI
root.mainloop()
