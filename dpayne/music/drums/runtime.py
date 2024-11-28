import curses
from .interface import draw_interface
from .audio import load_sounds
from .sequencer import play_pattern
from .config import DEFAULT_BPM, PATTERN_STEPS, TRACK_COUNT
from .pattern_io import save_pattern, load_pattern

def main(stdscr):
    bpm = DEFAULT_BPM
    pattern = [[0 for _ in range(PATTERN_STEPS)] for _ in range(TRACK_COUNT)]
    swing = [[0 for _ in range(PATTERN_STEPS)] for _ in range(TRACK_COUNT)]
    syncopation = [0 for _ in range(TRACK_COUNT)]
    step_offset = [[0 for _ in range(PATTERN_STEPS)] for _ in range(TRACK_COUNT)]
    sounds = load_sounds()
    current_step = 0
    current_track = 0
    playing = False

    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(int(60000 / bpm / 4))

    while True:
        draw_interface(stdscr, current_step, current_track, pattern, bpm, swing, syncopation, step_offset)
        key = stdscr.getch()

        if key == ord('q'):
            break
        elif key == ord(' '):
            pattern[current_track][current_step] ^= 1
        elif key == curses.KEY_UP:
            current_track = (current_track - 1) % TRACK_COUNT
        elif key == curses.KEY_DOWN:
            current_track = (current_track + 1) % TRACK_COUNT
        elif key == curses.KEY_LEFT:
            current_step = (current_step - 1) % PATTERN_STEPS
        elif key == curses.KEY_RIGHT:
            current_step = (current_step + 1) % PATTERN_STEPS
        elif key == ord('p'):
            playing = not playing
        elif key == ord('+'):
            bpm = min(bpm + 5, 300)
            stdscr.timeout(int(60000 / bpm / 4))
        elif key == ord('-'):
            bpm = max(bpm - 5, 30)
            stdscr.timeout(int(60000 / bpm / 4))
        elif key == ord('w'):
            swing[current_track][current_step] = (swing[current_track][current_step] + 1) % 2
        elif key == ord('s'):  # Save pattern
            try:
                save_pattern("pattern.json", pattern, swing, syncopation, step_offset, bpm)
            except Exception as e:
                print(f"Error saving pattern: {e}")
        elif key == ord('l'):  # Load pattern
            try:
                data = load_pattern("pattern.json")
                pattern = data["pattern"]
                swing = data["swing"]
                syncopation = data["syncopation"]
                step_offset = data["step_offset"]
                bpm = data["bpm"]
                stdscr.timeout(int(60000 / bpm / 4))
                print("Pattern loaded successfully.")
            except Exception as e:
                print(f"Error loading pattern: {e}")

        if playing:
            play_pattern(pattern, sounds, bpm, swing, step_offset, current_step)
            current_step = (current_step + 1) % PATTERN_STEPS
