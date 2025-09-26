import os
import argparse
import stat


def set_file_permissions(target_path: str) -> None:
    """
    Recursively sets file permissions to 400 for all files in a directory,
    skipping any files that end with a .pub extension.

    Args:
        target_path (str): The path to the directory to process.
    """
    # 1. Validate the input path
    if not os.path.isdir(target_path):
        print(f"❌ Error: The path '{target_path}' is not a valid directory.")
        return

    print(f"🔍 Processing directory: {os.path.abspath(target_path)}\n")

    # The file mode 400 (read-only by owner)
    # S_IREAD is the constant for owner read permission.
    read_only_mode: int = stat.S_IREAD  # This is equivalent to octal 0o400

    # 2. Walk through the directory tree
    for root, _, files in os.walk(target_path):
        for filename in files:
            # Construct the full path to the file
            full_path: str = os.path.join(root, filename)

            # 3. Check for the .pub exception
            if filename.endswith(".pub"):
                print(f"⏭️  Skipping: {full_path}")
                continue

            # 4. Change the file mode for all other files
            try:
                os.chmod(full_path, read_only_mode)
                print(f"✅ Set mode 400 for: {full_path}")
            except OSError as e:
                print(f"❌ Error setting permissions for {full_path}: {e}")
