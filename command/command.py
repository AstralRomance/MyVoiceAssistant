import datetime
import webbrowser
from utils import speak


def invalid_command(full_command=None):
    print("Command not found")


def echo_command(command_string):
    speak(command_string, lang='ru')


def music_command(full_command):
    # type: (str) -> None
    default_spotify_link = 'https://open.spotify.com/playlist/0fMHBwXC2IFVl1WdniM34J?si=4e45e2270817458b'
    words = full_command.split(' ')
    if len(words) < 2:
        invalid_command()
        return

    spotify_link = words[1]
    webbrowser.open(spotify_link)


class SaveCommand:
    def __init__(self, folder):
        self._folder = folder

    def save_command(self, full_command):
        # type: (str)->None
        words = full_command.split(' ')
        if len(words) < 2:
            print("Не ясно что сохранять")
            return
        elif len(words) == 2:
            if 'заметк' in words[1]:
                print("Пустая заметка")
                return
            else:
                print("Могу сохранить только заметки")
                return

        if 'заметк' not in words[1]:
            print("Могу сохранить только заметки")
            return
        text = full_command[len((words[1] + words[0])) + 2:]
        time = datetime.datetime.now()
        with open(
                "{}/note-{}-{}-{}-{}-{}-{}".format(self._folder, time.year, time.month, time.day, time.hour,
                                                   time.minute,
                                                   time.second), "w") as file:
            file.write(text)


class ReadCommand:
    def __init__(self, folder):
        self._folder = folder


COMMAND_MODEL = {
    'повтор': echo_command,
    'музык': music_command,
    'погод': None,
    'сохран': SaveCommand("./").save_command,
    'отправ': None,
    'прочит': None,
    'забуд': None
}


def find_command(command_name):
    # type: (str) -> callable
    for name, command in COMMAND_MODEL.items():
        if name in command_name:
            return command
    return invalid_command
