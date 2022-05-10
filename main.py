from tkinter import *
from tkinter import ttk

import MouseController
import KeyboardController
import json_read_write

x = "this is a test commit"


def on_close(window):
    keyboard.popup = False
    mouse.picking = False
    mouse.window = None
    window.destroy()


def create_popup(message):
    popup = Toplevel(root)
    popup.title("Error")
    popup.geometry(str(x_size) + "x"
                   + str(int(y_size / 4)) + "+"
                   + str(x_offset) + "+"
                   + str(int(y_offset + y_size * 0.75 / 2)))
    popup.resizable(False, False)
    popup.columnconfigure(0, weight=1)
    popup.rowconfigure(0, weight=1)
    ttk.Label(popup, text=message).grid(column=0, row=0)
    mouse.window = popup

    popup.grab_set()
    keyboard.popup = True
    popup.protocol("WM_DELETE_WINDOW", lambda arg=popup: on_close(arg))


def change_hour(x, y, z):
    if hour_text.get() == "":
        settings["delay"][0] = 0
    elif not hour_text.get().isdigit():
        hour_text.set("".join(filter(lambda a: a.isdigit(), hour_text.get())))
        create_popup("Only digits are allowed in this field.")
    else:
        settings["delay"][0] = int(hour_text.get())
    mouse.set_delay(calc_delay())


def change_min(x, y, z):
    if min_text.get() == "":
        settings["delay"][1] = 0
    elif not min_text.get().isdigit():
        min_text.set("".join(filter(lambda a: a.isdigit(), min_text.get())))
        create_popup("Only digits are allowed in this field.")
    else:
        settings["delay"][1] = int(min_text.get())

    mouse.set_delay(calc_delay())


def change_sec(x, y, z):
    if sec_text.get() == "":
        settings["delay"][2] = 0
    elif not sec_text.get().isdigit():
        sec_text.set("".join(filter(lambda a: a.isdigit(), sec_text.get())))
        create_popup("Only digits are allowed in this field.")
    else:
        settings["delay"][2] = int(sec_text.get())
    mouse.set_delay(calc_delay())


def change_ms(x, y, z):
    if ms_text.get() == "":
        settings["delay"][3] = 0
    elif not ms_text.get().isdigit():
        ms_text.set("".join(filter(lambda a: a.isdigit(), ms_text.get())))
        create_popup("Only digits are allowed in this field.")
    else:
        settings["delay"][3] = int(ms_text.get())
    mouse.set_delay(calc_delay())


def calc_delay():
    temp = (settings["delay"][0] * 3600
            + settings["delay"][1] * 60
            + settings["delay"][2]
            + settings["delay"][3] * 0.001)
    if temp == 0:
        return 0.0001
    else:
        return temp


def change_position(x, y, z):
    settings["select"] = position_select.get()
    if position_select.get():
        mouse.custom = True
    else:
        mouse.custom = False


def pick():
    mouse.picking = True
    # TODO: Title of window is error
    create_popup("Click a location on the screen.")


def replace(x, y):
    x_text.set(str(x))
    settings["position"][0] = x
    mouse.x = x
    y_text.set(str(y))
    settings["position"][1] = y
    mouse.y = y
    on_close(mouse.window)


def change_x(x, y, z):
    if x_text.get() == "":
        settings["position"][0] = 0
    elif not x_text.get().isdigit():
        x_text.set("".join(filter(lambda a: a.isdigit(), x_text.get())))
        create_popup("Only digits are allowed in this field.")
    else:
        settings["position"][0] = int(x_text.get())


def change_y(x, y, z):
    if y_text.get() == "":
        settings["position"][1] = 0
    elif not y_text.get().isdigit():
        y_text.set("".join(filter(lambda a: a.isdigit(), y_text.get())))
        create_popup("Only digits are allowed in this field.")
    else:
        settings["position"][1] = int(y_text.get())


if __name__ == "__main__":
    # main window
    x_size = 400
    y_size = 400
    settings = json_read_write.load_settings()
    mouse = MouseController.MouseController(calc_delay(), replace, None,
                                            settings["position"][0],
                                            settings["position"][1])
    keyboard = KeyboardController.KeyboardController(mouse, settings["key"])
    root = Tk()
    root.title("Keyboard/Mouse Automated Input")
    x_offset = int(root.winfo_screenwidth() / 2 - x_size / 2)
    y_offset = int(root.winfo_screenheight() / 2 - y_size / 2)
    root.geometry(str(x_size) + "x" + str(y_size) + "+"
                  + str(x_offset) + "+" + str(y_offset))
    root.resizable(False, False)

    # click interval
    click_frame = ttk.LabelFrame(root, border=5, text="Click Interval")
    click_frame.pack(fill="x", padx=5, pady=5)

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

    # cursor position
    position_frame = ttk.LabelFrame(root, border=5, text="Cursor Position")
    position_frame.pack(fill="x", padx=5, pady=5)

    position_frame.columnconfigure(0, weight=2)
    for i in range(1, 7):
        position_frame.columnconfigure(i, weight=1)

    position_select = IntVar()
    position_select.set(settings["select"])
    ttk.Radiobutton(position_frame, text="Current location",
                    value=0, variable=position_select).grid(column=0, row=0)
    ttk.Radiobutton(position_frame, value=1,
                    variable=position_select).grid(column=1, row=0, sticky=E)
    position_select.trace_add("write", change_position)

    ttk.Button(position_frame, text="Pick location",
               command=pick).grid(column=2, row=0, sticky=W)

    x_text = StringVar()
    x_text.set(settings["position"][0])
    ttk.Entry(position_frame, justify=RIGHT,
              textvariable=x_text, width=5).grid(column=3, row=0, sticky=E)
    ttk.Label(position_frame, text="X").grid(column=4, row=0, sticky=W)
    x_text.trace_add("write", change_x)

    y_text = StringVar()
    y_text.set(settings["position"][1])
    ttk.Entry(position_frame, justify=RIGHT,
              textvariable=y_text, width=5).grid(column=5, row=0, sticky=E)
    ttk.Label(position_frame, text="Y").grid(column=6, row=0, sticky=W)
    y_text.trace_add("write", change_y)

    root.mainloop()

    json_read_write.save_settings(settings)
