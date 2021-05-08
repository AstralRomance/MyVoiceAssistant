from recognizer import CustomRecognizer
from executor import CommandExecutor

recognize_worker = CustomRecognizer()
command_executor = CommandExecutor()

if __name__ == '__main__':
    while True:
        command_executor.handle_command(recognize_worker.listen_commands())