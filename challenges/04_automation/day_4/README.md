# Day 4: Real-Time System Resource Monitor

Display CPU usage, RAM usage, and disk space usage in a terminal dashboard that refreshes while the script runs.

[Automation overview](../README.md) · [Challenge index](../../README.md) · [Main project overview](../../../README.md#folder-overview)

## Setup and running

Install `psutil` with the same Python interpreter used to run the script:

```powershell
python -m pip install psutil
python "challenges/04_automation/day_4/day_4.py"
```

`psutil` is an external package for reading system and process information. The other imports, `os` and `time`, are part of Python's standard library.

Or open `day_4.py` in VS Code and press **Ctrl + S** with the existing Run on Save setup. Stop the running monitor with **Ctrl + C** before starting it again. The terminal then prints `Monitoring Stopped.....`.

If Python reports `ModuleNotFoundError: No module named 'psutil'`, run the installation command above in the terminal used for this project.

## What the dashboard shows

| Reading | Meaning |
| --- | --- |
| CPU usage | System-wide CPU utilization measured over a one-second interval. |
| RAM usage | The percentage of physical memory used, plus used and total memory in GB. |
| Disk usage | The percentage of storage space used, plus used and total space in GB, for the volume selected by `/`. |

Disk usage here means occupied storage space, rather than disk read/write activity. The script reads a single volume using `psutil.disk_usage("/")`; it does not add up all drives. On Windows, `/` resolves to the root of the current drive.

The RAM and disk values are returned in bytes. Dividing by `1e9` converts them to decimal gigabytes, and `round(..., 2)` keeps two decimal places.

## How the code works

1. `clear_screen()` runs `cls` on Windows or `clear` on other systems to refresh the terminal display.
2. `show_stats()` prints the title and requests the current measurements.
3. `psutil.cpu_percent(interval=1)` waits one second to measure CPU usage.
4. `psutil.virtual_memory()` supplies RAM statistics, including `.percent`, `.used`, and `.total`.
5. `psutil.disk_usage("/")` supplies storage statistics for the selected volume.
6. F-strings format the readings for the terminal.
7. The main `while True` loop waits another three seconds with `time.sleep(3)` before refreshing.
8. `except KeyboardInterrupt` handles **Ctrl + C** and prints the stop message.

The refresh cycle takes approximately four seconds: one second for the CPU measurement plus the three-second pause and a small amount of processing time.

## Files and current challenge coverage

The script prints live readings only. It does not create files, store measurement history, or move files from any folder. Run it from the repository root or the lesson folder.

CPU, RAM, and disk readings and the refreshing terminal dashboard are implemented. The original task also asks for warnings when CPU or RAM usage exceeds 80%; those warnings are not implemented in the current Python file. The original `DAY_4.md` is preserved.

## Documentation and package source

- [psutil documentation](https://psutil.io/): the official documentation and API reference.
- [psutil on PyPI](https://pypi.org/project/psutil/): installation and package information.
- [psutil — GitHub](https://github.com/giampaolo/psutil): the official source repository; use **Star** to support the project.
