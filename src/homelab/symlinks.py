import shutil
import time
from pathlib import Path
from typing import Optional

UserDecision = str | None


def create_symlink(source_path: Path, target_path: Path, decision: Optional[str] = None) -> UserDecision:
    force: bool = decision is not None

    print(f"Config path is: {source_path}")

    if not source_path.exists():
        print(f"Source {source_path} does not exist. Skipping symbolic link creation.")
        return decision
    elif not target_path.parent.exists():
        print(f"Target directory {target_path.parent} does not exist. Creating it...")
        target_path.parent.mkdir(parents=True)
    elif target_path.exists() or target_path.is_symlink():
        print(f"Target path {target_path} already exists.")

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
                print("Skipping symbolic link creation.")

        if decision != "skip":
            print("Creating symbolic link...")
            target_path.symlink_to(source_path)
            print("Symbolic link created successfully!")
    else:
        print("Creating symbolic link...")
        target_path.symlink_to(source_path)
        print("Symbolic link created successfully!")

    if force:
        print(f"Will use {decision} for all future conflicts.")
    else:  # Reset decision
        decision = None

    return decision
