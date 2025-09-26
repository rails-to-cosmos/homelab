import os
import platform
import shutil
import subprocess
from pathlib import Path


def install_fonts_linux(path: Path):
    font_cache_dir = Path.home() / ".fonts"

    os.makedirs(font_cache_dir, exist_ok=True)

    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(".ttf") or filename.endswith(".otf"):
                font_path = os.path.join(dirpath, filename)
                print(f"Installing {font_path}")
                shutil.copy2(font_path, font_cache_dir)

    subprocess.run(["fc-cache", "-f", "-v"])


def install_fonts_mac(dir_path: Path) -> None:
    # Ensure the directory exists
    if not dir_path.is_dir():
        print(f"Directory {dir_path} does not exist.")
        return

    # Recursively iterate through all files in the directory
    for item_path in dir_path.rglob("*"):
        # If the item is a file and its suffix is ".ttf" or ".otf"
        if item_path.is_file() and item_path.suffix in [".ttf", ".otf"]:
            # Construct the target path
            target_path = Path.home() / "Library" / "Fonts" / item_path.name

            # Copy the font file to the target directory
            shutil.copy2(item_path, target_path)

            print(f"Font {item_path.name} installed successfully.")


def install_fonts(path: Path):
    match platform.system():
        case "Linux":
            install_fonts_linux(path)
        case "Darwin":
            install_fonts_mac(path)
        case system:
            print(f"Unsupported platform: {system}")
