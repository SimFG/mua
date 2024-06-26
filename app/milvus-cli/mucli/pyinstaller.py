from pathlib import Path

import PyInstaller.__main__

HERE = Path(__file__).parent.absolute()
path_to_main = str(HERE / "main.py")


def install():
    PyInstaller.__main__.run(
        [
            path_to_main,
            # '--onefile',
            "-D",
            "--windowed",
            "--noupx",
            "-nmucli",  # output name
            # other pyinstaller options...
        ]
    )
