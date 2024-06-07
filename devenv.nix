{ pkgs, ... }:

{
  env.LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [pkgs.stdenv.cc.cc.lib];

  packages = with pkgs; [
    python312Full
    python312Packages.virtualenv
    python312Packages.pandas

    fzf
    fd
    zlib
    stdenv.cc.cc
  ];

  enterShell = ''
    export FZF_DEFAULT_COMMAND='fd --type f --strip-cwd-prefix'
    source $DEVENV_ROOT/.venv/bin/activate
  '';

  enterTest = ''
    mypy src
  '';

  scripts.init.exec = ''
    virtualenv .venv
    pip install poetry
    poetry install --with dev
  '';
}
