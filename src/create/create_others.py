from subprocess import run
from ..configs import others_file_list


def main(project_dir='./',):
    for file_name in others_file_list:
        run(
            [
                "touch",
                f"{project_dir}/{file_name}",
            ]
        )
    
    print("other files crated.")
    