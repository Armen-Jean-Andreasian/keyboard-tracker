from src.packages.thread.thread_base import WhileTrueThread
from src.packages.custom_data_types import Container
from typing import Callable


class WhileTrueThreadWithResults(WhileTrueThread):
    def __init__(self, container: Container, method: Callable, *method_args, exclude_none=True, **method_kwargs):
        """
        Thread that does collect results in a Container and returns it.

        :param container: The container to gather results in it
        :param method:  The method that should be called in a separate thread
        :param method_args: The args of the method above
        :param exclude_none: If the method returns None, to exclude it or not
        :param method_kwargs: The kwargs of the method
        """
        super().__init__(method, *method_args, **method_kwargs)

        self.container = container
        self.exclude_none = exclude_none

    def _method_for_thread(self):
        """Wrapped function to run in an infinite loop and gather the results into the container,
        until the thread is not implicitly terminated"""
        while True:
            if self.side_thread.is_dead():  # stopping the loop
                break
            else:  # keeping the loop
                r = self.method(*self.method_args, *self.method_kwargs)

                if self.exclude_none:
                    if r is not None:
                        self.container.add(r)
                else:
                    self.container.add(r)

    def get_results(self):
        self.side_thread.thread.join()
        return self.container

