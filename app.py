import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("Media-player")
canvas.geometry("600x800")
canvas.config(bg = 'black')

rootpath = "/home/lorenzo/Music"
pattern = "*.mp3"
listBox = tk.Listbox(canvas, fg="cyan", bg = "black", width = 100, font = ('ds-digital', 14))
listBox.pack(padx = 15, pady = 15)

label = tk.Label(canvas, text = "", bg = "black", fg="yellow", font = ('ds-digital', 18))
label.pack(pady = 15)


top = tk.Frame(canvas, bg="black")
top.pack(padx = 10, pady = 5, anchor="center")

prevButton = tk.Button(canvas, text="Prev")
prevButton.pack(pady = 15, in_ = top, side = "left")

stopButton = tk.Button(canvas, text="Pause")
stopButton.pack(pady = 15, in_ = top, side = "right")

for root, dirs, files in os.walk(rootpath):
  for filename in fnmatch.filter(files, pattern):
          listBox.insert('end', filename)

canvas.mainloop()