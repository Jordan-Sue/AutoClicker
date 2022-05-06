from pynput import keyboard


class KeyboardController:
    """A class used to handle keyboard inputs.

    :param keyboard.Listener keyboard_listener: TODO
    :param mouse.Controller mouse: TODO
    :param str correct_key_string: the correct key to signal the mouse
        event
    """

    def __init__(self, mouse_controller, correct_key):
        """Constructor method.

        :param mouse.Controller mouse_controller: TODO
        :param string correct_key: the correct key to signal the mouse
            event
        """

        self.keyboard_listener = keyboard.Listener(self.on_press)
        self.mouse = mouse_controller
        self.correct_key_string = correct_key

        self.keyboard_listener.start()

    def on_press(self, key):
        """If the correct key is pressed, signal the mouse event.

        :param key: the key pressed
        """

        # print(key)
        if self.correct_key_string == str(key):
            self.mouse.clicking = not self.mouse.clicking
            # print(mouse.clicking)
            if self.mouse.clicking:
                self.mouse.event.set()
