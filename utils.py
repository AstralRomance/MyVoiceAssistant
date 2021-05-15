import os
import tempfile
from datetime import datetime

from gtts import gTTS
from loguru import logger
from playsound import playsound

import config

MESSAGES = config.CONFIG[config.MESSAGES_KEY]


def text_to_audio_file(text, lang, filepath):
    # type: (str, str, str) -> None
    tts = gTTS(text, lang=lang, tld="com")
    tts.save(filepath)


def speak(text, lang):
    # type: (str, str)-> None
    now = datetime.now().time()
    file = "{}/file-{}".format(tempfile.gettempdir(), now)
    text_to_audio_file(text, lang, file)
    playsound(file)
    os.remove(file)


def say_to_user(message_id):
    logger.debug(f'execute message {message_id}')
    message = MESSAGES.get(message_id)
    if not message:
        logger.error(f'No such message {message_id}')
        return
    musics = message.get(config.MUSIC_KEY, [])
    to_voice = message.get(config.TEXT_TO_VOICE_KEY, [])
    texts = message.get(config.TEXT_KEY, [])

    for music in musics:
        logger.debug(music)
        playsound(music)
    for obj in to_voice:
        speak(obj[config.TEXT_KEY], obj[config.LANGUAGE_KEY])
    for text in texts:
        print(text)
