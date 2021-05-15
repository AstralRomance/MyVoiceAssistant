import yaml

DELAY_TIMEOUT_KEY = "dialog_timeout"
MUSIC_KEY = "music"
TEXT_KEY = "text"
TEXT_TO_VOICE_KEY = "to_voice"
LANGUAGE_KEY = "language"
REMOTE_RECOGNIZER_KEY = "remote_recognizer"
SPEAKER_KEY = "speaker"
MODEL_KEY = "model"
START_PHRASE_KEY = "start_phrase"
MESSAGES_KEY = "messages"
NOTE_FOLDER_KEY = "note_folder"
EMAIL_CONFIG_KEY = "email_config"

EMAIL_KEY = "email"
PASSWORD_KEY = "password"
SERVER_KEY = "server"
PORT_KEY = "port"
CONTACTS_KEY = "contacts"


def _read_yaml(filepath):
    with open(filepath, "r") as file:
        return yaml.load(file, yaml.FullLoader)


CONFIG = _read_yaml('resources/config.yaml')
EMAIL_CONFIG = None
if CONFIG.get(EMAIL_CONFIG_KEY):
    EMAIL_CONFIG = _read_yaml(CONFIG[EMAIL_CONFIG_KEY])
