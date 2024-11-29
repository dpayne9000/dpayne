# modules/interface.py
import curses
from .config import DRUM_SOUNDS


def draw_interface(
    stdscr, current_step, current_track, pattern, bpm, swing, syncopation, step_offset
):
    SWING_LABELS = ["Normal", "Swing"]
    SYNCOPATION_LABELS = ["Normal", "Anacrusis", "Staccato", "Legato"]
    height, width = stdscr.getmaxyx()

    if height < 14 or width < 60:
        stdscr.clear()
        stdscr.addstr(
            0, 0, "Terminal size too small. Please resize and try again.", curses.A_BOLD
        )
        stdscr.refresh()
        return

    stdscr.clear()
    title = "ASCII Drum Machine & 8-Track Sequencer"
    stdscr.addstr(0, (width - len(title)) // 2, title, curses.A_BOLD)

    # Draw the tracks and steps
    for track_idx, track in enumerate(DRUM_SOUNDS):
        # Highlight the current track
        if track_idx == current_track:
            stdscr.addstr(
                2 + track_idx,
                0,
                f"{track['name']:8} |",
                curses.A_REVERSE | curses.A_BOLD,
            )
        else:
            stdscr.addstr(2 + track_idx, 0, f"{track['name']:8} |", curses.A_BOLD)

        for step_idx in range(16):
            if step_idx % 4 == 0 and step_idx != 0:
                stdscr.addstr(2 + track_idx, 10 + step_idx * 2 - 1, "|")

            char = "X" if pattern[track_idx][step_idx] else "-"
            if swing[track_idx][step_idx] == 1:
                char = f"{char}~"  # Add a visual indicator for swing

            if step_idx == current_step:
                stdscr.addstr(2 + track_idx, 10 + step_idx * 2, char, curses.A_REVERSE)
            else:
                stdscr.addstr(2 + track_idx, 10 + step_idx * 2, char)

        stdscr.addstr(
            2 + track_idx,
            45,
            f" Sync: {SYNCOPATION_LABELS[syncopation[track_idx]]:8} | Offset: {step_offset[track_idx][current_step]:2} | Swing: {SWING_LABELS[swing[track_idx][current_step]]:6}",
            curses.A_BOLD,
        )

    # Bottom toolbar
    toolbar = f"BPM: {bpm} | P: Play/Pause | +/-: Adjust BPM | Q: Quit"
    stdscr.addstr(height - 3, 0, toolbar, curses.A_BOLD)
    instructions = "SPACE: Toggle Step | UP/DOWN: Select Track | LEFT/RIGHT: Move Step | S: Adjust Syncopation | O: Adjust Offset | W: Toggle Swing"
    try:
        stdscr.addstr(
            height - 2, (width - len(instructions)) // 2, instructions, curses.A_DIM
        )
    except curses.error:
        print(
            "Error: Terminal size too small. Please resize and try again."
        )  # Ignore if the instructions don't fit on the screen
    stdscr.refresh()
