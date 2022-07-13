from subprocess import run
from ..configs import gitignore_content


def main(project_dir='./',):
    gitignore_dir = f"{project_dir}/.gitignore"
    run(
        [
            "touch",
            gitignore_dir
        ]
    )
    with open(gitignore_dir, 'w+') as outfile:
        outfile.write(
            gitignore_content,
        )
    print(".gitignore crated.")