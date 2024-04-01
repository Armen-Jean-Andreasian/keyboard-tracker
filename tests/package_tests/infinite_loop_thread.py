from src.packages.thread import WhileTrueThread

func = print
val = "hello world"
duration = 3

infinite_thread = WhileTrueThread(func, val)
infinite_thread.on()
infinite_thread.wait(duration)
infinite_thread.off()
