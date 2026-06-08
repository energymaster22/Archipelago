from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

def create_and_connect_regions(world: VacationSimulatorWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: VacationSimulatorWorld) -> None:
    hotel = Region("Hotel", world.player, world.multiworld)
    vacation_beach = Region("Vacation Beach", world.player, world.multiworld)
    vacation_forest = Region("Vacation Forest", world.player, world.multiworld)
    vacation_mountain = Region("Vacation Mountain", world.player, world.multiworld)

    dive_site = Region("Dive Site", world.player, world.multiworld)
    hiking_trail = Region("Hiking Trail", world.player, world.multiworld)
    overlook = Region("Overlook", world.player, world.multiworld)

    regions = [hotel, vacation_beach, vacation_forest, vacation_mountain, dive_site, hiking_trail, overlook]

    world.multiworld.regions += regions

def connect_regions(world: VacationSimulatorWorld) -> None:
    hotel = world.get_region("Hotel")
    vacation_beach = world.get_region("Vacation Beach")
    vacation_forest = world.get_region("Vacation Forest")
    vacation_mountain = world.get_region("Vacation Mountain")

    dive_site = world.get_region("Dive Site")
    hiking_trail = world.get_region("Hiking Trail")
    overlook = world.get_region("Overlook")

    hotel.connect(vacation_beach, "Vacation Beach Gate")
    hotel.connect(vacation_forest, "Vacation Forest Gate")
    hotel.connect(vacation_mountain, "Vacation Mountain Gate")
    
    vacation_beach.connect(dive_site, "Submarine")
    vacation_forest.connect(hiking_trail, "Trail Gate")
    vacation_mountain.connect(overlook, "Ski Lift")
    
