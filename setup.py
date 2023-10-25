import sys
from cx_Freeze import setup, Executable

# Create an instance of Executable with your script as the target.
executables = [Executable("main.py", icon="./icon.ico")]

# Define the setup parameters.
build_options = {
    "packages": [
    "requests",
    "speech_recognition",
    "gtts",
],
    "excludes": [],
    "include_files": [],  # Add additional files or data here if needed.
}

# Use the setup function to configure your frozen application.
setup(
    name="AI Assistant",
    version="1.0",
    description="My AI Assistant",
    options={"build_exe": build_options},
    executables=executables
)
