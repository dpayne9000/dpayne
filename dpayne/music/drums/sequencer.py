# modules/sequencer.py
import time
from .audio import play_sound
from .config import DRUM_SOUNDS


def play_pattern(pattern, sounds, bpm, swing, step_offset, current_step):
    step_duration = 60 / bpm / 4  # Base duration for each step
    start_time = time.time()

    for track_idx, track in enumerate(pattern):
        step_to_play = (current_step + step_offset[track_idx][current_step]) % 16
        if track[step_to_play] == 1:
            # Check swing: Apply a delay or advance for "swing" steps
            swing_delay = (
                0.05 if swing[track_idx][current_step] == 1 else 0
            )  # Example swing adjustment
            time.sleep(swing_delay)  # Apply swing timing
            play_sound(DRUM_SOUNDS[track_idx]["name"], sounds)

    elapsed_time = time.time() - start_time
    time.sleep(max(0, step_duration - elapsed_time))
