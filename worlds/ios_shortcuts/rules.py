from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

if TYPE_CHECKING:
    from .world import IosShortcutsWorld

def set_all_rules(world: IosShortcutsWorld) -> None:
    #set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

#def set_all_entrance_rules(world: IosShortcutsWorld) -> None:

def set_all_location_rules(world: IosShortcutsWorld) -> None:
    can_run_locked_shortcut: Rule = Has("Shortcut Activation")

    locked_shortcut = world.get_location("Locked Shortcut")
    world.set_rule(locked_shortcut, can_run_locked_shortcut)

def set_completion_condition(world: IosShortcutsWorld) -> None:
    world.set_completion_rule(Has("Shortcut Activation"))