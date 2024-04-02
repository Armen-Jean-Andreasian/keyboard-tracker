from .keyboard_tracker import KeyboardTracker
from .thread_without_results import WhileTrueThreadWithoutResults
from src.packages.custom_data_types import Container


class KeyboardTrackerApp:
    def __init__(self, time_active: int):
        self.results_container = Container()
        self.time_active = time_active

        self.tracker = KeyboardTracker(container=self.results_container)
        self.side_thread = WhileTrueThreadWithoutResults(method=self.tracker.run)

    def track(self) -> Container:
        self.side_thread.on()
        self.side_thread.wait(self.time_active)
        self.side_thread.off()

        return self.tracker.result  # or:  self.results_container

    @property
    def result(self):
        return self.tracker.result
