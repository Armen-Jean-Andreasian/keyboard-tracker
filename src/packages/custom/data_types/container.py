class ContainerBase:
    __slots__ = ("__container",)
    __instances = set()

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls.__instances.add(instance)
        return instance

    def __init__(self):
        self.__container = []

    def __add__(self, container: "Container") -> "ContainerBase":
        if not isinstance(container, Container):
            raise ValueError(f"{container} is not of type Container")
        else:
            self.__container.extend(container)
            return self

    def __add_value__(self, value):
        self.__container.append(value)

    def __clear__(self):
        self.__container.clear()
        return self

    def __contains__(self, item):
        return item in self.__container

    def __delete__(self, instance):
        self.__instances.remove(self)
        return self

    def __get_container__(self):
        return self.__container

    def __getitem__(self, item):
        return self.__container[item]

    def __iter__(self):
        for i in self.__container:
            yield i

    def __len__(self):
        return len(self.__container)

    def __reversed__(self):
        return reversed(self.__container)

    def __str__(self):
        containing = str(self.__container)[1:-1]
        return "/" + containing + "/"


class Container(ContainerBase):
    def add(self, value):
        self.__add_value__(value)
        return self

    def clear(self):
        self.__clear__()
        return self

    @property
    def get(self):
        return self.__get_container__()
