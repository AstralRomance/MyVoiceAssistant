from pyowm import OWM

from command.command import find_command


class CommandExecutor:
    def __init__(self):
        self.weather = OWM('03338ee9abbd8676bd1bdb01e453e966', {'language': 'ru'})
        self.weather_manager = self.weather.weather_manager()
        self.default_city = 'санкт-петербург'

    def handle_command(self, command_string):
        command_word = command_string.split(' ')[0]
        command_function = find_command(command_word)
        command_function(command_string)
