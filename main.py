from src.create import (
    create_dj,
    create_webapp,
    create_settings,
    create_others,
    create_gitignore,
)
from src.utils import decide_path

if __name__ == "__main__":

    project_directory = input(
        "enter your new Dj project directory:)\nleave it blank if you wanna current directory\n->"
    )

    dj_version = input(
        "enter which dj version do you need\nleave it blank if you wanna the last version\n->"
    )

    project_name = input(
        "enter your new Dj project name\nOh!you can not ignore this one..\n->"
    )

    PROJECT_NAME = project_name
    BASE_DIR = decide_path(project_directory)

    if project_name is None:
        raise "please name your project"

    create_dj(project_name=PROJECT_NAME, base_dir=BASE_DIR)
    BASE_DIR = f"{BASE_DIR}/{PROJECT_NAME}"
    create_webapp(project_dir=BASE_DIR)
    create_settings(project_name=PROJECT_NAME, project_dir=BASE_DIR)
    create_gitignore(project_dir=BASE_DIR)
    create_others(project_dir=BASE_DIR)
    print("finished.")
