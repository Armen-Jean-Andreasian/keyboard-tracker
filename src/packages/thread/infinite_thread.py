import threading
import time
from typing import Callable, Any, Optional


class SideThread:
    def __init__(self, target: Callable[..., Any], target_args: Optional[list | tuple] = (), timeout: int = 0):
        """

        :param target: Function to run in a new thread.
        :param target_args: Arguments passed to function
        :param timeout: see
        `threading.Event.wait <https://docs.python.org/3/library/threading.html#threading.Condition.wait>`_
        """
        self.timeout = timeout
        self.thread = threading.Thread(target=target, args=target_args)
        self.event = threading.Event()

    def run(self):
        self.thread.start()
        return self

    def stop(self):
        self.event.set()
        return self

    def is_dead(self):
        """
        Returns True if the event is set (stopped).

        Also, False if the timeout is reached, otherwise wait for the event to complete.
        `threading.Event.wait <https://docs.python.org/3/library/threading.html#threading.Condition.wait>`_
        """
        return self.event.wait(self.timeout)


class WhileTrueThread:
    def __init__(self, func: Callable, *method_args, timeout: int = 0, **method_kwargs):
        """
        :param func: The callable (function) that should be run in a separate thread
        :param method_args: The args of the function
        :param timeout:  block rate (in seconds)
        `Read the documentation <https://docs.python.org/3/library/threading.html#threading.Condition.wait>`_
        :param method_kwargs: The kwargs of the function

        """
        self.method = func
        self.method_args: tuple = method_args
        self.method_kwargs: dict = method_kwargs

        self.side_thread = SideThread(target=self._method_for_thread, timeout=timeout)

    def on(self):
        """Turns on the side thread"""
        self.side_thread.run()
        return self

    def off(self):
        """Turns off the side thread"""
        self.side_thread.stop()
        return self

    def wait(self, sec: int):
        """Implicitly let the side thread run for `sec` amount of seconds """
        time.sleep(sec)
        return self

    def _method_for_thread(self):
        """Wrapped function to run in an infinite loop until the thread is not implicitly terminated"""
        while True:
            if self.side_thread.is_dead():  # stopping the loop
                break
            else:  # keeping the loop
                self.method(*self.method_args, *self.method_kwargs)
