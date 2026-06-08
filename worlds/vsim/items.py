from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

ITEM_NAME_TO_ID = {
    "Memory (Vacation Beach)": 1,
    "Memory (Vacation Forest)": 2,
    "Memory (Vacation Mountain)": 3,
    "Vacation Beach Gate Unlock": 4,
    "Vacation Forest Gate Unlock": 5,
    "Vacation Mountain Gate Unlock": 6,
    "Camera": 7,
    "Positive Reinforcement": 8,
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Memory (Vacation Beach)": ItemClassification.progression,
    "Memory (Vacation Forest)": ItemClassification.progression,
    "Memory (Vacation Mountain)": ItemClassification.progression,
    "Vacation Beach Gate Unlock": ItemClassification.progression,
    "Vacation Forest Gate Unlock": ItemClassification.progression,
    "Vacation Mountain Gate Unlock": ItemClassification.progression,
    "Camera": ItemClassification.progression,
    "Positive Reinforcement": ItemClassification.filler,
}

class VacationSimulatorItem(Item):
    game = "Vacation Simulator"

def get_random_filler_item_name(world: VacationSimulatorWorld) -> str:
    return "Positive Reinforcement"

def create_item_with_correct_classification(world: VacationSimulatorWorld, name: str) -> VacationSimulatorItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    return VacationSimulatorItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: VacationSimulatorWorld) -> None:

    itempool = []

    for x in range(22):
        itempool.append(world.create_item("Memory (Vacation Beach)"))
    for x in range(23):
        itempool.append(world.create_item("Memory (Vacation Forest)"))
    for x in range(24):
        itempool.append(world.create_item("Memory (Vacation Mountain)"))
    
    if world.options.starting_gate == 0:
        world.push_precollected(world.create_item("Vacation Beach Gate Unlock"))
        itempool.append(world.create_item("Vacation Forest Gate Unlock"))
        itempool.append(world.create_item("Vacation Mountain Gate Unlock"))

    if world.options.starting_gate == 1:
        itempool.append(world.create_item("Vacation Beach Gate Unlock"))
        world.push_precollected(world.create_item("Vacation Forest Gate Unlock"))
        itempool.append(world.create_item("Vacation Mountain Gate Unlock"))
    
    if world.options.starting_gate == 2:
        itempool.append(world.create_item("Vacation Beach Gate Unlock"))
        itempool.append(world.create_item("Vacation Forest Gate Unlock"))
        world.push_precollected(world.create_item("Vacation Mountain Gate Unlock"))
    
    itempool.append(world.create_item("Camera"))

    number_of_items = len(itempool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool



