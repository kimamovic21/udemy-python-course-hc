import os


def batch_rename(folder, base_name, extension):
    if (
        not base_name
        or not extension
        or any(char in base_name + extension for char in "/\\:")
    ):
        print("Enter a base name and extension without folder paths")
        return

    protected_files = {os.path.basename(__file__), "DAY_2.md", "README.md"}
    files = [
        f
        for f in os.listdir(folder)
        if f not in protected_files
        and os.path.isfile(os.path.join(folder, f))
        and f.lower().endswith(extension.lower())
    ]
    files.sort()  # Sort filenames alphabetically before numbering them.

    if not files:
        print("NO files found in dir")
        return

    for i, file in enumerate(files, start=1):
        new_name = f"{base_name}_{i}{extension}"
        if new_name != file and os.path.exists(os.path.join(folder, new_name)):
            print(f"Cannot rename: {new_name} already exists")
            return

    for i, file in enumerate(files, start=1):
        new_name = f"{base_name}_{i}{extension}"
        print(f"{file} => {new_name}")
    confirm = input("Press (y) to confirm or (n) to reject: ").strip().lower()

    if confirm != "y":
        print("Cancel")
        return

    for i, file in enumerate(files, start=1):
        src = os.path.join(folder, file)
        new_name = f"{base_name}_{i}{extension}"
        dest = os.path.join(folder, new_name)
        os.rename(src, dest)
    print(f"Renamed {len(files)} files successfully")


if __name__ == "__main__":
    folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
    base_name = input("Enter base name for files: ").strip()
    extension = input("Enter extension name for files: ").strip()

    batch_rename(folder, base_name, extension)
