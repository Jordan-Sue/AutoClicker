from pynput import keyboard


class KeyboardController:
    """A class used to handle keyboard inputs.

    :param object keyboard_listener: a listener object that calls a
        given function when a key on the keyboard is pressed
    :param str correct_key_string: the correct key to signal the mouse
        event
    :param bool popup: represents whether a popup window is displayed
    """

    def __init__(self, correct_key, on_press):
        """Constructor method.

        :param string correct_key: the correct key to signal the mouse
            event
        :param function on_press: the function called when the listener
            detects a keyboard input
        """

        self.keyboard_listener = keyboard.Listener(on_press=on_press)
        self.correct_key_string = correct_key
        self.popup = False

        self.keyboard_listener.start()
