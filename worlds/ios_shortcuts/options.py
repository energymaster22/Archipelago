from dataclasses import dataclass

from Options import OptionGroup, PerGameCommonOptions, Toggle

class IPhone(Toggle):
    """
    Do you actually have an iPhone?
    """

    display_name = "iPhone?"

@dataclass
class IosShortcutsOptions(PerGameCommonOptions):
    iphone: IPhone

option_groups = [
    OptionGroup(
        "Important Options",
        [IPhone]
    )
]