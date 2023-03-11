from cx_Freeze import setup, Executable

# dependencies
build_exe_options = {
    "packages": ["os", "sys", "glob", "simplejson", "requests", "atexit", "PySide.QtCore", "PySide.QtGui", "PySide.QtXml"],
    "excludes": [],
    "build_exe": "build",
    "icon": "./assets/icon.png"
}

executable = [
    Executable("./main.py",
               base="Win32GUI",
               targetName="Example.exe",
               targetDir="build",
               copyDependentFiles=True)
]

setup(
    name="Telegraph uploader",
    version="0.1",
    description="Application that simplifies uploading a bunch of images to telegra.ph", # Using the word "test" makes the exe to invoke the UAC in win7. WTH?
    author="Xareyli",
    options={"build_exe": build_exe_options},
    executables=executable,
    requires=['PySide', 'cx_Freeze', 'json']
)
