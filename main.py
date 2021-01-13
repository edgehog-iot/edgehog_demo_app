import time
import os
import tempfile
from signal_handler import SignalHandler
from demo import file_check

SLEEP_TIMER = int(os.environ.get('SLEEP_TIMER', 3))
directory = os.environ.get("CHECK_DIRECTORY", tempfile.gettempdir())
file2check = os.environ.get("CHECK_FILE", "test")

if __name__ == '__main__':
    handler = SignalHandler()
    print("File check started")
    while not handler.halt:
        file_check(os.path.join(directory, file2check))
        time.sleep(SLEEP_TIMER)

    print("File check stopped")
