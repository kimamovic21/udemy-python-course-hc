# Day 3: Auto File Organizer with Watchdog

Monitor the user's Downloads folder and organize newly created or renamed files into subfolders. This project uses filesystem events instead of manually scanning a folder once.

[Automation overview](../README.md) · [Challenge index](../../README.md) · [Main project overview](../../../README.md#folder-overview)

## Setup and running

Install the package with the same Python interpreter used to run the script:

```powershell
python -m pip install watchdog
python "challenges/04_automation/day_3/day_3.py"
```

`os` and `time` are part of Python's standard library.

## Watchdog in this project

`watchdog` is an external Python package for receiving filesystem change events. It detects changes; our handler decides which files to skip, waits for them to be ready, and moves them with `os.rename()`.

| Component | Role in this script |
| --- | --- |
| `Observer` | Monitors the selected folder and dispatches events to the handler. |
| `FileSystemEventHandler` | Base class extended by `FileMoverHandler` to define our reactions. |
| `on_created(event)` | Handles a newly created file using `event.src_path`. |
| `on_moved(event)` | Handles a moved or renamed file using its new `event.dest_path`. |
| `event.is_directory` | Allows folder events to be skipped. |
| `recursive=False` | Limits monitoring to Downloads itself, excluding nested folders. |
| `observer.stop()` and `observer.join()` | Stop monitoring and wait for the observer thread to finish. |

The two-second stability check and permission retries are implemented by our script; Watchdog events alone do not mean a browser download is complete.

## Watched folder and stopping the script

The script prints the watched path, normally `C:\Users\<username>\Downloads` on Windows. It watches only files directly in that folder. Existing files are not scanned at startup, and nested folders are not watched. Unlike Days 1–2, this lesson deliberately works in Downloads rather than its project directory.

Keep the process running while downloading a new file. Stop it with **Ctrl + C**. Before running an edited version, stop the previous instance in every terminal so multiple organizers do not compete for the same files.

## File destinations

| Extension | Destination inside Downloads |
| --- | --- |
| `.pdf` | `PDFs/` |
| `.jpg`, `.png` | `Images/` |
| Other completed-file extensions | `Others/` |
| `.tmp`, `.crdownload`, `.part`, `.download` | Skipped and left in place |

Output folders are created when a file is ready to move. A successful move prints its destination. If that name already exists, a numbered suffix is added instead of replacing the existing file.

## Why the original failed during Chrome downloads

The original `on_created()` handler immediately moved any new file, including temporary download files. A `.tmp` file therefore went into `Others` while Chrome still needed it, which could interrupt the download. A queued event could also refer to a path that Chrome had already renamed, producing `FileNotFoundError`.

The working version:

- Ignores common temporary download extensions.
- Handles both `on_created` and `on_moved`, using the destination path after a rename.
- Waits until size and modification time stay unchanged for two seconds.
- Retries permission errors while another application holds the file open, for up to 30 seconds in total.
- Uses `os.rename()` for moves within Downloads, avoiding a copy-and-delete fallback when a file is locked.
- Ignores stale events whose source no longer exists and reports other filesystem errors with both paths and the exception details.
- Sleeps in the main loop instead of using a busy `while True: pass` loop.

File stability is a practical check, not a browser completion signal. A download written directly to a final filename can pause for more than two seconds. If a file keeps changing or remains locked beyond the timeout, the script leaves it in place and prints a message; it does not keep retrying in the background indefinitely. While waiting for one file, later events remain queued.

## Current challenge coverage

Folder monitoring, extension-based destinations, and automatic movement are implemented. The task statement also mentions an `Archives` folder for ZIP files; this mapping is not implemented, so ZIP files currently go into `Others`. The original `DAY_3.md` remains unchanged.

## Documentation and package source

- [Watchdog documentation](https://python-watchdog.readthedocs.io/en/stable/): the official documentation.
- [Watchdog quickstart](https://python-watchdog.readthedocs.io/en/stable/quickstart.html): an introduction to observers, handlers, and monitoring folders.
- [Watchdog API reference](https://python-watchdog.readthedocs.io/en/stable/api.html): event and observer APIs.
- [Watchdog on PyPI](https://pypi.org/project/watchdog/): installation and package information.
- [Watchdog — GitHub](https://github.com/gorakhargosh/watchdog): the official source repository; use **Star** to support the project.

## Original tutorial code — reference only

This is the original version before the local troubleshooting changes, including the original generic error message. It is preserved for comparison; the working Python file includes the download-handling changes described above.

```python
import os
import shutil
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

WATCH_FOLDER = os.path.expanduser("~/Downloads")

FILE_DESTS = {
    ".pdf": "PDFs",
    ".jpg": "Images",
    ".png": "Images",
}


class FileMoverHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        filepath = event.src_path
        ext = os.path.splitext(filepath)[1].lower()

        dest_folder = FILE_DESTS.get(ext, "Others")
        full_dest = os.path.join(WATCH_FOLDER, dest_folder)
        os.makedirs(full_dest, exist_ok=True)
        move_to = os.path.join(full_dest, os.path.basename(filepath))
        try:
            shutil.move(filepath, move_to)
            # print message
        except:
            print("Failed to move")


if __name__ == "__main__":
    print(f"Watching folder: {WATCH_FOLDER}")
    event_handler = FileMoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path=WATCH_FOLDER, recursive=False)
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
```
