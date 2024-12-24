from pathlib import Path

SYMLINK_MAP = {
    Path.home() / "sync" / "resources" / "config" / "alacritty"                : Path.home() / ".config" / "alacritty",
    Path.home() / "sync" / "resources" / "config" / "alfred"                  : Path.home() / ".config" / "Alfred.alfredpreferences",
    Path.home() / "sync" / "resources" / "config" / "aws"                     : Path.home() / ".aws",
    Path.home() / "sync" / "resources" / "config" / "gitconfig"               : Path.home() / ".gitconfig",
    Path.home() / "sync" / "resources" / "config" / "profile"                 : Path.home() / ".profile",
    Path.home() / "sync" / "resources" / "config" / "rofi"                    : Path.home() / ".config" / "rofi",
    Path.home() / "sync" / "resources" / "config" / "ssh" / "ab"              : Path.home() / ".ssh" / "ab",
    Path.home() / "sync" / "resources" / "config" / "ssh" / "akatovda"        : Path.home() / ".ssh" / "akatovda",
    Path.home() / "sync" / "resources" / "config" / "ssh" / "config"          : Path.home() / ".ssh" / "config",
    Path.home() / "sync" / "resources" / "config" / "wakerc"                  : Path.home() / ".wakerc",
    Path.home() / "sync" / "resources" / "config" / "xinitrc"                 : Path.home() / ".xinitrc",
    Path.home() / "sync" / "resources" / "config" / "xsession"                : Path.home() / ".xsession",
    Path.home() / "sync" / "resources" / "config" / "zshrc"                   : Path.home() / ".zshrc",
    Path.home() / "sync" / "resources" / "config" / "cabal" / "config"        : Path.home() / ".config" / "cabal" / "config",
    Path.home() / "sync" / "resources" / "config" / "htop" / "htoprc"         : Path.home() / ".config" / "htop" / "htoprc",
    Path.home() / "sync" / "resources" / "config" / "karabiner"               : Path.home() / ".config" / "karabiner",
    Path.home() / "sync" / "resources" / "config" / "nix"                     : Path.home() / ".config" / "nix",
    Path.home() / "sync" / "resources" / "config" / "openemu"                 : Path.home() / "Game Library",
    Path.home() / "sync" / "resources" / "config" / "applications"            : Path.home() / ".local" / "share" / "applications",

    Path.home() / "sync" / "resources" / "config" / "autostart"                : Path.home() / ".config" / "autostart",
    Path.home() / "sync" / "resources" / "config" / "terminator"               : Path.home() / ".config" / "terminator",
    Path.home() / "sync" / "resources" / "config" / "cinnamon"                 : Path.home() / ".config" / "cinnamon",

    Path.home() / "sync" / "resources" / "ice"                                   : Path.home() / ".local" / "share" / "ice",
    Path.home() / "sync" / "resources" / "document"                              : Path.home() / "Documents",
    Path.home() / "sync" / "resources" / "camera"                                : Path.home() / "Pictures",
    Path.home() / "sync" / "resources" / "dotfiles" / "redshift.conf"            : Path.home() / ".config" / "redshift.conf",
}
