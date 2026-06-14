from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World

from .import items, locations, regions, rules, web_world
from .import options as vacationsimulator_options

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
        settings = {
            "beachGate": int(self.options.beach_memory_count),
            "forestGate": int(self.options.forest_memory_count),
            "mountainGate": int(self.options.mountain_memory_count),
            "finalGate": int(self.options.final_memory_count),
        }
    
        slot_data = {
            "settings": settings,
        }
    
        return slot_data