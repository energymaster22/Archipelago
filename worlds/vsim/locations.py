from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items


LOCATION_NAME_TO_ID = {
    "Vacation Beach - Block The Sun": 94202001,
    "Vacation Beach - R e l a x": 94202002,
    "Vacation Beach - Good At Sports I": 94202003,
    "Vacation Beach - Good At Sports II": 94202004,
    "Vacation Beach - Beach Bugs": 94202005,
    "Vacation Beach - Sandcastles I": 94202006,
    "Vacation Beach - Sandcastles II": 94202007,
    "Vacation Beach - Sandcastles III": 94202008,
    "Vacation Beach - Sandcastles IV": 94202009,
    "Vacation Beach - Sandcastles V": 94202010,
    "Vacation Beach - Sweet Selfie": 94202011,
    "Dive Site - Sea Shanty": 94202012,
    "Dive Site - Open BotBeard's Treasure": 94202013,
    "Dive Site - Sea Life Snaps I": 94202014,
    "Dive Site - Sea Life Snaps II": 94202015,
    "Vacation Beach - Beach Orders I": 94202016,
    "Vacation Beach - Beach Orders II": 94202017,
    "Vacation Beach - Beach Orders III": 94202018,
    "Vacation Beach - Beach Orders IV": 94202019,
    "Vacation Beach - Beach Photos I": 94202020,
    "Vacation Beach - Beach Photos II": 94202021,
    "Vacation Beach - Beach Photos III": 94202022,
    "Vacation Beach - Beach Photos IV": 94202023,
    "Vacation Forest - Fish Finder I": 94202024,
    "Vacation Forest - Fish Finder II": 94202025,
    "Vacation Forest - Fish Finder III": 94202026,
    "Vacation Forest - Painting I": 94202027,
    "Vacation Forest - Painting II": 94202028,
    "Vacation Forest - Forest Bugs": 94202029,
    "Vacation Forest - Forest Targets": 94202030,
    "Vacation Forest - Beach Targets": 94202031,
    "Vacation Forest - Mountain Targets": 94202032,
    "Vacation Forest - Spooky Story": 94202033,
    "Vacation Forest - Garden Variety": 94202034,
    "Vacation Forest - Forest Orders I": 94202035,
    "Vacation Forest - Forest Orders II": 94202036,
    "Vacation Forest - Forest Orders III": 94202037,
    "Vacation Forest - Forest Orders IV": 94202038,
    "Hiking Trail - Skipping ROCKS": 94202039,
    "Hiking Trail - Bird Observer": 94202040,
    "Hiking Trail - Hike Selfie": 94202041,
    "Hiking Trail - Turn On Geyser": 94202042,
    "Vacation Forest - Raft Master": 94202043,
    "Vacation Forest - Forest Photos I": 94202044,
    "Vacation Forest - Forest Photos II": 94202045,
    "Vacation Forest - Forest Photos III": 94202046,
    "Vacation Forest - Forest Photos IV": 94202047,
    "Vacation Mountain - Warm Winter": 94202048,
    "Vacation Mountain - Knitted Gift": 94202049,
    "Vacation Mountain - Good Listener": 94202050,
    "Vacation Mountain - Mountain Orders I": 94202051,
    "Vacation Mountain - Mountain Orders II": 94202052,
    "Vacation Mountain - Mountain Orders III": 94202053,
    "Vacation Mountain - Mountain Orders IV": 94202054,
    "Vacation Mountain - Puzzle Master": 94202055,
    "Vacation Mountain - Ice Sculptures I": 94202056,
    "Vacation Mountain - Ice Sculptures II": 94202057,
    "Vacation Mountain - Ice Sculptures III": 94202058,
    "Vacation Mountain - Ice Sculptures IV": 94202059,
    "Vacation Mountain - Ice Sculptures V": 94202060,
    "Vacation Mountain - Snow Safety Lesson": 94202061,
    "Vacation Mountain - Mountain Bugs": 94202062,
    "Vacation Mountain - Photobombinable": 94202063,
    "Overlook - On Hill Skiing I": 94202064,
    "Overlook - On Hill Skiing II": 94202065,
    "Overlook - Mountain Climbing I": 94202066,
    "Overlook - Mountain Climbing II": 94202067,
    "Overlook - Raise Flag At Summit": 94202068,
    "Vacation Mountain - Mountain Photos I": 94202069,
    "Vacation Mountain - Mountain Photos II": 94202070,
    "Vacation Mountain - Mountain Photos III": 94202071,
    "Vacation Mountain - Mountain Photos IV": 94202072,
}

class VacationSimulatorLocation(Location):
    game = "Vacation Simulator"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: VacationSimulatorWorld) -> None:
    create_regular_locations(world)
    
