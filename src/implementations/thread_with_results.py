from src.packages.thread import WhileTrueThread
from src.packages.custom_data_types import Container
from typing import Callable, Any, Optional


class WhileTrueThreadWithResults(WhileTrueThread):
    def __init__(self, container: Container, method: Callable, *method_args, **method_kwargs):
        super().__init__(method, *method_args, **method_kwargs)

        self.container = container

    def _method_for_thread(self):
        """Wrapped function to run in an infinite loop and gather the results into the container,
        until the thread is not implicitly terminated"""
        while True:
            if self.side_thread.is_dead():  # stopping the loop
                break
            else:  # keeping the loop
                self.container.add(self.method(*self.method_args, *self.method_kwargs))

    def get_results(self):
        return self.container





