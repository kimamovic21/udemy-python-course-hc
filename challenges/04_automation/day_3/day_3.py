import os
import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

WATCH_FOLDER = os.path.expanduser("~/Downloads")
TEMP_EXTENSIONS = {".tmp", ".crdownload", ".part", ".download"}
READY_SECONDS = 2
RETRY_SECONDS = 0.5
MAX_WAIT_SECONDS = 30

FILE_DESTS = {
    ".pdf": "PDFs",
    ".jpg": "Images",
    ".png": "Images",
}


class FileMoverHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            self.move_when_ready(event.src_path)

    def on_moved(self, event):
        if not event.is_directory:
            self.move_when_ready(event.dest_path)

    def move_when_ready(self, filepath):
        filepath = os.path.abspath(filepath)
        if os.path.normcase(os.path.dirname(filepath)) != os.path.normcase(
            os.path.abspath(WATCH_FOLDER)
        ):
            return
        ext = os.path.splitext(filepath)[1].lower()
        if ext in TEMP_EXTENSIONS:
            return

        dest_folder = FILE_DESTS.get(ext, "Others")
        full_dest = os.path.join(WATCH_FOLDER, dest_folder)
        move_to = os.path.join(full_dest, os.path.basename(filepath))
        deadline = time.monotonic() + MAX_WAIT_SECONDS
        last_signature = None
        stable_since = time.monotonic()
        last_error = None

        while time.monotonic() < deadline:
            try:
                stat = os.stat(filepath)
                signature = (stat.st_size, stat.st_mtime_ns)
                if signature != last_signature:
                    last_signature = signature
                    stable_since = time.monotonic()
                elif time.monotonic() - stable_since >= READY_SECONDS:
                    os.makedirs(full_dest, exist_ok=True)
                    stem, suffix = os.path.splitext(os.path.basename(filepath))
                    number = 1
                    while os.path.exists(move_to):
                        move_to = os.path.join(full_dest, f"{stem}_{number}{suffix}")
                        number += 1
                    # A rename stays on the same drive and does not copy a locked file.
                    os.rename(filepath, move_to)
                    print(f"Moved: {os.path.basename(filepath)} -> {move_to}")
                    return
            except FileNotFoundError:
                # A queued event can refer to a file already renamed or moved.
                return
            except PermissionError as error:
                # Chrome or another application may still have the file open.
                last_error = error
            except OSError as error:
                self.report_error(filepath, move_to, error)
                return

            time.sleep(RETRY_SECONDS)

        print(f"File not moved after {MAX_WAIT_SECONDS} seconds: {filepath}")
        if last_error is not None:
            self.report_error(filepath, move_to, last_error)
        else:
            print("The file is still changing. It has been left in place.")

    @staticmethod
    def report_error(filepath, move_to, error):
        print(
            f"Failed to move file: {filepath}\n"
            f"Destination: {move_to}\n"
            f"Error ({type(error).__name__}): {error}"
        )


if __name__ == "__main__":
    print(f"Watching folder: {WATCH_FOLDER}")
    event_handler = FileMoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path=WATCH_FOLDER, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
