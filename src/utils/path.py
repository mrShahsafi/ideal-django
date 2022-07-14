import os.path
from pathlib import Path


def decide_path(dir):
    is_dir = os.path.isdir(dir)

    if dir != '' and is_dir:

        base_dir = dir
    else:
        base_dir = Path('./').resolve().parent.as_posix()

    return base_dir
