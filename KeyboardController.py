from pynput import keyboard


class KeyboardController:
    """A class used to handle keyboard inputs.

    :param object keyboard_listener: a listener object that calls a
        given function when a key on the keyboard is pressed
    :param object mouse: a mouse controller object to enable
        mouse manipulation via the pynput mouse library
    :param str correct_key_string: the correct key to signal the mouse
        event
    """

    def __init__(self, mouse_controller, correct_key):
        """Constructor method.

        :param object mouse_controller: a mouse controller object to enable
            mouse manipulation via the pynput mouse library
        :param string correct_key: the correct key to signal the mouse
            event
        """

        self.keyboard_listener = keyboard.Listener(self.on_press)
        self.mouse = mouse_controller
        self.correct_key_string = correct_key

        self.keyboard_listener.start()

    def on_press(self, key):
        """If the correct key is pressed, signal the mouse event.

        :param object key: the key object pressed
        """

        # print(key)
        if self.correct_key_string == str(key):
            self.mouse.clicking = not self.mouse.clicking
            # print(mouse.clicking)
            if self.mouse.clicking:
                self.mouse.event.set()
