# media-player
### Video-demo: https://youtu.be/xZOGP5XqH-8
# Introduction
**IMPORTANT**
for making the media-player work for your personal device, the only thing that you need to do is change the rootpath to your music-folder adress, like this: rootpath= "your music-folder adress"
 
This Python-based media player offers a user-friendly interface and robust audio playback capabilities. Built using Tkinter for the graphical user interface (GUI) and Pygame's Mixer for audio handling, this project provides a comprehensive solution for music enthusiasts and developers alike.
For this project i've used Tkinter and Pygame.Tkinter is the Python's standard UI library very useful for building an intuitive user experience. Meanwhile, Pygame's Mixer module takes charge of the audio backend, handling tasks such as loading audio files, controlling playback, and providing essential audio metadata.When the player is launched, it will interact with your personal music in your music folder.
Underneath the hood, Tkinter event handlers monitor user interactions and trigger corresponding actions. For instance, clicking the play button will trigger the mixer from Pygame to play music.
Getting Started
To run the media player, ensure that you have Python and the required libraries (Tkinter and Pygame) installed. Clone the repository and execute the main script.
I've used for both the buttons and the songs name specific fonts.

# Code-Breakdown
Let's break down the code piece by piece:
1. Imports:
import tkinter as tk
import fnmatch
import os
from pygame import mixer

 * import tkinter as tk: This line imports the tkinter library and assigns it an alias tk. Tkinter is Python's standard GUI library for creating graphical user interfaces.
 * import fnmatch: This line imports the fnmatch module which provides functions for matching filenames against a pattern.
 * import os: This line imports the os module which provides functions for interacting with the operating system, like accessing directories and files.
 * from pygame import mixer: This line imports the mixer module from the pygame library. Pygame is a popular library for multimedia programming, and the mixer module is specifically used for playing audio.
2. Window Setup:
canvas = tk.Tk()
canvas.title("Media-player")
canvas.geometry("600x800")
canvas.config(bg = 'black')

 * These lines create the main application window.
   * canvas = tk.Tk(): This line creates a new tkinter window object and assigns it to the variable canvas.
   * .title("Media-player"): This line sets the title of the window to "Media-player".
   * .geometry("600x800"): This line sets the geometry of the window, specifying its width and height as 600x800 pixels.
   * .config(bg = 'black'): This line sets the background color of the window to black.
3. Music Library Path and Song Pattern:
rootpath = "/home/lorenzo/Music"
pattern = "*.mp3"

 * These lines define variables that specify the location of the music library and the pattern to identify music files.
   * rootpath = "/home/lorenzo/Music": This line sets the rootpath variable to the path of the music library on the system. In this case, it's assumed the music library is located in the "Music" folder within my home directory (/home/lorenzo). You'll need to update this path to point to your actual music library location.
   * pattern = "*.mp3": This line sets the pattern variable to "*.mp3" which is a wildcard pattern that matches any filename that ends with the extension ".mp3". This indicates that the application will only consider MP3 files from the specified music library.
4. Initialize Pygame Mixer:
mixer.init()

 * This line initializes the Pygame mixer which is essential for playing audio files.
5. Load Button Images:
prev_img = tk.PhotoImage(file = "prev_img.png")
stop_img = tk.PhotoImage(file = "stop_img.png")
play_img = tk.PhotoImage(file = "play_img.png")
next_img = tk.PhotoImage(file = "next_img.png")
pause_img = tk.PhotoImage(file = "pause_img.png")

 * These lines load images for the buttons using the tk.PhotoImage class. The filenames of the image files (presumed to be "prev_img.png", "stop_img.png", etc.) are specified. Make sure these image files are present in the same directory as your Python script.
6. Define Functions for Button Clicks:
The code defines several functions that are called when the corresponding buttons are clicked. These functions handle media playback controls and updating the music list.
 * select() function:
def select():
  label.config(text = listBox.get("anchor"))
  mixer.music.load(rootpath + "/" + listBox.get("anchor"))
  mixer.music.play()

 * This function is triggered when the "Play" button is clicked.
   * It gets the currently selected song from the listbox using listBox.get("anchor").
   * It updates the label (label) to display the name of the selected song.
   * It constructs the complete file path for the selected song by combining the rootpath and the selected filename.
   * It uses the mixer.music.load function to load the selected song into the Pygame mixer.
   * Finally, it calls mixer.music.play to start playing the loaded song.
