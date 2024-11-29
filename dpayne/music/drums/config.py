# modules/config.py
import pygame

# Initialize pygame mixer
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

# Drum sounds and corresponding files
SAMPLES_DIR = "./dpayne/music/drums/samples/"
DRUM_SOUNDS = [
    {"name": "Kick", "file": f"{SAMPLES_DIR}kick.wav"},
    {"name": "Snare", "file": f"{SAMPLES_DIR}snare.wav"},
    {"name": "Hi-Hat", "file": f"{SAMPLES_DIR}hihat.wav"},
    {"name": "Tom1", "file": f"{SAMPLES_DIR}tom1.wav"},
    {"name": "Tom2", "file": f"{SAMPLES_DIR}tom2.wav"},
    {"name": "Rim", "file": f"{SAMPLES_DIR}rim.wav"},
    {"name": "Clap", "file": f"{SAMPLES_DIR}clap.wav"},
    {"name": "Cowbell", "file": "./samples/cowbell.wav"},
]

# Default settings
DEFAULT_BPM = 120
PATTERN_STEPS = 16
TRACK_COUNT = len(DRUM_SOUNDS)
