# FOR OFFLINE TESTS. NOT VALID NOW
import pyaudio
import json
from vosk import Model, KaldiRecognizer

def setup_helper():
    model = Model('model')
    recognizer = KaldiRecognizer(model, 16000)

    commands_audio = pyaudio.PyAudio()
    audio_stream = commands_audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
    audio_stream.start_stream
    return recognizer, audio_stream