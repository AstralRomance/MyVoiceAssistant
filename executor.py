from command.command import find_command


class CommandExecutor:

    def handle_command(self, command_string):
        command_word = command_string.split(' ')[0]
        command_function = find_command(command_word)
        command_function(command_string)
