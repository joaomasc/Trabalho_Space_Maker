#pip install cx_freeze
import cx_Freeze

executables = [
    cx_Freeze.Executable(script="main.py", icon="icone.ico")
]

cx_Freeze.setup(
    name="Space Maker",
    options={
        "build_exe": {
            "packages": ["pygame", "tkinter"],
            "include_files": [
                "art.jpg",
                "telescopio.jpg",
                "SPACE.jpg",
                "stws.mp3"
            ]
        }
    },
    executables=executables
)

#py geraSetup.py build
#py geraSetup.py bdist_msi