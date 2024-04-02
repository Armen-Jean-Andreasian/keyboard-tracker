from src.packages.custom_data_types import Container

c = Container()

c.add(2)
c.add(3)
c.add(4)
c.add(4)
c.add(4)
print(c.__reversed__())