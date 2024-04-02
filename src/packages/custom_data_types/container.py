class ContainerBase:
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

    def __contains__(self, item):
        return item in self.__container

    def __delete__(self, instance):
        self.__instances.remove(self)
        return self

    def __getitem__(self, item):
        return self.__container[item]

    def __iter__(self):
        for i in self.__container:
            yield i

    def __len__(self):
        return len(self.__container)

    def __reversed__(self):
        return self.__str__()[::-1]

    def __str__(self):
        containing = str(self.__container)[1:-1]
        return "/" + containing + "/"


class Container(ContainerBase):
    def add(self, value):
        self.__container.append(value)

    def clear(self):
        self.__container.clear()
        return self

    @property
    def get(self):
        return self.__container
