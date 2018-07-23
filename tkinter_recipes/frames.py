import tkinter as tk
from tkinter import Frame

class FrameExample(tk.Frame):
    def __init__(self, master, list_of_frames):
        super().init(master)
        self.build_frames(list_of_frames)

    def build_frames(list_of_frames):
        pass


class SubFrame1(tk.Frame):
    def __init__(self, master):
        super().init(master)


class SubFrame2(tk.Frame):
    def __init__(self, master):
        super().init(master)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('test')
    root.mainloop()
