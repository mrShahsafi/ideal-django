from subprocess import (
    run,
    PIPE,
)


def validate_version(version):
    if version == '':
        return


def validate_os():
    cmd = run(["uname"], stdout=PIPE)

    os_platform = cmd.stdout.decode(
        'utf-8'
    ).removesuffix('\n')

    return os_platform.lower()

