from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups, option_presets

class VacationSimulatorWebWorld(WebWorld):
    game = "Vacation Simulator"

    theme = "partyTime"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide for setting up Vacation Simulator for Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["Energymaster22", "chandler05"],
    )

    tutorials = [setup_en]

    option_groups = option_groups
    option_presets = option_presets