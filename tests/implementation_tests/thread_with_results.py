from src.implementations.side_thread.thread_with_results import WhileTrueThreadWithResults
from src.packages.custom.data_types import Container

func = print
val = "hello world"
duration = 3
container = Container()


infinite_thread = WhileTrueThreadWithResults(container, func, val)
infinite_thread.on()
infinite_thread.wait(3)
infinite_thread.off()
r = infinite_thread.get_results()
print(r)

