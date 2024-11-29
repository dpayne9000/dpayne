import json
import os


def save_pattern(filename, pattern, swing, syncopation, step_offset, bpm):
    """
    Save the current pattern and settings to a file.

    :param filename: Name of the file to save the pattern to.
    :param pattern: The main pattern array.
    :param swing: The swing matrix.
    :param syncopation: Syncopation settings for tracks.
    :param step_offset: Step offset matrix.
    :param bpm: Current BPM.
    """
    data = {
        "pattern": pattern,
        "swing": swing,
        "syncopation": syncopation,
        "step_offset": step_offset,
        "bpm": bpm,
    }
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Pattern saved to {filename}")


def load_pattern(filename):
    """
    Load a pattern and settings from a file.

    :param filename: Name of the file to load the pattern from.
    :return: A dictionary containing the pattern, swing, syncopation, step_offset, and bpm.
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File '{filename}' does not exist.")

    with open(filename, "r") as f:
        data = json.load(f)

    return {
        "pattern": data.get("pattern", []),
        "swing": data.get("swing", []),
        "syncopation": data.get("syncopation", []),
        "step_offset": data.get("step_offset", []),
        "bpm": data.get("bpm", 120),
    }
