import keyboard


def on_key_event(event):
    print(f'key pressed: {event.name}')


keyboard.hook(on_key_event)


