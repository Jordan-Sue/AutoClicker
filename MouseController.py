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
    """

    def __init__(self, delay):
        """Constructor method.

        :param delay: the number of seconds between each click
        :type delay: int or float
        """

        self.mouse_controller = mouse.Controller()
        self.delay = delay
        self.clicking_thread = threading.Thread(target=self.infinite_click,
                                                daemon=True)
        self.event = threading.Event()

        self.clicking_thread.start()

    def set_position(self, x, y):
        """Set the mouse's position to the coordinate (x,y).

        :param x: the x coordinate of the screen
        :type x: int or float
        :param y: the y coordinate of the screen
        :type y: int or float
        """

        self.mouse_controller.position = (x, y)

    def infinite_click(self):
        """Click the mouse with a given delay between each click.

        This function runs infinitely waiting on a thread event to
        either begin or halt clicking.
        """

        while True:
            self.event.wait()
            self.mouse_controller.click(Button.left)
            # print(self.mouse_controller.position)
            time.sleep(self.delay)

    def set_delay(self, new_delay):
        """Set the delay to the new given delay.

        :param new_delay: the new number of seconds between clicks
        :type new_delay: int or float
        """

        self.delay = new_delay
