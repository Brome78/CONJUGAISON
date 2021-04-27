
from cx_Freeze import setup, Executable
base = None
executables = [Executable("CONJUGAISONV1.py", base=base)]

packages = ["tkinter"]
options = {
    'build_exe': {    
        'packages':packages,
    },
}
setup(
    name = "Conjugaison V1",
    options = options,
    version = "1.0",
    description = 'Programme de conjugaison',
    executables = executables
)