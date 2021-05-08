import webbrowser
from pyowm import OWM

class CommandExecutor:
    def __init__(self):
        self.default_spotify_link = 'https://open.spotify.com/playlist/0fMHBwXC2IFVl1WdniM34J?si=4e45e2270817458b'
        self.weather = OWM('03338ee9abbd8676bd1bdb01e453e966', {'language': 'ru'})
        self.weather_manager = self.weather.weather_manager()
        self.default_city = 'санкт-петербург'

    def handle_command(self, command_string):
        if 'повтор' in command_string.split(' ')[0]:
            self.echo_command(command_string)
        elif 'музык' in command_string.split(' ')[0]:
            self.music_command()
        elif 'погод' in command_string.split(' ')[0]:
            self.weather_command(command_string.split(' '))
        elif (self.echo_command is None) or (self.echo_command == ''):
            return 0

    def music_command(self, spotify_link):
        if not spotify_link:
            spotify_link = self.default_spotify_link
        webbrowser.open(spotify_link)

    def echo_command(self, command_string):
        print(f'You said {command_string}')

    def weather_command(self, command_string):
        print(command_string)
        try:
            if len(command_string) >= 2:
                    weather_data = self.weather_manager.weather_at_place(command_string[1])
                    print(f'Current temperature in {command_string[1]} is {weather_data.get_temperature}\nAlso {weather_data.get_status}')
            else:
                weather_data = self.weather_manager.weather_at_place(self.default_city)
                print(f'Current temperature in {self.default_city} is {weather_data.get_temperature}\nAlso {weather_data.get_status}')
        except Exception as e:
                print(f'Cant get weather with given input')
