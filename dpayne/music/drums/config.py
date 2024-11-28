# modules/config.py
import pygame

# Initialize pygame mixer
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

# Drum sounds and corresponding files
DRUM_SOUNDS = [
    {"name": "Kick", "file": "./samples/kick.wav"},
    {"name": "Snare", "file": "./samples/snare.wav"},
    {"name": "Hi-Hat", "file": "./samples/hihat.wav"},
    {"name": "Tom1", "file": "./samples/tom1.wav"},
    {"name": "Tom2", "file": "./samples/tom2.wav"},
    {"name": "Rim", "file": "./samples/rim.wav"},
    {"name": "Clap", "file": "./samples/clap.wav"},
    {"name": "Cowbell", "file": "./samples/cowbell.wav"}
]

# Default settings
DEFAULT_BPM = 120
PATTERN_STEPS = 16
TRACK_COUNT = len(DRUM_SOUNDS)
