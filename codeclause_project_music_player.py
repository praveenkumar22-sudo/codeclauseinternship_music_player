import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Player")

        # Initialize Pygame mixer
        pygame.mixer.init()

        # Create UI elements
        self.play_button = tk.Button(master, text="Play", command=self.play_music) 
        self.stop_button = tk.Button(master, text="Stop", command=self.stop_music) 
        self.pause_button = tk.Button(master, text="Pause", command=self.pause_music)
        self.select_files_button = tk.Button(master, text="Select Music Files", command=self.select_files)

        # Pack UI elements
        self.play_button.pack()
        self.stop_button.pack()
        self.pause_button.pack()
        self.select_files_button.pack()

        # Initialize music variables
        self.music_files = []

    def select_files(self):
        files_selected = filedialog.askopenfilenames(filetypes=[("MP3 files", "*.mp3")])
        if files_selected:
            self.music_files = list(files_selected)
            if self.music_files:
                self.play_music()

    def play_music(self):
        if self.music_files:
            pygame.mixer.music.load(self.music_files[0])  # Load the first music file
            pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

    def pause_music(self):
        pygame.mixer.music.pause()

def main():
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
 