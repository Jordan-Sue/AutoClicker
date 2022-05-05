from tkinter import *
from tkinter.ttk import *
from pynput import mouse
from pynput.mouse import Button as mButton
from pynput import keyboard
import time
import queue
import threading

autoclicking = False
queue = queue.SimpleQueue()


def autoclick():
    print("hahaha")


def record():
    print("I'm watching :)")


def playback():
    if not mouse_inputs:
        print("pop-up -> no recording!")
    else:
        print("playing now")


def f6_pressed(event):
    print("insert repeated clicking here")


def on_press(key):
    global autoclicking
    print("key was pressed!")
    if key == keyboard.Key.f6:
        autoclicking = not autoclicking
        print(autoclicking)
        if autoclicking:
            event.set()


# def on_release(key):
#     print("kms")


def infinite_click():
    while True:
        event.wait()
        while autoclicking:
            time.sleep(0.001)
            m.click(mButton.left)
            print(m.position)
        event.clear()


if __name__ == '__main__':
    root = Tk()
    root.title("Terrible Autoclicker")
    root.geometry("400x400")
    window_width = root.winfo_reqwidth()
    window_height = root.winfo_reqheight()
    x_coord = int(root.winfo_screenwidth() / 2 - window_width / 2)
    y_coord = int(root.winfo_screenheight() / 2 - window_height / 2)
    root.geometry("+" + str(x_coord) + "+" + str(y_coord))
    root.resizable(False, False)

    frame = Frame(root)
    frame.grid()
    Button(frame, text="Autoclick", command=autoclick).grid(column=0, row=0)
    Button(frame, text="Record", command=record).grid(column=1, row=0)
    Button(frame, text="Playback", command=playback).grid(column=2, row=0)

    mouse_inputs = []
    # m = mouse.Controller()
    # mouse = MouseControl.MouseControl()
    # mouse.set_position(500, 500)

    m = mouse.Controller()
    # m.position = (500, 500)

    clicking_thread = threading.Thread(target=infinite_click, daemon=True)
    event = threading.Event()
    clicking_thread.start()

    keyboard_listener = keyboard.Listener(
        on_press)
    keyboard_listener.start()
    root.mainloop()
