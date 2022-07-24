from commands.main import (
    NewGameCommand,
    LoadGameCommand,
    SaveGameCommand,
    ExitGameCommand,
)
from menus.common import (
    BaseMenu,
)


class MainMenu(BaseMenu):
    """
    """

    commands = [
        NewGameCommand,
        LoadGameCommand,
        SaveGameCommand,
        ExitGameCommand,
    ]
