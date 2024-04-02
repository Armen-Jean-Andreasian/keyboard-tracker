# Keyboard Manager App

![cattie](https://i.pinimg.com/736x/a9/87/a0/a987a02b162eb20680ec8bdcbc9bf275.jpg)


---
## Disclaimer
Usage of this repo for illegal pursuits may harm your mental health, as well as the makeup in the prison.
So do not try to use this for any illegal activities. At least if you are not good at soap dropping.

Moreover, do not spy on your girlfriend, come on. _Just make her pregnant and leave her._ No! Hold on,
I hope you understand that it was a joke, and you will never leave her the half of your house.
Actually, spying on someone who's supposed to be your bro, friend and lover is not cool.

---
## Overview

In this repo you will find:
- how to kill a thread in `Python`.
- how to create a controllable infinite loop.
- how to use `keyboard` package.
- how to follow SOLID rules in hard times.
- how to exit this repo, if you are intolerant to lactose and to "_non-professional_" `README.md` files.

![cattie](https://qph.cf2.quoracdn.net/main-qimg-64d2a98c13c8bd0550c6ae5f9af2a311)


## Versions

- Python: `3.11.5`
- `keyboard`: `0.13.5`
  - Installment
    - ```bash
      pip install keyboard
      ```


---
## Usage

1. Clone the repo
2. Run the `main.py` to see how it works
3. Modify if needed
4. Have fun

---
## Licence

Depends on you. If you are a respectable user, in case of re-publishing you can mention the origin.

---
## TLR 

Well, I was making this app for people who like watching videos/movies with pets.
It should allow them block the input when the pets jump on the keyboard.

Which I haven't done yet, lol. 
Instead of that I created a Keyboard tracker, which saves all pressed buttons to a log file.

The blocker is not done yet. Status: coming soon

---
## Bonus

For Python interviewers who don't know what question to ask, you can find the original `The Light Bulb Task` in [task.txt](task.txt).

If you don't know how to solve it, the `WhileTrueThread` in [thread_base.py](src%2Fpackages%2Fthread%2Fthread_base.py) is the solution.

---
# Professional Documentation af (for real)

---

## `Container` in [container.py](src%2Fpackages%2Fcustom_data_types%2Fcontainer.py)

Mutable data type which:
- Allows adding new item(s)
- Allows clearing only all items at once
- *Allows deleting the instance from memory (not implemented yet)


---

## `KeyboardListener` in [keyboard_listener_base.py](src%2Fpackages%2Fkeyboard_listener%2Fkeyboard_listener_base.py)

Prepacked class of adding a rule on keyboard activities. With `on_key_event` abstract method, for each child class.

---

## `KeyboardTrackerApp` in [keyboard_tracker.py](src%2Fimplementations%2Fkeyboard_tracker.py)
An implementation of `KeyboardListener` for our `KeyboardTrackerApp`.
- As an argument receives a  `Container` object to stash results in it. Has a property to get it back. 
 Which was forced, as `keyboard.hook` method doesn't return anything and everything you have is the callback you need to provide to it.
 And the callback is only spot where you can put additional functionality. So SRP bye, go talk with `keyboard` package, lol.

Contains `on_key_event` method which is the implementation of abstract callback method. Why abstract? It was forced because of the "lovely" design of `keyboard` package.

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

---

## `WhileTrueThreadWithoutResults` in [thread_without_results.py](src%2Fimplementations%2Fthread_without_results.py)

Just a stub class as an interface of`WhileTrueThread` allowing to run a function in a thread.

---

# P.S.
Actually, this is a serious piece of work from a technical standpoint, full of great tips. Don't get it twisted.
