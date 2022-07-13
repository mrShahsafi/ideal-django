import os
from subprocess import run


def main(project_name="backend",base_dir=''):
    os.makedirs(
        os.path.join(
            base_dir,
            f"{project_name}",
        )
    )
    
    run(
        [
            "django-admin",
            "startproject",
            f"{project_name}",
            f"{base_dir}/{project_name}",
        ]
    )

    print(f"crate at {base_dir}/{project_name}")