def create_regular_locations(world: VacationSimulatorWorld) -> None:
    hotel = world.get_region("Hotel")
    vacation_beach = world.get_region("Vacation Beach")
    vacation_forest = world.get_region("Vacation Forest")
    vacation_mountain = world.get_region("Vacation Mountain")

    dive_site = world.get_region("Dive Site")
    hiking_trail = world.get_region("Hiking Trail")
    overlook = world.get_region("Overlook")

    vacation_beach_locations = get_location_names_with_ids([
        "Vacation Beach - Block The Sun",
        "Vacation Beach - R e l a x",
        "Vacation Beach - Good At Sports I",
        "Vacation Beach - Good At Sports II",
        "Vacation Beach - Beach Bugs",
        "Vacation Beach - Sandcastles I",
        "Vacation Beach - Sandcastles II",
        "Vacation Beach - Sandcastles III",
        "Vacation Beach - Sandcastles IV",
        "Vacation Beach - Sandcastles V",
        "Vacation Beach - Sweet Selfie",
        "Vacation Beach - Beach Orders I",
        "Vacation Beach - Beach Orders II",
        "Vacation Beach - Beach Orders III",
        "Vacation Beach - Beach Orders IV",
        "Vacation Beach - Beach Photos I",
        "Vacation Beach - Beach Photos II",
        "Vacation Beach - Beach Photos III",
        "Vacation Beach - Beach Photos IV",
    ])
    vacation_beach.add_locations(vacation_beach_locations, VacationSimulatorLocation)

    vacation_forest_locations = get_location_names_with_ids({
        "Vacation Forest - Fish Finder I",
        "Vacation Forest - Fish Finder II",
        "Vacation Forest - Fish Finder III",
        "Vacation Forest - Painting I",
        "Vacation Forest - Painting II",
        "Vacation Forest - Forest Bugs",
        "Vacation Forest - Forest Targets",
        "Vacation Forest - Beach Targets",
        "Vacation Forest - Mountain Targets",
        "Vacation Forest - Spooky Story",
        "Vacation Forest - Garden Variety",
        "Vacation Forest - Forest Orders I",
        "Vacation Forest - Forest Orders II",
        "Vacation Forest - Forest Orders III",
        "Vacation Forest - Forest Orders IV",
        "Vacation Forest - Raft Master",
        "Vacation Forest - Forest Photos I",
        "Vacation Forest - Forest Photos II",
        "Vacation Forest - Forest Photos III",
        "Vacation Forest - Forest Photos IV",
    })
    vacation_forest.add_locations(vacation_forest_locations, VacationSimulatorLocation)

    vacation_mountain_locations = get_location_names_with_ids([
        "Vacation Mountain - Warm Winter",
        "Vacation Mountain - Knitted Gift",
        "Vacation Mountain - Good Listener",
        "Vacation Mountain - Mountain Orders I",
        "Vacation Mountain - Mountain Orders II",
        "Vacation Mountain - Mountain Orders III",
        "Vacation Mountain - Mountain Orders IV",
        "Vacation Mountain - Puzzle Master",
        "Vacation Mountain - Ice Sculptures I",
        "Vacation Mountain - Ice Sculptures II",
        "Vacation Mountain - Ice Sculptures III",
        "Vacation Mountain - Ice Sculptures IV",
        "Vacation Mountain - Ice Sculptures V",
        "Vacation Mountain - Snow Safety Lesson",
        "Vacation Mountain - Mountain Bugs",
        "Vacation Mountain - Photobombinable",
        "Vacation Mountain - Mountain Photos I",
        "Vacation Mountain - Mountain Photos II",
        "Vacation Mountain - Mountain Photos III",
        "Vacation Mountain - Mountain Photos IV",
    ])
    vacation_mountain.add_locations(vacation_mountain_locations, VacationSimulatorLocation)

    dive_site_locations = get_location_names_with_ids([
        "Dive Site - Sea Shanty",
        "Dive Site - Open BotBeard's Treasure",
        "Dive Site - Sea Life Snaps I",
        "Dive Site - Sea Life Snaps II",
    ])
    dive_site.add_locations(dive_site_locations, VacationSimulatorLocation)

    hiking_trail_locations = get_location_names_with_ids([
        "Hiking Trail - Skipping ROCKS",
        "Hiking Trail - Bird Observer",
        "Hiking Trail - Hike Selfie",
        "Hiking Trail - Turn On Geyser",
    ])
    hiking_trail.add_locations(hiking_trail_locations, VacationSimulatorLocation)

    overlook_locations = get_location_names_with_ids([
        "Overlook - On Hill Skiing I",
        "Overlook - On Hill Skiing II",
        "Overlook - Mountain Climbing I",
        "Overlook - Mountain Climbing II",
        "Overlook - Raise Flag At Summit",
    ])
    overlook.add_locations(overlook_locations, VacationSimulatorLocation)
