#!/usr/bin/env -S uv run --script
# /// script
# dependencies = ["homelab"]
#
# [tool.uv.sources]
# homelab = { path = "." }
# ///

import subprocess

import fire  # type: ignore

from homelab import Config, Logger
from homelab.fonts import install_fonts
from homelab.kbd import setup_key_repetition_interval
from homelab.symlinks import create_symlink

PROJECT_NAME = "homelab"


class App:
    def _cfg(self) -> Config:
        return Config.from_yaml("config.yaml")

    def all(self) -> None:
        self.symlinks()
        self.fonts()
        self.kbd()
        self.views()

    def symlinks(self) -> None:
        cfg = self._cfg()
        logger = Logger(PROJECT_NAME, cfg.log_level, cfg.log_format)

        decision = None
        for source, target in cfg.symlinks.items():
            decision = create_symlink(source, target, decision)

    def fonts(self) -> None:
        cfg = self._cfg()
        for font_location in cfg.font_locations:
            install_fonts(font_location)

    def kbd(self) -> None:
        setup_key_repetition_interval()

    def views(self) -> None:
        cfg = self._cfg()
        subprocess.run(["git", "clone", cfg.views.remote, str(cfg.views.local.expanduser())])


def main() -> None:
    fire.Fire(App)


if __name__ == "__main__":
    main()
