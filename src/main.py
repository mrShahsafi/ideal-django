from subprocess import run

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

print(project_name)

run(
    [
        "django-admin",
        "startproject",
        f"{project_name}",
    ]
)

