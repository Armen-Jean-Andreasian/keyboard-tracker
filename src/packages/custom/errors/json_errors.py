from .custom_error_base import CustomError
from .custom_generic_errors import CustomFileNotFoundError


class CustomJsonFileNotFoundError(CustomFileNotFoundError):
    """
    If the JSON file is not found

    Usage Example:
            try:
                with open()...
                    ...
                except FileNotFoundError as error:
                    raise JsonFileNotFoundError(error) from None

    """

    def __init__(self, error):
        super().__init__(error)
        self.custom_description = f"The specified JSON file does not exist by: '{error.filename}'."


class CustomJSONDecodeError(CustomError):
    """
    Custom error class for handling JSON decoding errors.
    """

    def __init__(self, error):
        super().__init__(error)
        self.custom_description = (
            f"JSONDecodeError: {error.msg}")
