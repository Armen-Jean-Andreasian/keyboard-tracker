import keyboard
from typing import TYPE_CHECKING
from src.packages.keyboard_listener import KeyboardListener

if TYPE_CHECKING:
    from src.packages.custom.data_types import Container


class KeyboardTracker(KeyboardListener):
    def __init__(self, container: "Container"):
        """
        :param container: an empty container object to gather the results in during execution.
        Has a property to get it back.
        """
        super().__init__()
        self.container = container

    def on_key_event(self, event):
        """Implementation of on_key_event abstract method for a keyboard tracker app"""
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
            if key is not None:
                self.container.add(key)

    @property
    def result(self):
        """Returns the full container"""
        return self.container
