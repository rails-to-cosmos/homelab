from pathlib import Path

SYMLINK_MAP = {
    Path.home() / "sync" / "resources" / "dotfiles" / ".aws"                     : Path.home() / ".aws",
    Path.home() / "sync" / "resources" / "dotfiles" / ".ssh"                     : Path.home() / ".ssh",
    Path.home() / "sync" / "resources" / "dotfiles" / ".profile"                 : Path.home() / ".profile",
    Path.home() / "sync" / "resources" / "dotfiles" / ".xinitrc"                 : Path.home() / ".xinitrc",
    Path.home() / "sync" / "resources" / "dotfiles" / ".wakerc"                  : Path.home() / ".wakerc",
    Path.home() / "sync" / "resources" / "dotfiles" / "Alfred.alfredpreferences" : Path.home() / ".config" / "Alfred.alfredpreferences",
    Path.home() / "sync" / "resources" / "dotfiles" / ".gitconfig"               : Path.home() / ".gitconfig",
    Path.home() / "sync" / "resources" / "dotfiles" / ".xsession"                : Path.home() / ".xsession",
    Path.home() / "sync" / "resources" / "dotfiles" / ".zshrc"                   : Path.home() / ".zshrc",
    Path.home() / "sync" / "resources" / "dotfiles" / ".stack"                   : Path.home() / ".stack",
    Path.home() / "sync" / "resources" / "dotfiles" / "alacritty"                : Path.home() / ".config" / "alacritty",
    Path.home() / "sync" / "resources" / "dotfiles" / "cabal"                    : Path.home() / ".config" / "cabal",
    Path.home() / "sync" / "resources" / "dotfiles" / "htop"                     : Path.home() / ".config" / "htop",
    Path.home() / "sync" / "resources" / "dotfiles" / "karabiner"                : Path.home() / ".config" / "karabiner",
    Path.home() / "sync" / "resources" / "dotfiles" / "nix"                      : Path.home() / ".config" / "nix",
    Path.home() / "sync" / "resources" / "dotfiles" / "openemu"                  : Path.home() / "Game Library",
    Path.home() / "sync" / "resources" / "dotfiles" / "rofi"                     : Path.home() / ".config" / "rofi",
    Path.home() / "sync" / "resources" / "dotfiles" / "applications"             : Path.home() / ".local" / "share" / "applications",
    Path.home() / "sync" / "resources" / "dotfiles" / "autostart"                : Path.home() / ".config" / "autostart",
    Path.home() / "sync" / "resources" / "ice"                                   : Path.home() / ".local" / "share" / "ice",
}
