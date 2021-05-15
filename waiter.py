from datetime import datetime

from recognizer import RecognizerInterface


class Waiter:
    def __init__(self, recognizer, key_phrase):
        # type: (RecognizerInterface, str) -> Waiter
        self._recognizer = recognizer
        self._key_phrase = key_phrase.lower()

    def wait(self, wait_time=None):
        start_time = datetime.now()
        while True:
            with self._recognizer:
                text = self._recognizer.listen_micro()
            print(text)
            current_time = datetime.now()
            print((current_time - start_time).seconds)
            if self._is_phrase_equals_key_phrase(self._key_phrase, text):
                break
            if wait_time and (current_time - start_time).seconds > wait_time:
                break

    # TODO: make it better
    @staticmethod
    def _is_phrase_equals_key_phrase(key_phrase, phrase):
        # type: (str, str) -> bool
        if not phrase or not key_phrase:
            return False
        key_phrase_words = key_phrase.split(' ')
        phrase_words = phrase.split(' ')
        for word in key_phrase_words:
            if word not in phrase_words:
                return False
        return True
