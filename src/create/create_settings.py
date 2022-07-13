from subprocess import run
from ..configs import (
    settings_list,
    init_content,
    dev_content,
    prod_content,
    drf_content,
    local_content,
)


def main(project_dir, project_name):
    
    setting_dir = f"{project_dir}/{project_name}/settings"
    setting_pure_file = f"{project_dir}/{project_name}/settings.py"

    run(
        [
            "mkdir",
            setting_dir,
        ]
    )
    
    for file_name in settings_list:
        run(
            [
                "touch",
                f"{setting_dir}/{file_name}",
            ]
        )
    
    run(
        [
            "mv",
            setting_pure_file,
            f"{setting_dir}/base.py",
        ]
    )

    with open(f"{setting_dir}/__init__.py", 'w+') as outfile:
        outfile.write(
            init_content
        )
    
    if 'dev.py' in settings_list:
        with open(f"{setting_dir}/dev.py", 'w+') as outfile:
            outfile.write(
                dev_content
            )

    if 'prod.py' in settings_list:
        with open(f"{setting_dir}/prod.py", 'w+') as outfile:
            outfile.write(
                prod_content
            )

    if 'drf_setting.py' in settings_list:
        with open(f"{setting_dir}/drf_setting.py", 'w+') as outfile:
            outfile.write(
                drf_content
            )
    if 'local.py.conf' in settings_list:
        with open(f"{setting_dir}/local.py.conf", 'w+') as outfile:
            outfile.write(
                local_content,
            )

    print("modular settings crated.")