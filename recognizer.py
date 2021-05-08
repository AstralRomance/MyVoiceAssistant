import speech_recognition
from loguru import logger


class CustomRecognizer(speech_recognition.Recognizer):
    def __init__(self):
        super().__init__()
        self.my_micro = speech_recognition.Microphone()
        # Minimal number of seconds to recognize commands.
        # Default 1 sec of silence for separate input phrases
        self.phrase_timeout = 1
        self.pause_treshold = self.phrase_timeout

    def listen_commands(self):
        with self.my_micro as audio_input:
            print('Say command')
            self.adjust_for_ambient_noise(audio_input)
            audio = self.listen(audio_input)
        try:
            recognized_text = self.recognize_google(audio, language='ru-RU')
            print(f'Recognized command {recognized_text}')
            if (recognized_text == '') or (recognized_text is None):
                return None
        except speech_recognition.UnknownValueError as e:
                logger.error(f'Cannot recognize with: {e}')
                recognized_text = self.listen_commands()
        return recognized_text.lower()

    