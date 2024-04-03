import os.path
from typing import Union, List
import json
from src.packages.custom.errors import CustomJsonFileNotFoundError, CustomJSONDecodeError, CustomTypeError


class JsonFileManager:
    """A utility class for reading from and writing to JSON files."""

    @staticmethod
    def check_file_path_exists(file_path: str):
        if os.path.exists(path=file_path) is False:
            with open(file_path, 'w') as file:
                json.dump([], file)
        return True

    @staticmethod
    def read(file_path: str) -> dict | list:
        """
        Read JSON data from a file.

        Args:
            file_path (str): The path to the JSON file.

        Raises:
            CustomJsonFileNotFoundError: If the specified file does not exist.
            CustomJSONDecodeError: If the JSON data in the file is not valid.

        """
        try:
            with open(file_path, mode='r', encoding='utf-8') as json_file:
                return json.load(json_file)
        except FileNotFoundError as fnf_error:
            raise CustomJsonFileNotFoundError(fnf_error) from None
        except json.JSONDecodeError as jd_error:
            raise CustomJSONDecodeError(jd_error) from None

    @staticmethod
    def write(file_path: str, content: dict | list[dict]) -> None:
        """
        Write JSON data to a file.

        Args:
            file_path (str): The path to the JSON file.
            content (dict): The dictionary containing the data to be written to the file.

        Raises:
            CustomTypeError: If `dict_content` is not a json.dump-able.
            PermissionError: If the file cannot be written due to permission issues.
        """

        try:
            with open(file_path, mode='w', encoding='utf-8') as file_handle:
                json.dump(content, file_handle, indent=4)
        except TypeError as t_error:
            raise CustomTypeError(error=t_error, expected_type=dict, given=type(content))

    @staticmethod
    def extend(file_path: str, content: Union[dict, List[dict]]) -> None:
        """
        Extends the JSON file with data.
        If the file doesn't exist, it will create it.

        Args:
            file_path (str): The path to the JSON file.
            content (dict): The dictionary containing the data
            content (list): A list containing dictionaries with the data

        Raises:
            CustomTypeError: If `dict_content` is not a dictionary.
            PermissionError: If the file cannot be written due to permission issues.
        """
        JsonFileManager.check_file_path_exists(file_path)

        old_content: list | dict = JsonFileManager.read(file_path)
        new_containing = list()

        # handling old content
        if len(old_content) > 0:
            if isinstance(old_content, dict):
                new_containing.append(old_content)
            elif isinstance(old_content, list):
                new_containing.extend(old_content)

        del old_content

        # handling new content
        if isinstance(content, dict):
            new_containing.append(content)
        elif isinstance(content, list):
            new_containing += content

        # saving
        JsonFileManager.write(file_path=file_path, content=new_containing)
