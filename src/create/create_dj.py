import os
from subprocess import run

from .create_venv import main as create_venv


def main(project_name="backend",base_dir='',django_version = None):
    os.makedirs(
        os.path.join(
            base_dir,
            f"{project_name}",
        )
    )
    create_venv(
        project_dir=f"{base_dir}/{project_name}",
        django_version=django_version,
    )

    create_dj_cmd = f"source {base_dir}/{project_name}/venv/bin/activate && django-admin startproject {project_name} {base_dir}/{project_name}"

    run(
        create_dj_cmd,
        shell=True,
    )

    print(f"crate at {base_dir}/{project_name}")