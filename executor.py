from command.command import find_command, invalid_command
from utils import say_to_user


class CommandExecutor:

    def handle_command(self, command_string):
        command_word = command_string.split(' ')[0]
        command_function = find_command(command_word)
        command_function(command_string)
        if command_function != invalid_command:
            say_to_user('finish_command')
