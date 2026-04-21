from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import IosShortcutsWorld

def create_and_connect_regions(world: IosShortcutsWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: IosShortcutsWorld) -> None:
    home_screen = Region("Home Screen", world.player, world.multiworld)
    shortcuts_app = Region("Shortcuts App", world.player, world.multiworld)

def connect_regions(world: IosShortcutsWorld) -> None:
    home_screen = world.get_region("Home Screen")
    shortcuts_app = world.get_region("Shortcuts App")

    home_screen.connect(shortcuts_app, "Open Shortcuts App")