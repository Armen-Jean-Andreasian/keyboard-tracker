from src.packages.thread.thread_base import WhileTrueThread
from typing import Callable


class WhileTrueThreadWithoutResults(WhileTrueThread):
    def __init__(self, method: Callable, *method_args, **method_kwargs):
        """
        Just an interface designed for specific methods/structures that don't implicitly return a value.
        This class just run  the method without invoking the values out of it.
        That should be done by the method itself, to keep track of the results

        :param method:  The method that should be called in a separate side_thread
        :param method_args: The args of the method above
        :param method_kwargs: The kwargs of the method

        """
        super().__init__(method, *method_args, **method_kwargs)


