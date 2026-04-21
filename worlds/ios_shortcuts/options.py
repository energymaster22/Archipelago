from dataclasses import dataclass

from Options import Choice

class IPhone(Toggle):
    """
    Do you actually have an Iphone?
    """

    display_name = "Iphone?"

@dataclass
class IosShortcutsOptions(PerGameCommonOptions):
    iphone: IPhone

option_groups = [
    OptionGroup(
        "Important Options",
        [IPhone]
    )
]