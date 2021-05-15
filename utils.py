import os
import tempfile
from datetime import datetime

from gtts import gTTS
from playsound import playsound


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
    # TODO: make voice + text
    print(message_id)
