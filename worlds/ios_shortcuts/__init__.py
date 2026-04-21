from .world import IosShortcutsWorld as IosShortcutsWorld

import worlds.LauncherComponents as LauncherComponents

def launch_client(*args) -> None:
    from .client import main
    LauncherComponents.launch(main, name="iOSShortcutsClient", args=args)

LauncherComponents.components.append(
    LauncherComponents.Component(
        "iOS Shortcuts Client",
        func=launch_client,
        component_type=LauncherComponents.Type.CLIENT,
    )
)