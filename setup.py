from cx_Freeze import setup, Executable

build_exe_options = {
    "excludes": [
        "tkinter",
        "unittest",
        "rpp.Manager",
        "rpp.Runtime",
        "rpp.Presence",
    ],
    "packages": ["pypresence", "httpx_ws", "presences"],
}

setup(
    name="Rich Presence Plus",
    version="0.1",
    description="Rich Presence Plus",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base="Console", target_name="RPPDev")],
)
