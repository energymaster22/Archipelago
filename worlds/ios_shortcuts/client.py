import asyncio

import CommonClient
import Utils

from flask import Flask

from typing import Any, Dict, List, Optional, Set, Tuple

class IosShortcutsClientCommandProcessor(CommonClient.ClientCommandProcessor):
    pass

class IosShortcutsClientContext(CommonClient.CommonContext):
    game: "iOS Shortcuts"

    tags: Set[str] = {"AP"}
    command_processor: CommonClient.ClientCommandProcessor = IosShortcutsClientCommandProcessor
    items_handling: int = 0b111
    want_slot_data: bool = True

    def __init__(self, server_adress: Optional[str], password: Optional[str]) -> None:
        super().__init__(server_adress, password)

        self.game = "iOS Shortcuts"

    def make_gui(self):
        from kvui import GameManager

        class TextManager(GameManager):
            base_title: str = "iOS Shortcuts Client"

        return TextManager

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)

        await self.get_username()
        await self.send_connect()

    async def disconnect(self, allow_autoreconnect: bool = False):
        self.game = "iOS Shortcuts"

        self.state_game = "iOS Shortcuts"

        await super().disconnect(allow_autoreconnect)

def main(*args) -> None:
    Utils.init_logging("iOSShortcutsClient", exception_logger="Client")

    parser = CommonClient.get_base_parser(description="iOS Shortcuts Client")

    parser.add_argument("url", nargs="?", help="Archipelago Connection URL")
    parser.add_argument('--name', default=None, help="Archipelago Slot Name")

    args = parser.parse_args(args)

    if args.url:
        url = urllib.parse.urlparse(args.url)
        args.connect = url.netloc
        if url.username:
            args.name = urllib.parse.unquote(url.username)
        if url.password:
            args.password = urllib.parse.unquote(url.password)

    async def _main(_args):
        ctx: IosShortcutsClientContext = IosShortcutsClientContext(args.connect, args.password)

        ctx.server_task = asyncio.create_task(CommonClient.server_loop(ctx), name="ServerLoop")

        if CommonClient.gui_enabled:
            ctx.run_gui()

        ctx.run_cli()

        await ctx.exit_event.wait()
        await ctx.shutdown()

    import colorama

    colorama.just_fix_windows_console()

    asyncio.run(_main(args))

    colorama.deinit()


if __name__ == "__main__":
    main(*sys.argv[1:])
