import json

import pyaudio
import speech_recognition
from loguru import logger
from vosk import Model, KaldiRecognizer


# TODO: make abstract
class RecognizerInterface():
    def listen_micro(self):
        pass


class RemoteRecognizer(speech_recognition.Recognizer, RecognizerInterface):
    def __init__(self):
        super().__init__()
        self.my_micro = speech_recognition.Microphone()
        # Minimal number of seconds to recognize command.
        # Default 1 sec of silence for separate input phrases
        self.phrase_timeout = 1
        self.pause_treshold = self.phrase_timeout

    def listen_micro(self):
        with self.my_micro as audio_input:
            print('Say command')
            self.adjust_for_ambient_noise(audio_input)
            try:
                audio = self.listen(audio_input, timeout=2)
            except:
                return ""
        try:
            recognized_text = self.recognize_google(audio, language='ru-RU')
            print(f'Recognized command {recognized_text}')
            if (recognized_text == '') or (recognized_text is None):
                return ""
        except speech_recognition.UnknownValueError as e:
            logger.error(f'Cannot recognize with: {e}')
            recognized_text = self.listen_micro()
        return recognized_text.lower()


class LocalRecognizer(RecognizerInterface):

    def __init__(self):
        self._model = Model('resources/model')  # полный путь к модели
        self._recognizer = KaldiRecognizer(self._model, 16000)

    def __enter__(self):
        self._p_audio = pyaudio.PyAudio()
        self._stream = self._p_audio.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=16000,
            input=True,
            frames_per_buffer=16000
        )
        self._stream.start_stream()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._stream.stop_stream()
        self._p_audio.close(self._stream)

    def listen_micro(self):
        data = self._stream.read(16000)
        if len(data) == 0:
            return ""

        if self._recognizer.AcceptWaveform(data):
            text = json.loads(self._recognizer.Result()).get('text')
            if text:
                return text
            return ""
