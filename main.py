from datetime import datetime

from config import CONFIG, DELAY_TIMEOUT_KEY, MODEL_KEY, REMOTE_RECOGNIZER_KEY, LANGUAGE_KEY, START_PHRASE_KEY
from executor import CommandExecutor
from recognizer import RemoteRecognizer, LocalRecognizer
from waiter import Waiter
from utils import say_to_user

remote_recognizer = RemoteRecognizer(CONFIG[REMOTE_RECOGNIZER_KEY][LANGUAGE_KEY])
local_recognizer = LocalRecognizer(CONFIG[MODEL_KEY])
command_executor = CommandExecutor()
wait_processor = Waiter(local_recognizer, CONFIG[START_PHRASE_KEY])

if __name__ == '__main__':
    while True:
        wait_processor.wait()
        say_to_user('ready')
        start_time = datetime.now()
        while True:
            text = remote_recognizer.listen_micro()
            if not text:
                current_time = datetime.now()
                if (current_time - start_time).seconds > CONFIG[DELAY_TIMEOUT_KEY]:
                    break
            else:
                start_time = datetime.now()
            if text:
                command_executor.handle_command(text)
                say_to_user('finish_command')
        say_to_user('bye')
