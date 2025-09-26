from pathlib import Path
from typing import Self

import attrs
import yaml


def ExpandedPath(path: Path | str) -> Path:
    return Path(path).expanduser()


@attrs.define(frozen=True, kw_only=True)
class RepositoryConfig:
    remote: str
    local: Path


@attrs.define(frozen=True, kw_only=True)
class Config:
    log_level: str
    log_format: str
    font_locations: list[Path]
    symlinks: dict[Path, Path]
    views: RepositoryConfig

    @classmethod
    def from_yaml(cls, path: Path) -> Self:
        with open(path, "r") as f:
            data = yaml.safe_load(f)

        match data:
            case {"log": {"level": log_level, "format": log_format},
                  "font_locations": [*font_locations],
                  "symlinks": symlinks,
                  "views": {
                      "remote": views_remote,
                      "local": views_local,
                  }}:
                return cls(log_level=log_level,
                           log_format=log_format,
                           font_locations=list(map(ExpandedPath, font_locations)),
                           symlinks={ExpandedPath(k): ExpandedPath(v) for k, v in symlinks.items()},
                           views=RepositoryConfig(remote=views_remote, local=ExpandedPath(views_local)))
            case _:
                raise ValueError("Unexpected config format")
