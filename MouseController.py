from pynput import mouse
from pynput.mouse import Button
import threading
import time


class MouseController:
    """A class used to control the mouse and enable automated clicking.

    :param mouse.Controller mouse_controller:
    :param bool clicking: a boolean dictating whether clicking should be
        on or not
    :param delay: the number of seconds between each click
    :param threading.Thread clicking_thread: the thread the infinite
        clicking loop will run on
    :param threading.Event event: the event that blocks the infinite
        clicking loop unless signaled
    """

    def __init__(self, delay):
        """Constructor method.

        :param delay: the number of seconds between each click
        """

        self.mouse_controller = mouse.Controller()
        self.clicking = False
        self.delay = delay
        self.clicking_thread = threading.Thread(target=self.infinite_click,
                                                daemon=True)
        self.event = threading.Event()
        self.clicking_thread.start()

    def set_position(self, x, y):
        """Set the mouse to the coordinate (x,y).

        :param x: the x coordinate of the screen
        :param y: the y coordinate of the screen
        """

        self.mouse_controller.position = (x, y)

    def infinite_click(self):
        """Click the mouse with a given delay between each click.

        This function runs infinitely waiting for a signal each
        iteration, and when the signal is received clicking will
        commence only if the boolean "clicking" is set to true.
        """

        while True:
            self.event.wait()
            while self.clicking:
                time.sleep(self.delay)
                self.mouse_controller.click(Button.left)
                # print(self.m.position)
            self.event.clear()

    def set_delay(self, new_delay):
        """Set the delay to the new given delay.

        :param new_delay: the new number of seconds between clicks
        """

        self.delay = new_delay