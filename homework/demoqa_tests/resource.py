from pathlib import Path

from homework import tests


def path(file_name):
    return str(
        Path(tests.__file__).parent.joinpath(f'resources/{file_name}').absolute()
    )