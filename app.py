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

mixer.init()

prev_img = tk.PhotoImage(file = "prev_img.png")
stop_img = tk.PhotoImage(file = "stop_img.png")
play_img = tk.PhotoImage(file = "play_img.png")
next_img = tk.PhotoImage(file = "next_img.png")
pause_img = tk.PhotoImage(file = "pause_img.png")

def select():
  label.config(text = listBox.get("anchor"))
  mixer.music.load(rootpath + "/" + listBox.get("anchor"))
  mixer.music.play()

 
def stop():
      mixer.music.stop()
      listBox.select.clear("active")

listBox = tk.Listbox(canvas, fg="cyan", bg = "black", width = 100, font = ('ds-digital', 14))
listBox.pack(padx = 15, pady = 15)

label = tk.Label(canvas, text = "", bg = "black", fg="yellow", font = ('ds-digital', 18))
label.pack(pady = 15)


top = tk.Frame(canvas, bg="black")
top.pack(padx = 10, pady = 5, anchor="center")

prevButton = tk.Button(canvas, text="Prev", image= prev_img, bg="black", borderwidth = 0)
prevButton.pack(pady = 15, in_ = top, side = "left")

stopButton = tk.Button(canvas, text="Stop", image= stop_img, bg="black", borderwidth = 0, command= stop)
stopButton.pack(pady = 15, in_ = top, side = "right")

playButton = tk.Button(canvas, text="Play", image= play_img, bg="black", borderwidth = 0, command= select )
playButton.pack(pady = 15, in_ = top, side = "right")

nextButton = tk.Button(canvas, text="Next", image= next_img, bg="black", borderwidth = 0)
nextButton.pack(pady = 15, in_ = top, side = "right")

pauseButton = tk.Button(canvas, text="Pause", image= pause_img, bg="black", borderwidth = 0)
pauseButton.pack(pady = 15, in_ = top, side = "right")

for root, dirs, files in os.walk(rootpath):
  for filename in fnmatch.filter(files, pattern):
          listBox.insert('end', filename)

canvas.mainloop()