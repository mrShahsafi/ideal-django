from subprocess import run

from ..utils import validate_os


def main(
        project_dir="./",
        django_version=None,
        venv_name="venv",
):

    global command
    global dj

    if django_version is None:
        dj = "django"
    else:
        dj = f"django=={django_version}"

    os_platform = validate_os()

    if os_platform == 'darwin':  # it means mac os (https://discussions.apple.com/thread/1384968)
        command = f"cd {project_dir} && virtualenv {venv_name} && pip install {dj}"

    elif os_platform == 'linux':
        command = f"python3 - m {venv_name} {project_dir} && pip install {dj}"

    run(
        command,
        shell=True
    )