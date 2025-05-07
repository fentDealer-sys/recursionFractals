from turtle import *
import tkinter as tk
from PIL import ImageGrab

def capture_window():
    root = getcanvas().winfo_toplevel()
    root.update()
    x = root.winfo_rootx()
    y = root.winfo_rooty()
    width = root.winfo_width()
    height = root.winfo_height()

    bbox = (x, y, x + width, y + height)

    img = ImageGrab.grab(bbox=bbox)

    img.save("turtle_capture.png")
    img.show()