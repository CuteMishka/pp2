import pygame
import os

class MusicPlayer:
    def __init__(self, path):
        self.path = path
        self.files = [f for f in os.listdir(path) if f.endswith(('.mp3', '.wav'))]
        self.idx = 0
        self.playing = False

    def play(self):
        if self.files:
            if not self.playing:
                pygame.mixer.music.load(os.path.join(self.path, self.files[self.idx]))
                pygame.mixer.music.play()
                self.playing = True
            else:
                pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.pause()
        self.playing = False

    def next(self):
        if self.files:
            self.idx = (self.idx + 1) % len(self.files)
            self.playing = False
            self.play()

    def prev(self):
        if self.files:
            self.idx = (self.idx - 1) % len(self.files)
            self.playing = False
            self.play()