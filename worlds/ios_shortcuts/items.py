from BaseClasses import Item, ItemClassification

ITEM_NAME_TO_ID = {
    "Shortcut Activation": 1,
    "Filler": 2
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Shortcut Activation": ItemClassification.progression,
    "Filler": ItemClassification.filler,
}

class IosShortcutsItem(Item):
    game = "iOS Shortcuts"

def get_random_filler_item_name(world: IosShortcutsWorld) -> str:
    return "Filler"

def create_item_with_correct_classification(world: IosShortcutsWorld, name: str) -> IosShortcutsItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

def create_all_items(world: IosShortcutsWorld) -> None:
    itempool: list[Item] = [
        world.create_item("Shortcut Activation")
    ]

    number_of_items = len(itempool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool