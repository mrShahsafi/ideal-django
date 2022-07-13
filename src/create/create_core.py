from subprocess import run

from ..configs import (
    files_list,
    modules_list,
)


def main(mainapp_name="core", project_dir='./'):
    run(
        [
            "mkdir",
            f"{project_dir}/{mainapp_name}",
        ]
    )
    
    for file_name in files_list:
        
        run(
            [
                "touch",
                f"{project_dir}/{mainapp_name}/{file_name}",
            ]
        )
    for module_name in modules_list:
        
        run(
            [
                "mkdir",
                f"{project_dir}/{mainapp_name}/{module_name}",
            ]
        )
        run(
            [
                "touch",
                f"{project_dir}/{mainapp_name}/{module_name}/__init__.py",
            ]
        )