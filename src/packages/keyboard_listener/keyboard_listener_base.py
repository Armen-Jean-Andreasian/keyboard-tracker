import keyboard
from abc import abstractmethod


class KeyboardListener:
    """
    The flow of the class:
        binding the hook to key press (turn_on_hook)
        running in a while loop
        adding pressed keys to a container

        returning the container on demand
    """

    def __init__(self):
        self.turn_on_hook()

    @abstractmethod
    def on_key_event(self, event):
        """
        The central method of the entire app.
        Determines the pressed key detection rule for the keyboard hook.
        """
        ...

    def turn_on_hook(self):
        """
        Adding a global keyboard listener.
        As we need to call this method only once in a loop, while we move the call to init
        """
        keyboard.hook(self.on_key_event)

    def run(self):
        """
        Instead of running direct while loop here, leaving this stub method as a passable method
        for WhileTrueThread, which will run the loop.

        """
        pass
