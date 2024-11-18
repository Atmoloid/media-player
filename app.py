import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("Media-player")
canvas.geometry("600x800")
canvas.config(bg = 'black')

rootpath = "/home/lorenzo/Music"
pattern = ".*mp3"
listBox = tk.Listbox(canvas, fg="cyan", bg = "black", width = 100)
listBox.pack(padx = 15, pady = 15)

canvas.mainloop()