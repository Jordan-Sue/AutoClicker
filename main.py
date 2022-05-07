from tkinter import *
from tkinter.ttk import *

import MouseController
import KeyboardController
import json_read_write


def autoclick():
    print("hahaha")


def record():
    print("I'm watching :)")


def playback():
    print("playing now")


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
    Button(frame, text="Record", command=record).grid(column=0, row=1)
    Button(frame, text="Playback", command=playback).grid(column=0, row=2)

    settings = json_read_write.load_settings()
    mouse = MouseController.MouseController(settings["delay"])
    keyboard = KeyboardController.KeyboardController(mouse, settings["key"])

    root.mainloop()

    json_read_write.save_settings(settings)
