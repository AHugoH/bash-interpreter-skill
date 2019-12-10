from mycroft import MycroftSkill, intent_file_handler


class BashInterpreter(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('interpreter.bash.intent')
    def handle_interpreter_bash(self, message):
        self.speak_dialog('interpreter.bash')


def create_skill():
    return BashInterpreter()

