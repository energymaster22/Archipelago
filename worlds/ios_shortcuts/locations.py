from BaseClasses import ItemClassification, Location

from . import items

LOCATION_NAME_TO_ID = {
    "Locked Shortcut": 1,
    "Free Shortcut": 2,
}

class IosShortcutsLocation(Location):
    game = "iOS Shortcuts"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: IosShortcutsWorld) -> None:
    create_regular_locations(world)
    #create_events(world)

def create_regular_locations(world:IosShortcutsWorld) -> None:
    home_screen = world.get_region("Home Screen")
    shortcuts_app = world.get_region("Shortcuts App")

    shortcuts_app_locations = get_location_names_with_ids(
        ["Locked Shortcut", "Free Shortcut"]
    )
    shortcuts_app.add_locations(shortcuts_app_locations, IosShortcutsLocation)