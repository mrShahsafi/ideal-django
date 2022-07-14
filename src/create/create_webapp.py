from subprocess import run

from ..configs import (
    files_list,
    modules_list,
    apps_content,
)


def main(mainapp_name="core", project_dir='./'):

    webapp_dir = f"{project_dir}/{mainapp_name}"

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
                f"{webapp_dir}/{file_name}",
            ]
        )
    for module_name in modules_list:
        
        run(
            [
                "mkdir",
                f"{webapp_dir}/{module_name}",
            ]
        )
        run(
            [
                "touch",
                f"{webapp_dir}/{module_name}/__init__.py",
            ]
        )

    with open(f"{webapp_dir}/apps.py", 'w+') as outfile:
        outfile.write(
            apps_content(app_name=mainapp_name)
        )
    print(f"{mainapp_name} created.")