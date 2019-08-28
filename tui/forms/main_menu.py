import npyscreen

from tui.widgets.main_menu import MainMenuMultiLineAction


class MainMenuForm(npyscreen.FormBaseNew):
    def create(self):
        self.option = self.add(MainMenuMultiLineAction, values=[
                'New game',
                'Load game',
                'Save game',
                'Exit'
            ])


class NewGameForm(npyscreen.FormBaseNew):
    def create(self):
        self.t = self.add(npyscreen.TitleText, value='Хуй')


class LoadGameForm(npyscreen.FormBaseNew):
    def create(self):
        self.t = self.add(npyscreen.TitleText, value='Пизда')


class SaveGameForm(npyscreen.FormBaseNew):
    def create(self):
        self.t = self.add(npyscreen.TitleText, value='Джигурда')
