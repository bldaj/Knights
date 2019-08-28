import npyscreen


class MainMenuMultiLineAction(npyscreen.MultiLineAction):
    def actionHighlighted(self, act_on_this, key_press):
        if act_on_this == 'New game':
            self.parent.parentApp.switchForm('NewGame')
        elif act_on_this == 'Load game':
            self.parent.parentApp.switchForm('LoadGame')
        elif act_on_this == 'Save game':
            self.parent.parentApp.switchForm('SaveGame')
        elif act_on_this == 'Exit':
            self.parent.parentApp.switchForm(None)
