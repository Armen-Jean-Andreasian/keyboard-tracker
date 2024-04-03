# Are served more abstract errors
from .custom_error_base import CustomError


class CustomFileNotFoundError(CustomError):
    """
    If the file is not found.

    Usage Example:
        try:
            ...
        except FileNotFoundError as error:
            raise CustomFileNotFoundError(error) from None

    """

    def __init__(self, error):
        super().__init__(error)
        self.custom_description = f"The specified file does not exist by: '{error.filename}'."


class CustomTypeError(CustomError):
    """
    If unexpected type.

    Usage Example:
        try:
            ...
        except TypeError as error:
            raise CustomTypeError(error, expected_type=int, given=str) from None
    """

    def __init__(self, error, expected_type: type = None, given: type = None):
        super().__init__(error)
        if expected_type and given:
            self.custom_description = f"Expected {expected_type}, got {given}"
        else:
            self.custom_description = f"{error.__str__()}'. "
