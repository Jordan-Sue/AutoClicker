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
    :param bool picking: represents whether the user is picking a
        position with the mouse
    TODO add params
    """

    def __init__(self, delay, pick_func, window, x, y):
        """Constructor method.

        :param delay: the number of seconds between each click
        :type delay: int or float
        TODO add params
        """

        self.mouse_controller = mouse.Controller()
        self.delay = delay
        self.clicking_thread = threading.Thread(target=self.infinite_click,
                                                daemon=True)
        self.event = threading.Event()
        self.mouse_listener = mouse.Listener(on_click=self.on_press)
        self.picking = False
        ###
        self.pick_func = pick_func
        self.window = window
        self.custom = False
        self.x = x
        self.y = y

        self.clicking_thread.start()
        self.mouse_listener.start()

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
            if self.custom:
                self.set_position(self.x, self.y)
            self.mouse_controller.click(Button.left)
            # print(self.mouse_controller.position)
            time.sleep(self.delay)

    def set_delay(self, new_delay):
        """Set the delay to the new given delay.

        :param new_delay: the new number of seconds between clicks
        :type new_delay: int or float
        """

        self.delay = new_delay

    def on_press(self, x, y, button, pressed):
        """If a condition is met, return x and y, otherwise do nothing.

        :param int x: x value of the cursor
        :param int y: y value of the cursor
        :param enum button: type of button pressed
        :param bool pressed: true when the button is pressed, false when
            the button is released
        """
        if self.picking:
            if not pressed:
                # print(x)
                # print(y)
                self.pick_func(x, y)
