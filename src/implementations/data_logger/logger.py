from src.packages.json_file_manager import JsonFileManager
from .data_wrapper import DataWrapper
from typing import Optional, Any


class Logger:
    file_path = "logs.json"

    @classmethod
    def save_log(cls, data: Any, file_path: Optional[str] = None) -> None:
        """
        Wraps the data with current date and time (str), in the following pattern:
            wrap = {"date": "DD-MM-YY H:M", "content": data}

        Then adds the wrapped data to a JSON file.
        If the file does not exist a new one will be created, with `logs.json` name in the same directory.
        If the file does not end with .json, adds it to the file

        Args:
            data (list or dict): The log data. Can be a list of dictionaries with logs, or a single log dictionary.
            file_path (str, optional): The path to the JSON file.
                                       If not provided, the default file path specified in the class attribute.

        Raises:
            CustomJsonFileNotFoundError: If the JSON file is not found
            CustomJSONDecodeError: If the given data cant be dumped
            PermissionError: If the file cannot be written due to permission issues.
        """
        content = DataWrapper.wrap_data(data)

        if file_path is not None:
            if file_path.endswith('.json') is False:
                file_path += '.json'
            JsonFileManager.extend(content=content, file_path=file_path)
        else:
            JsonFileManager.extend(content=content, file_path=cls.file_path)

