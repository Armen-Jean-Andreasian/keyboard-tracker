## `Container` in [container.py](src%2Fpackages%2Fcustom_data_types%2Fcontainer.py)

Mutable data type which:
- Allows adding new item(s)
- Allows clearing only all items at once
- *Allows deleting the instance from memory (not ready yet)

---
## `WhileTrueThread` in [infinite_loop_thread.py](tests%2Fpackage_tests%2Finfinite_loop_thread.py)

A class of a controllable infinite loop opened in a new thread. With `on`, `off`, `wait` methods. 

Just a like a light switch, once it's on, the bulb will light till the switch is not off again. Same here.

Designed for running non-stop functions in a separate thread.

Yes, with CPU-bound operations it's gonna work in mono thread mode, however, having two threads allows to control and end the infinite loop whenever it's needed using conditions.
While in a single thread writing a functionality to stopping itself but keeping the thread running is not appropriate enough.  

The `wait` method allows to run the thread for a fixed time, same as `time.sleep`. 

---

## `WhileTrueThreadWithResults` in [thread_with_results.py](src%2Fimplementations%2Fthread_with_results.py)

The child class of `WhileTrueThread` which allows to get all results in a `Container`. 








