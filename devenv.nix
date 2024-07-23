{ pkgs, lib, config, inputs, ... }:

{
  env.PROJECT_NAME = "homelab";
  env.PYTHON_VERSION = "3.12";

  env.FZF_DEFAULT_COMMAND = "fd --type f --strip-cwd-prefix";

  packages = with pkgs; [
    fzf
    fd
  ];

  scripts.init.exec = ''
    pyenv install -s $PYTHON_VERSION
    pyenv local $PYTHON_VERSION
    pyenv version
    pyenv virtualenv $PROJECT_NAME
    echo "$PROJECT_NAME" > .python-version
  '';

  scripts.install.exec = ''
    pip install --upgrade pip
    pip install poetry
    poetry install
  '';

  scripts.run-test.exec = ''
    poetry run mypy .
    poetry run pytest . $@
  '';
}
