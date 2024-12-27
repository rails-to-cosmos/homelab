#!/usr/bin/env python3

from pathlib import Path
from typing import Optional

import os
import platform
import shutil
import subprocess
import time
import fire  # type: ignore

from homelab.config import SYMLINK_MAP, FONTS_LOCATION
from homelab.logger import log


def create_symlink(source_path: Path, target_path: Path, decision: Optional[str] = None) -> str | None:
    force: bool = decision is not None

    log.info(f"Config path is: {source_path}")

    if not source_path.exists():
        log.info(f"Source {source_path} does not exist. Skipping symbolic link creation.")
        return decision

    # Check if the parent directory of the target path exists, if not create it
    if not target_path.parent.exists():
        log.info(f"Target directory {target_path.parent} does not exist. Creating it...")
        target_path.parent.mkdir(parents=True)

    if target_path.exists() or target_path.is_symlink():
        log.info(f"Target path {target_path} already exists.")

        if target_path.resolve() == source_path:
            print(f"Path {target_path} is a symbolic link to the source. Skipping symbolic link creation.")
            return decision

        if decision is None:
            print("How do you want me to resolve the conflict? (rename/delete/skip (!)) ")
            match input().lower().strip().split("!"):
                case [decision]:
                    force = False
                case [decision, _]:
                    force = True

        match decision:
            case "rename":
                new_target_path = target_path.with_name(f"{target_path.name}_bak_{int(time.time())}")
                print(f"Renaming the existing target to {new_target_path}")
                shutil.move(str(target_path), str(new_target_path))
            case "delete":
                print(f"Deleting the existing target {target_path}")
                shutil.rmtree(str(target_path)) if target_path.is_dir() else target_path.unlink()
            case "skip":
                log.info("Skipping symbolic link creation.")

    if decision != "skip":
        log.info("Creating symbolic link...")
        target_path.symlink_to(source_path)
        log.info("Symbolic link created successfully!")

    if force:
        print(f"Will use {decision} for all future conflicts.")
    else:
        decision = None

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
    match platform.system():
        case "Darwin":
            subprocess.run(["defaults", "write", "-g", "InitialKeyRepeat", "-int", "10"])
            subprocess.run(["defaults", "write", "-g", "KeyRepeat", "-int", "1"])
        case "Linux":
            subprocess.run(["xset", "r", "rate", "200", "60"])


class App:
    def init(self) -> None:
        self.create_symlinks()
        self.install_fonts()
        self.setup_key_repetition_interval()
        self.clone_views()

    def create_symlinks(self) -> None:
        decision = None
        for source, target in SYMLINK_MAP.items():
            decision = create_symlink(source, target, decision)

    def install_fonts(self, fonts_location: str | Path = FONTS_LOCATION) -> None:
        install_fonts(fonts_location)

    def setup_key_repetition_interval(self) -> None:
        setup_key_repetition_interval()

    def clone_views(self) -> None:
        subprocess.run(["git", "clone", "ssh://git-codecommit.us-east-2.amazonaws.com/v1/repos/views", os.path.expanduser("~/sync/views")])


def main() -> None:
    fire.Fire(App)


if __name__ == "__main__":
    main()
