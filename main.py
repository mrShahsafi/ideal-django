from pathlib import Path
from src.create import (
    create_dj,
    create_mainapp,
)
BASE_DIR = Path('./').resolve().parent.as_posix()

# project_directory = input(
#     "enter your new Dj project directory:)\nleave it blank if you wanna current directory\n->"
# )

# dj_version = input(
#     "enter which dj version do you need\nleave it blank if you wanna the last version\n->"
# )

project_name = input(
    "enter your new Dj project name\nOh!you can not ignore this one..\n->"
)


# if project_directory is None:
#     project_directory = "./"

# if project_name is None:
#     raise "please name your project"

create_dj(project_name=project_name,base_dir=BASE_DIR)

BASE_DIR = f"{BASE_DIR}/{project_name}"
create_mainapp(project_dir=BASE_DIR)



