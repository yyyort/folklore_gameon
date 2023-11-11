import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="Folklore",
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files": [
                '../audio',
                '.',
                '../graphics',
                '../folklore',
                '../map',
            ],
        }
    },
    executables=executables,
    # Set base to Win32GUI to hide the console window
    base="Win32GUI"
)
