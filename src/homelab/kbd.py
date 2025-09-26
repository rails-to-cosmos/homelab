import platform
import subprocess


def setup_key_repetition_interval():
    match platform.system():
        case "Darwin":
            subprocess.run(["defaults", "write", "-g", "InitialKeyRepeat", "-int", "10"])
            subprocess.run(["defaults", "write", "-g", "KeyRepeat", "-int", "1"])
        case "Linux":
            subprocess.run(["xset", "r", "rate", "200", "60"])
