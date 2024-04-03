from datetime import datetime


class TimeStamp:
    @staticmethod
    def get() -> str:
        """Returns datetime now in `02-04-2024 23:55` format"""
        return datetime.now().strftime("%d-%m-%Y %H:%M")


class DataWrapper:
    structure = lambda date_value, content_value: {
        "date": date_value,
        "content": content_value
    }

    @classmethod
    def wrap_data(cls, data) -> dict:
        """Wraps data into dict with a timestamp as a key"""
        data = str(data)
        dt_stamp = TimeStamp.get()

        structure = cls.structure(date_value=dt_stamp, content_value=data)
        return structure
