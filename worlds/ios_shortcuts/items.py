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