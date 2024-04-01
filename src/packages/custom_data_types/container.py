class Container:
    """
    Mutable data type which:
    - Allows adding new item(s)
    - Disallows removing the items by one
    - Allows clearing all items
    - Allows deleting the instance from memory
    """
    __slots__ = ("__container",)
    __instances = set()

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls.__instances.add(instance)
        return instance

    def __init__(self):
        self.__container = []

    def add(self, value):
        self.__container.append(value)

    @property
    def get(self):
        return self.__container

    def clear(self):
        self.__container.clear()
        return self

    def __str__(self):
        containing = str(self.__container)[1:-1]
        return "/" + containing + "/"
