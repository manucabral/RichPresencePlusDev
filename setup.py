import rpp
from cx_Freeze import setup, Executable

build_exe_options = {
    "excludes": [
        "tkinter",
        "unittest",
        "rpp.Manager",
        "rpp.Runtime",
        "rpp.Presence",
        "rpp.Browser",
    ],
    "packages": ["pypresence", "websocket", "presences"],
}

setup(
    name=rpp.__title__,
    version=rpp.__version__,
    description="A simple Discord Rich Presence manager for desktop and web apps.",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base="Console", target_name="RPPDev")],
)
