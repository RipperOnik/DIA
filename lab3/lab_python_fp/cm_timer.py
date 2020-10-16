import time
from contextlib import contextmanager

# Пока мы в блоке with будет работать yield, после выхода из блока мы вызовем метод stop
@contextmanager
def cm_timer2():
    t = cm_timer1()
    t.start()
    yield t
    t.stop()

class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

# Пока мы в блоке with object будет иметь значение, возвращенное с метода __enter__
# После выхода из блока автоматически вызовется метод __exit__
class cm_timer1:
    def __init__(self):
        self._start_time = None

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

