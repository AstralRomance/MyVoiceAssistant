from datetime import datetime

from config import CONFIG, DELAY_TIMEOUT_KEY
from executor import CommandExecutor
from recognizer import RemoteRecognizer, LocalRecognizer
from waiter import Waiter

remote_recognizer = RemoteRecognizer()
local_recognizer = LocalRecognizer()
command_executor = CommandExecutor()
wait_processor = Waiter(local_recognizer, "привет ассистент")

if __name__ == '__main__':
    while True:
        wait_processor.wait()
        start_time = datetime.now()
        while True:
            text = remote_recognizer.listen_micro()
            print("tttt: " + text)
            if not text:
                current_time = datetime.now()
                if (current_time - start_time).seconds > CONFIG[DELAY_TIMEOUT_KEY]:
                    break
            else:
                start_time = datetime.now()

            command_executor.handle_command(text)
