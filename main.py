from tkinter import *
from tkinter import ttk

import MouseController
import KeyboardController
import json_read_write


def autoclick():
    print("hahaha")


def record():
    print("I'm watching :)")


def playback():
    print("playing now")


def on_closing(window):
    keyboard.popup = False
    window.destroy()


# def change_hotkey():
#     hotkey_popup = Toplevel(root)
#     hotkey_popup.title("Change Hotkey")
#
#     hotkey_popup.grab_set()
#     keyboard.popup = True
#     hotkey_popup.protocol("WM_DELETE_WINDOW",
#                           lambda arg=hotkey_popup: on_closing(arg))


def change_hour(x, y, z):
    if not (hour_text.get() == ''):
        settings["delay"][0] = int(hour_text.get())
    else:
        settings["delay"][0] = 0
    mouse.set_delay(calc_delay())


def change_min(x, y, z):
    if not (min_text.get() == ''):
        settings["delay"][1] = int(min_text.get())
    else:
        settings["delay"][1] = 0
    mouse.set_delay(calc_delay())


def change_sec(x, y, z):
    if not (sec_text.get() == ''):
        settings["delay"][2] = int(sec_text.get())
    else:
        settings["delay"][2] = 0
    mouse.set_delay(calc_delay())


def change_ms(x, y, z):
    if not (ms_text.get() == ''):
        settings["delay"][3] = int(ms_text.get())
    else:
        settings["delay"][3] = 0
    mouse.set_delay(calc_delay())


def calc_delay():
    return (settings["delay"][0] * 3600
            + settings["delay"][1] * 60
            + settings["delay"][2]
            + settings["delay"][3] * 0.001)


if __name__ == '__main__':
    x_size = 400
    y_size = 400
    settings = json_read_write.load_settings()
    mouse = MouseController.MouseController(calc_delay())
    keyboard = KeyboardController.KeyboardController(mouse, settings["key"])
    root = Tk()
    root.title("Keyboard/Mouse Automated Input")
    x_offset = int(root.winfo_screenwidth() / 2 - x_size / 2)
    y_offset = int(root.winfo_screenheight() / 2 - y_size / 2)
    root.geometry(str(x_size) + "x" + str(y_size) + "+"
                  + str(x_offset) + "+" + str(y_offset))
    root.resizable(False, False)

    click_frame = ttk.LabelFrame(root, border=5, text="Click Delay")
    click_frame.pack(fill='x', padx=5, pady=5)

    for i in range(8):
        click_frame.columnconfigure(i, weight=1)

    hour_text = StringVar()
    hour_text.set(settings["delay"][0])
    ttk.Entry(click_frame, justify=RIGHT,
              textvariable=hour_text, width=7).grid(column=0, row=0)
    ttk.Label(click_frame, text="hour(s)").grid(column=1, row=0)
    hour_text.trace_add("write", change_hour)

    min_text = StringVar()
    min_text.set(settings["delay"][1])
    ttk.Entry(click_frame, justify=RIGHT,
              textvariable=min_text, width=7).grid(column=2, row=0)
    ttk.Label(click_frame, text="min(s)").grid(column=3, row=0)
    min_text.trace_add("write", change_min)

    sec_text = StringVar()
    sec_text.set(settings["delay"][2])
    ttk.Entry(click_frame, justify=RIGHT,
              textvariable=sec_text, width=7).grid(column=4, row=0)
    ttk.Label(click_frame, text="sec(s)").grid(column=5, row=0)
    sec_text.trace_add("write", change_sec)

    ms_text = StringVar()
    ms_text.set(settings["delay"][3])
    ttk.Entry(click_frame, justify=RIGHT,
              textvariable=ms_text, width=7).grid(column=6, row=0)
    ttk.Label(click_frame, text="msec(s)").grid(column=7, row=0)
    ms_text.trace_add("write", change_ms)

    # ttk.Button(click_frame,
    #            text="Interval",
    #            command=change_interval).grid(column=0, row=0)
    # ttk.Button(click_frame,
    #            text="Hotkey",
    #            command=change_hotkey).grid(column=1, row=0)
    # ttk.Button(click_frame,
    #            text="Type",
    #            command=change_interval).grid(column=2, row=0)

    # record_frame = ttk.LabelFrame(root, text="Record")
    # record_frame.pack(anchor="s", expand="yes", fill="x", padx=5, pady=5)
    #
    # ttk.Button(record_frame, text="Autoclick", command=autoclick).grid(column=0, row=0)
    # ttk.Button(record_frame, text="Record", command=record).grid(column=1, row=1)
    # ttk.Button(record_frame, text="Playback", command=playback).grid(column=2, row=2)

    root.mainloop()

    json_read_write.save_settings(settings)
