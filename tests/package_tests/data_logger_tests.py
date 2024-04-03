from src.implementations.data_logger import Logger
from src.implementations.data_logger import DataWrapper
from src.packages.json_file_manager import JsonFileManager
import unittest


class DataLoggerTests(unittest.TestCase):
    data = "Good Morning"
    file_path = "logs.json"


class WrapperTest(DataLoggerTests):
    def test_wrapper(self):
        wrapper = DataWrapper.wrap_data(self.data)

        self.assertIs(type(wrapper), dict)
        self.assertGreaterEqual(len(wrapper), 1)

        for key, value in wrapper.items():
            self.assertIsNotNone(value)

        return wrapper


class FileManagerTest(DataLoggerTests):
    def test_write(self):
        dict_content = WrapperTest().test_wrapper()

        JsonFileManager.write(file_path=self.file_path, content=dict_content)

    def test_read1(self):
        FileManagerTest().test_write()  # creating a fresh note to file
        dict_content = WrapperTest().test_wrapper()
        file_content = JsonFileManager.read(self.file_path)

        self.assertEqual(dict_content, file_content)
        self.assertIs(type(file_content), dict)

        print(self.test_read1.__name__, file_content)

    def test_read2(self):
        content = [
            {"date": "02-04-2024 23:53", "content": "fuck"},
            {"date": "03-04-2024 17:08", "content": "Good Morning"},
        ]
        JsonFileManager.write(content=content, file_path=self.file_path)
        content = JsonFileManager.read(file_path=self.file_path)

        self.assertIs(type(content), list)
        print(self.test_read2.__name__, content)


class LoggerTest(DataLoggerTests):
    def test_logger(self):
        content = "fuck"
        Logger.save_log(data=content)
        pass


if __name__ == '__main__':
    unittest.main()
