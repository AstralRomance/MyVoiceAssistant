import datetime
import webbrowser

import config
from command.email_handler import EmailSender
from recognizer import RemoteRecognizer
from utils import speak, say_to_user


def invalid_command(full_command=None):
    say_to_user('command_not_found_error')


def echo_command(command_string):
    speak(command_string, lang=config.CONFIG[config.SPEAKER_KEY][config.LANGUAGE_KEY])


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
            say_to_user('what_to_save_error')
            return
        elif len(words) == 2:
            if 'заметк' in words[1]:
                say_to_user('empty_note_error')
                return
            else:
                say_to_user('could_save_only_notes_error')
                return

        if 'заметк' not in words[1]:
            say_to_user('could_save_only_notes_error')
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


def skip_command(ign):
    say_to_user('skip')


SENDER = None

if config.EMAIL_CONFIG:
    SENDER = EmailSender(config.EMAIL_CONFIG[config.EMAIL_KEY], config.EMAIL_CONFIG_KEY[config.PASSWORD_KEY],
                         config.EMAIL_CONFIG[config.SERVER_KEY], config.EMAIL_CONFIG[config.PORT_KEY])


def email_command(full_command):
    def listen_data():
        record = None
        i = 0
        while not record:
            record = rec.listen_micro()
            i += 1
            if i > 20:
                break
        return record

    if not SENDER:
        say_to_user('configure_email_settings_error')
        return
    say_to_user('to_whom')
    rec = RemoteRecognizer(config.CONFIG[config.LANGUAGE_KEY])
    text = listen_data()
    if config.EMAIL_CONFIG.get(config.CONTACTS_KEY):
        contact = config.EMAIL_CONFIG[config.CONTACTS_KEY].get(text)
        if contact:

            say_to_user('say_subject')
            subject = listen_data()
            say_to_user('say_email')
            email_text = listen_data()

            SENDER.send(contact, subject, email_text)
            say_to_user('email_send')
        else:
            say_to_user('no_such_contact_error')
    else:
        say_to_user('no_contacts_error')


def shutdown_command(_):
    say_to_user('bye')
    exit(0)


COMMAND_MODEL = {
    'повтор': echo_command,
    'музык': music_command,
    'погод': None,
    'сохран': SaveCommand(config.CONFIG[config.NOTE_FOLDER_KEY]).save_command,
    'отправ': email_command,
    'забуд': skip_command,
    'пропусти': skip_command,
    'отключ': shutdown_command
}


def find_command(command_name):
    # type: (str) -> callable
    for name, command in COMMAND_MODEL.items():
        if name in command_name:
            return command
    return invalid_command
