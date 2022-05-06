from tkinter import *
from tkinter.ttk import *
from pynput import keyboard
import time
import json
import MouseController

settings = {}


def autoclick():
    print("hahaha")


def record():
    print("I'm watching :)")


def playback():
    print("playing now")


def on_press(key):
    if str(key) == settings["button"]:
        mouse.clicking = not mouse.clicking
        print(mouse.clicking)
        if mouse.clicking:
            mouse.event.set()


def load_settings():
    global settings
    with open('settings.json', 'r') as infile:
        settings = json.load(infile)


if __name__ == '__main__':
    load_settings()
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
    Button(frame, text="Record", command=record).grid(column=0, row=1)
    Button(frame, text="Playback", command=playback).grid(column=0, row=2)

    mouse = MouseController.MouseController(settings["delay"])
    mouse.set_position(5.5, 6.2)

    keyboard_listener = keyboard.Listener(
        on_press)
    keyboard_listener.start()
    root.mainloop()
    with open('settings.json', 'w') as outfile:
        json.dump(settings, outfile, indent=4, sort_keys=True)
