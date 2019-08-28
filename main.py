import npyscreen

from tui.forms import main_menu


class App(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', main_menu.MainMenuForm, name='Main menu')
        self.addForm('NewGame', main_menu.NewGameForm, name='New game')
        self.addForm('LoadGame', main_menu.LoadGameForm, name='Load game')
        self.addForm('SaveGame', main_menu.SaveGameForm, name='Save game')


if __name__ == '__main__':
    app = App().run()
    print('exited')
