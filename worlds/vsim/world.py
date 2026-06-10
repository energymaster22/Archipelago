from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World

from .import items, locations, regions, rules, web_world
from .import options as vacationsimulator_options

from .helpers import location_name_to_game_id

class VacationSimulatorWorld(World):
    """
    """

    game = "Vacation Simulator"

    web = web_world.VacationSimulatorWebWorld()

    options_dataclass = vacationsimulator_options.VacationSimulatorOptions
    options: vacationsimulator_options.VacationSimulatorOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Hotel"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.VacationSimulatorItem:
        return items.create_item_with_correct_classification(self, name)

    def create_item_filler_version(self, name: str) -> items.VacationSimulatorItem:
        return items.create_item_with_filler_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        #TODO: Trim this down to only include the options.
        #This would require work on the mod side, but since
        #everything in this game is static, it really should
        #not need all of this in slot data.
        
        #Note: The code for fill_slot_data is mostly lifted
        #from the original world by chandler05, with minot modifications
        #to make it work in the new world, but I intend
        #on replacing it with my own code when the above is done.
        
        locations: Dict[int, Any] = {}

        multiworld = self.multiworld
        player = self.player
        options = self.options

        for loc in multiworld.get_filled_locations(player):
            if loc.item.code == None:
                continue
            else:
                data = {
                    "ap_id": loc.address,
                    "item_name": loc.item.name,
                    "player_name": multiworld.player_name[loc.item.player],
                    "type": int(loc.item.classification),
                    "in_game_id": str(location_name_to_game_id(str(loc.name))),
                }

                locations[location_name_to_game_id(str(loc.name))] = data

        settings = {
            "beachGate": int(options.beach_memory_count),
            "forestGate": int(options.forest_memory_count),
            "mountainGate": int(options.mountain_memory_count),
            "finalGate": int(options.final_memory_count),
        }
    
        slot_data = {
            "locations": locations,
            "settings": settings,
        }
    
        return slot_data