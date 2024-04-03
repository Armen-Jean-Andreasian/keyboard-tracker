from typing import Any, Iterator, TypeAlias
from typing import Container as TypingContainer

UnderlyingContainer: TypeAlias = TypingContainer



class ContainerBase:
    """
    Mutable data type which:
    - Allows adding new item(s)
    - Disallows removing the items by one
    - Allows clearing all items
    - Allows deleting the instance from memory
    """
    __slots__: tuple
    __instances: set

    def __new__(cls, *args, **kwargs):
        ...

    def __init__(self):
        self.__container = []

    def __add__(self, container: Container) -> Container:
        """
        Extend the container by appending all elements from the specified container.

        Args:
            container (Container): The container whose elements will be appended.

        Returns:
            Container: A reference to the modified container.

        Raises:
            ValueError: If the specified container is not of type Container.
        """
        ...

    def __add_value__(self, value: Any) -> None:
        """
        Append a value to the container.

        Args:
            value: The value to append to the container.

        Returns:
            None
        """
        ...

    def __clear__(self) -> None:
        """
        Clear all elements from the container.

        Returns:
            None
        """
        ...

    def __contains__(self, item: Any) -> bool:
        """
        Check if the container contains the specified item.

        Args:
            item: The item to check for in the container.

        Returns:
            bool: True if the item is present in the container, False otherwise.
        """
        ...

    def __delete__(self, instance: Container) -> Container:
        """
        Delete the container instance from memory.

        Args:
            instance: The container instance to delete.

        Returns:
            ContainerBase: A reference to the deleted container instance.
        """
        ...

    def __get_container__(self) -> UnderlyingContainer:
        """
        Get the underlying container.

        Returns:
            List[Any]: The underlying container.
        """
        ...

    def __getitem__(self, index: int) -> Any | IndexError:
        """
        Get the item at the specified index in the container.

        Args:
            index: The index of the item to retrieve.

        Returns:
            Any: The item at the specified index.

        Raises:
            IndexError: If the index is out of range.
        """
        ...

    def __iter__(self) -> Iterator:
        """
        Returns:
            Iterator: An iterator over the elements of the container.
        """
        ...

    def __len__(self) -> int:
        """
        Returns:
            int: The number of elements in the container.
        """
        ...

    def __reversed__(self) -> Iterator:
        """
        Return an iterator that yields the elements of the container in reverse order.

        Returns:
            Iterator: An iterator over the elements of the container in reverse order.
        """
        ...

    def __str__(self) -> str:
        """
        Return a string representation of the container.

        Returns:
            str: A string representation of the container.
        """
        ...


class Container(ContainerBase):
    def add(self, value: Any) -> Container:
        """
        Add a value to the container.

        Args:
            value (Any): The value to add to the container.
        """
        self.__add_value__(value)
        return self

    def clear(self) -> "Container":
        """
        Clear all elements from the container.
        """
        self.__clear__()
        return self

    @property
    def get(self) -> UnderlyingContainer:
        """
        Get the underlying container.

        Returns:
            UnderlyingContainer: The underlying container.
        """
        return self.__get_container__()

