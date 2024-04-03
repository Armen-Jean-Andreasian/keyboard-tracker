import traceback
import json


class CustomError(Exception):
    def __init__(self, error):
        self.traceback_info = str(traceback.extract_tb(error.__traceback__)[0]).split('FrameSummary file ')[1]
        self.custom_description: str = ...

    def __str__(self):
        message_dict = {
            "Description": self.custom_description,
            "Traceback": self.traceback_info,
        }

        return json.dumps(message_dict, indent=4)
