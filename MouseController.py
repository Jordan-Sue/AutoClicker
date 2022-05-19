import time
import threading

from pynput import mouse
from pynput.mouse import Button


class MouseController:
    """A class used to control the mouse and enable automated clicking.

    :param object mouse_controller: a mouse controller object
        to enable mouse manipulation via the pynput library
    :param delay: the number of seconds between each click
    :type delay: int or float
    :param threading.Thread clicking_thread: the thread the infinite
        clicking loop will run on
    :param threading.Event event: the event that blocks the infinite
        clicking loop unless signaled
    :param object mouse_listener: a listener object that calls a
        given function when a mouse button is pressed or released
    :param dict settings: the dictionary of settings used to keep track
        of user inputs
    :param bool picking: represents whether the user is picking a
        position with the mouse
    """

    def __init__(self, delay, on_click, settings):
        """Constructor method.

        :param delay: the number of seconds between each click
        :type delay: int or float
        :param function on_click: the function called when the listener
            detects a change in the mouse
        :param dict settings: the dictionary of settings used to keep
            track of user inputs
        """

        self.mouse_controller = mouse.Controller()
        self.delay = delay
        self.clicking_thread = threading.Thread(target=self.infinite_click,
                                                daemon=True)
        self.event = threading.Event()
        self.mouse_listener = mouse.Listener(on_click=on_click)
        self.settings = settings
        self.picking = False

        self.clicking_thread.start()
        self.mouse_listener.start()

    def infinite_click(self):
        """Click the mouse with a given delay between each click.

        This function runs infinitely on its own thread waiting on a
        thread event to either begin or halt clicking.
        """

        while True:
            self.event.wait()
            if self.settings["select"]:
                self.mouse_controller.position = (self.settings["position"][0],
                                                  self.settings["position"][1])
            self.mouse_controller.click(Button.left)
            # print(self.mouse_controller.position)
            time.sleep(self.delay)
