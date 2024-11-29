# modules/audio.py
import pygame
from .config import DRUM_SOUNDS


def load_sounds():
    sounds = {}
    for sound in DRUM_SOUNDS:
        try:
            sounds[sound["name"]] = pygame.mixer.Sound(sound["file"])
        except FileNotFoundError:
            sounds[sound["name"]] = None
    return sounds


def play_sound(sound_name, sounds):
    if sounds.get(sound_name):
        try:
            sounds[sound_name].play()
        except Exception as e:
            print(f"Error playing {sound_name}: {e}")
    else:
        print(f"Sound not loaded: {sound_name}")
