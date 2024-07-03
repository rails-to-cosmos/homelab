#!/usr/bin/env python3

from pathlib import Path
from typing import Optional

import os
import platform
import shutil
import subprocess
import time

from homelab.config import SYMLINK_MAP, FONTS_LOCATION
from homelab.logger import log


def create_symlink(source_path: Path, target_path: Path, decision: Optional[str] = None) -> str | None:
    log.info(f"Config path is: {source_path}")

    if not source_path.exists():
        log.info(f"Source {source_path} does not exist. Skipping symbolic link creation.")
        return decision

    # Check if the parent directory of the target path exists, if not create it
    if not target_path.parent.exists():
        log.info(f"Target directory {target_path.parent} does not exist. Creating it...")
        target_path.parent.mkdir(parents=True)

    if target_path.exists() or target_path.is_symlink():
        if target_path.resolve() == source_path:
            log.info(f"Path {target_path} is a symbolic link to the source. Skipping symbolic link creation.")
            return decision
        else:
            log.info(f"Target path {target_path} already exists.")
            if decision is None:
                log.info("Do you want to rename it or delete it? (rename/delete/skip) ")
                answer = input().lower()
                if answer.startswith("r"):
                    new_target_path = target_path.with_name(f"{target_path.name}_bak_{int(time.time())}")
                    log.info(f"Renaming the existing target to {new_target_path}")
                    shutil.move(str(target_path), str(new_target_path))
                    decision = "r"
                elif answer.startswith("d"):
                    log.info(f"Deleting the existing target {target_path}")
                    if target_path.is_dir():
                        shutil.rmtree(str(target_path))
                    else:
                        target_path.unlink()
                    decision = "d"
                elif answer.startswith("s"):
                    log.info("Skipping symbolic link creation.")
                    return "s"
                else:
                    log.info("Invalid answer. Please answer rename, delete or skip.")
                    return decision

                log.info("Do you want to apply this action to all future conflicts? (yes/no) ")
                answer = input().lower()
                if answer.startswith("y"):
                    log.info(f"Will use {decision} for all future conflicts.")
                else:
                    decision = None
            else:
                if decision == "r":
                    new_target_path = target_path.with_name(f"{target_path.name}_bak_{int(time.time())}")
                    log.info(f"Renaming the existing target to {new_target_path}")
                    shutil.move(str(target_path), str(new_target_path))
                elif decision == "d":
                    log.info(f"Deleting the existing target {target_path}")
                    if target_path.is_dir():
                        shutil.rmtree(str(target_path))
                    else:
                        target_path.unlink()

    log.info("Creating symbolic link...")
    target_path.symlink_to(source_path)
    log.info("Symbolic link created successfully!")
    return decision


def install_fonts_linux(font_dir):
    home = os.path.expanduser("~")
    font_cache_dir = os.path.join(home, ".fonts")

    # Ensure the font cache directory exists
    os.makedirs(font_cache_dir, exist_ok=True)

    # Walk through the directory structure
    for dirpath, dirnames, filenames in os.walk(font_dir):
        for filename in filenames:
            if filename.endswith(".ttf") or filename.endswith(".otf"):
                font_path = os.path.join(dirpath, filename)
                log.info(f"Installing {font_path}")
                shutil.copy2(font_path, font_cache_dir)

    # Rebuild the font cache
    subprocess.run(["fc-cache", "-f", "-v"])


def install_fonts_mac(dir_path: Path) -> None:
    # Ensure the directory exists
    if not dir_path.is_dir():
        log.info(f"Directory {dir_path} does not exist.")
        return

    # Recursively iterate through all files in the directory
    for item_path in dir_path.rglob("*"):
        # If the item is a file and its suffix is ".ttf" or ".otf"
        if item_path.is_file() and item_path.suffix in [".ttf", ".otf"]:
            # Construct the target path
            target_path = Path.home() / "Library" / "Fonts" / item_path.name

            # Copy the font file to the target directory
            shutil.copy2(item_path, target_path)

            log.info(f"Font {item_path.name} installed successfully.")


def install_fonts(dir_path):
    match platform.system():
        case "Linux":
            install_fonts_linux(dir_path)
        case "Darwin":
            install_fonts_mac(Path(dir_path))
        case system:
            log.info(f"Unsupported platform: {system}")


def setup_key_repetition_interval():
    # Check if the current system is macOS
    match platform.system():
        case "Darwin":
            subprocess.run(["defaults", "write", "-g", "InitialKeyRepeat", "-int", "10"])
            subprocess.run(["defaults", "write", "-g", "KeyRepeat", "-int", "1"])
        case "Linux":
            subprocess.run(["xset", "r", "rate", "200", "60"])


def main() -> None:
    decision = None
    for source, target in SYMLINK_MAP.items():
        decision = create_symlink(source, target, decision)

    install_fonts(FONTS_LOCATION)
    setup_key_repetition_interval()


if __name__ == "__main__":
    main()
