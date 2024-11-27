# media-player
Introducing Your Python Media Player
This Python-based media player offers a user-friendly interface and robust audio playback capabilities. Built using Tkinter for the graphical user interface (GUI) and Pygame's Mixer for audio handling, this project provides a comprehensive solution for music enthusiasts and developers alike.
For this project i've used Tkinter and Pygame.Tkinter is the Python's standard UI library very useful for building an intuitive user experience. Meanwhile, Pygame's Mixer module takes charge of the audio backend, handling tasks such as loading audio files, controlling playback, and providing essential audio metadata.When the player is launched, it will interact with your personal music in your music folder.
Underneath the hood, Tkinter event handlers monitor user interactions and trigger corresponding actions. For instance, clicking the play button will trigger the mixer from Pygame to play music.
Getting Started
To run the media player, ensure that you have Python and the required libraries (Tkinter and Pygame) installed. Clone the repository and execute the main script.
I've used for both the buttons and the songs name specific fonts.

 P.S for making the media-player work for your personal device, the only thing that you need to do is change the rootpath to your music-folder adress, like this: rootpath= "your music-folder adress"
