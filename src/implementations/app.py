from .keyboard_tracker import KeyboardTracker
from src.implementations.side_thread.thread_without_results import WhileTrueThreadWithoutResults
from src.packages.custom.data_types import Container
from .data_logger import Logger


class KeyboardTrackerApp:
    def __init__(self, log_file_name: str = None):
        """
        Initializes the KeyboardTrackerApp.

        Args:
            log_file_name (str, optional): The name/file path of the log file to save the keyboard tracking data.
                                           Default is None.

        """
        self.results_container = Container()

        self.tracker = KeyboardTracker(container=self.results_container)
        self.side_thread = WhileTrueThreadWithoutResults(method=self.tracker.run)

        self.log_file_name = log_file_name
        self.is_thread_off = False

    def track(self, time_active: int) -> Container:
        """
        Starts tracking keyboard activity for a specified duration.

        Args:
            time_active (int): The duration in seconds for which to track keyboard activity.

        Returns:
            Container: The container object containing the tracked keyboard activity data.
        """
        self.side_thread.on()
        self.side_thread.wait(time_active)
        self.is_thread_off = self.side_thread.off()

        return self.__save_results()

    def __save_results(self) -> Container:
        """
        Saves the tracked keyboard activity results to a log file if the side thread is turned off.

        Returns:
            Container: The container object containing the tracked keyboard activity data.

        """

        if self.is_thread_off:
            Logger.save_log(data=self.result, file_path=self.log_file_name)

        return self.result

    @property
    def result(self):
        """
        Gets the tracked keyboard activity results.

        Returns:
            Container: The container object containing the tracked keyboard activity data.

        """
        return self.tracker.result  # or: `self.results_container`, but this approach I like more
