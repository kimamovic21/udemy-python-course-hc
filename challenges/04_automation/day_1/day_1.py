import os
import shutil

EXTENSION_MAP = {
    "PDFs": [".pdf"],
    "Images": [".png", ".jpeg", ".jpg"],
    "TextFiles": [".txt"],
}


def get_destination_folder(filename):
    ext = os.path.splitext(filename)[1].lower()
    for folder, extensions in EXTENSION_MAP.items():
        if ext in extensions:
            return folder
    return "Others"


def sort_files(folder_path):
    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)

        if file in {os.path.basename(__file__), "DAY_1.md", "README.md"}:
            continue

        if os.path.isfile(full_path):
            dest_folder = get_destination_folder(file)
            dest_path = os.path.join(folder_path, dest_folder)

            os.makedirs(dest_path, exist_ok=True)

            # move the file
            shutil.move(full_path, os.path.join(dest_path, file))
            print(f"Moved : {file} -> {dest_folder}/")


if __name__ == "__main__":
    folder = os.path.dirname(os.path.abspath(__file__))
    sort_files(folder)
    print("✅ sorting completed")
