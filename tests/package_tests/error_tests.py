from src.packages.custom.errors import CustomJSONDecodeError, CustomJsonFileNotFoundError
from src.packages.custom.errors import CustomTypeError
import unittest


class CustomJSONDecodeErrorTest(unittest.TestCase):
    def test(self):
        import json
        invalid_json_str = '{"key": "value",}'

        def failed_read():
            try:
                nonlocal invalid_json_str
                json.loads(invalid_json_str)
            except json.JSONDecodeError as error:
                raise CustomJSONDecodeError(error)

        with self.assertRaises(CustomJSONDecodeError) as context:
            failed_read()

        print(context.exception)


class CustomJsonFileNotFoundErrorTest(unittest.TestCase):
    def test(self):
        def file_not_found():
            try:
                with open('nonexistent_file.json') as _:
                    pass
            except FileNotFoundError as error:
                raise CustomJsonFileNotFoundError(error)

        with self.assertRaises(CustomJsonFileNotFoundError) as context:
            file_not_found()

        print(context.exception)


class CustomTypeErrorTest(unittest.TestCase):
    def test(self):
        divide = lambda x : x / 100

        def type_error():
            try:
                divide('abs')
            except TypeError as error:
                raise CustomTypeError(error)

        with self.assertRaises(CustomTypeError) as context:
            type_error()

        print(context.exception)


if __name__ == '__main__':
    unittest.main()
