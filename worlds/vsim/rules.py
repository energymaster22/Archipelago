from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasFromList, Rule

def set_all_rules(world: VacationSimulatorWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: VacationSimulatorWorld) -> None:
    vacation_beach_gate = world.get_entrance("Vacation Beach Gate")
    vacation_forest_gate = world.get_entrance("Vacation Forest Gate")
    vacation_mountain_gate = world.get_entrance("Vacation Mountain Gate")

    submarine = world.get_entrance("Submarine")
    trail_gate = world.get_entrance("Trail Gate")
    ski_lift = world.get_entrance("Ski Lift")

    has_beach_unlock = Has("Vacation Beach Gate Unlock")
    has_forest_unlock = Has("Vacation Forest Gate Unlock")
    has_mountain_unlock = Has("Vacation Mountain Gate Unlock")

    world.set_rule(vacation_beach_gate, has_beach_unlock)
    world.set_rule(vacation_forest_gate, has_forest_unlock)
    world.set_rule(vacation_mountain_gate, has_mountain_unlock)

    has_beach_mem = Has("Memory (Vacation Beach)", count=world.options.beach_memory_count.value)
    has_forest_mem = Has("Memory (Vacation Forest)", count=world.options.forest_memory_count.value)
    has_mountain_mem = Has("Memory (Vacation Mountain)", count=world.options.mountain_memory_count.value)

    world.set_rule(submarine, has_beach_mem)
    world.set_rule(trail_gate, has_forest_mem)
    world.set_rule(ski_lift, has_mountain_mem)

def set_all_location_rules(world: VacationSimulatorWorld) -> None:
    has_beach_unlock = Has("Vacation Beach Gate Unlock")
    has_forest_unlock = Has("Vacation Forest Gate Unlock")
    has_mountain_unlock = Has("Vacation Mountain Gate Unlock")

    has_beach_mem = Has("Memory (Vacation Beach)", count=world.options.beach_memory_count.value)
    has_forest_mem = Has("Memory (Vacation Forest)", count=world.options.forest_memory_count.value)
    has_mountain_mem = Has("Memory (Vacation Mountain)", count=world.options.mountain_memory_count.value)

    has_camera = Has("Camera")

    
    world.set_rule((world.get_location("Vacation Beach - Good At Sports II")), has_forest_unlock)
    world.set_rule((world.get_location("Vacation Beach - Sweet Selfie")), has_camera)
    world.set_rule((world.get_location("Dive Site - Sea Life Snaps I")), has_camera)
    world.set_rule((world.get_location("Dive Site - Sea Life Snaps II")), has_camera)
    world.set_rule((world.get_location("Vacation Beach - Beach Orders III")), has_forest_unlock)
    world.set_rule((world.get_location("Vacation Beach - Beach Orders IV")), has_forest_mem & has_forest_unlock & has_beach_mem & has_mountain_unlock)
    world.set_rule((world.get_location("Vacation Beach - Beach Photos I")), has_camera)
    world.set_rule((world.get_location("Vacation Beach - Beach Photos II")), has_camera & has_beach_mem)
    world.set_rule((world.get_location("Vacation Beach - Beach Photos III")), has_camera & has_beach_mem & has_forest_unlock & has_mountain_unlock)
    world.set_rule((world.get_location("Vacation Beach - Beach Photos IV")), has_camera & has_forest_unlock & has_mountain_unlock)
    world.set_rule((world.get_location("Vacation Forest - Fish Finder III")), has_mountain_unlock & has_beach_mem)
    world.set_rule((world.get_location("Vacation Forest - Painting II")), has_beach_unlock & has_mountain_unlock)
    world.set_rule((world.get_location("Vacation Forest - Beach Targets")), has_beach_unlock)
    world.set_rule((world.get_location("Vacation Forest - Mountain Targets")), has_mountain_unlock & has_mountain_mem)
    world.set_rule((world.get_location("Vacation Forest - Forest Orders III")), has_forest_mem & has_beach_mem & has_mountain_unlock)
    world.set_rule((world.get_location("Vacation Forest - Forest Orders IV")), has_forest_mem & has_mountain_unlock & has_beach_unlock)
    world.set_rule((world.get_location("Hiking Trail - Bird Observer")), has_camera)
    world.set_rule((world.get_location("Hiking Trail - Hike Selfie")), has_camera)
    world.set_rule((world.get_location("Vacation Forest - Raft Master")), has_forest_mem)
    world.set_rule((world.get_location("Vacation Forest - Forest Photos I")), has_camera)
    world.set_rule((world.get_location("Vacation Forest - Forest Photos II")), has_camera & has_forest_mem)
    world.set_rule((world.get_location("Vacation Forest - Forest Photos III")), has_camera & has_forest_mem & has_beach_unlock & has_mountain_unlock)
    world.set_rule((world.get_location("Vacation Forest - Forest Photos IV")), has_camera & has_beach_unlock)
    world.set_rule((world.get_location("Vacation Mountain - Mountain Orders III")), has_mountain_mem & has_forest_unlock & has_beach_unlock)
    world.set_rule((world.get_location("Vacation Mountain - Mountain Orders IV")), has_camera & has_beach_unlock & has_forest_mem & has_mountain_mem & has_forest_unlock)
    world.set_rule((world.get_location("Vacation Mountain - Puzzle Master")), has_camera)
    world.set_rule((world.get_location("Vacation Mountain - Photobombinable")), has_camera & has_mountain_mem)
    world.set_rule((world.get_location("Vacation Mountain - Mountain Photos I")), has_camera)
    world.set_rule((world.get_location("Vacation Mountain - Mountain Photos II")), has_camera & has_mountain_mem)
    world.set_rule((world.get_location("Vacation Mountain - Mountain Photos III")), has_camera & has_mountain_mem & has_beach_unlock & has_forest_unlock)
    world.set_rule((world.get_location("Vacation Mountain - Mountain Photos IV")), has_camera & has_beach_mem & has_forest_unlock)

def set_completion_condition(world: VacationSimulatorWorld) -> None:
    has_total_mem = HasFromList(
        "Memory (Vacation Beach)",
        "Memory (Vacation Forest)",
        "Memory (Vacation Mountain)",
        count=world.options.final_memory_count.value
    )

    has_beach_mem = Has("Memory (Vacation Beach)", count=world.options.beach_memory_count.value)
    has_forest_mem = Has("Memory (Vacation Forest)", count=world.options.forest_memory_count.value)
    has_mountain_mem = Has("Memory (Vacation Mountain)", count=world.options.mountain_memory_count.value)

    completion = has_total_mem & has_beach_mem & has_forest_mem & has_mountain_mem

    world.set_completion_rule(completion)