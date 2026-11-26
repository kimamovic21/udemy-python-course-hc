# The Ultimate Python Bootcamp

## Learn by Building 50 Projects

My Python learning repository, starting with the basics and adding exercises as I follow the course.

- [Udemy course](https://www.udemy.com/course/100-days-of-python)
- [ChaiCode](https://chaicode.com/) — the instructor's website and learning platform.
- [Course diagrams](https://app.eraser.io/workspace/xltiZYV3fLYZuUEtfUal)

## Folder overview

| Folder | What I practise |
| --- | --- |
| [01_starter](01_starter/README.md) | My first Python program: displaying text with `print()` and exploring The Zen of Python with `import this`. |
| [02_datatypes](02_datatypes/README.md) | Python data types and collections, dates and time zones, named tuples, and six coding exercises. Section in progress. |
| [03_conditionals](03_conditionals/README.md) | Conditional logic with nested `if` statements, conditional expressions, and `match`/`case`, practised in six mini projects and exercises 07–12. Section in progress. |
| [04_loops](04_loops/README.md) | `for` and `while` loops, loop control, the walrus operator (`:=`), and dictionary-based discount calculations. Exercises 13–18; section in progress. |
| [05_functions](05_functions/README.md) | Functions, scope, flexible arguments, recursion, lambdas, docstrings, and `help()`. Exercises 19–22; section in progress. |
| [06_chai_business](06_chai_business/README.md) | Organising code into modules and packages, importing functions, and understanding Python's `__pycache__`. Section in progress. |
| [07_comprehensions](07_comprehensions/README.md) | List, set, and dictionary comprehensions, generator expressions, and inventory filtering (exercise 23). Section completed. |
| [08_generators](08_generators/README.md) | Generator functions with `yield`, `next()`, `.send()`, `yield from`, and `.close()`, plus a token dispenser (exercise 24). Section in progress. |
| [09_decorators](09_decorators/README.md) | Wrapping functions with decorators, preserving metadata, logging, role checks, and caching results (exercise 25). Section in progress. |
| [10_oop](10_oop/README.md) | Classes, objects, attributes, inheritance, composition, MRO, instance, static, and class methods, and properties with validation. Exercises 26–27: a device tracker and vehicle rental system; section in progress. |
| [11_exceptions](11_exceptions/README.md) | Built-in and custom exceptions, tracebacks, input validation, chai billing, and file handling with `try`, `except`, `else`, `finally`, and `raise`. Section in progress. |
| [challenges](challenges/README.md) | Projects covering utilities, data handling, web scraping, automation, data science, and Flask web apps. Currently working on `06_url_shortener`, Udemy section 16, days 46–52, as one application. The challenge index lists groups, projects, and progress. |

Start with **01_starter**, the first folder in this project. Detailed explanations, running instructions, and expected output are documented in the corresponding lesson, project, or challenge-group README files. New folders will be added to this overview as the course progresses.

After **11_exceptions**, work through all the groups in the [challenge index](challenges/README.md#challenge-groups) before continuing to the next numbered section (`12_...`). Follow the documented learning order even if your editor sorts the folders differently.

## Video-only topic: Virtual environments (`venv`)

`venv` creates an isolated Python environment for a project, allowing its packages and versions to be managed separately from other projects. This course topic contains one video with no downloadable exercise files.

## Supporting files

- [`.vscode/settings.json`](.vscode/settings.json) — project editor settings for Python, Black formatting, and automatic execution after **Ctrl + S**, using the Python available in the terminal.
- [`.vscode/tasks.json`](.vscode/tasks.json) — the shared Streamlit task started when Data Science Day 4, Day 7, or Day 10 is saved.
- [`documentation.txt`](documentation.txt) — tutorial video names, maintained manually to keep track of my course progress.
- `challenges/**/DAY_*.md` — challenge statements, maintained manually. Course wording is preserved where supplied; web scraping Day 10 and Data Science Days 1–10 have marked, locally authored descriptions. Project explanations and progress are recorded in the corresponding README files.

## Quick start

Open the project root in VS Code with [Python 3](https://www.python.org/) and these extensions installed: [Python by Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-python.python), [Run on Save by pucelle](https://marketplace.visualstudio.com/items?itemName=pucelle.run-on-save), and [Black Formatter by Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter). Select your Python interpreter, edit a Python file, and save with **Ctrl + S** to format and run it in the terminal. Use **Shift + Alt + F** to format a file manually.

Run on Save launches the saved file with `python -u`, using the Python available in its terminal. For interactive scripts, click inside that terminal and submit each answer with **Enter**.

The Streamlit scripts in [Data Science Day 4](challenges/05_data_science/day_4/README.md), [Day 7](challenges/05_data_science/day_7/README.md), and [Day 10](challenges/05_data_science/day_10/README.md) use a shared task on **Ctrl + S**. Its first save starts the currently open app, and later saves reuse that task while Streamlit handles code changes. Open the Local URL printed in the task terminal. Stop the running app with **Ctrl + C** before opening and saving another Streamlit lesson.

The [URL Shortener](challenges/06_url_shortener/README.md) uses Flask and runs with ordinary Python execution. Install Flask in the selected environment, start `challenges/06_url_shortener/app.py`, and open `http://localhost:8000/`. Its guide explains setup, the local SQLite database, and the planned single commit for days 46–52.

The notebook lessons in [05_data_science](challenges/05_data_science/README.md) use `.ipynb` files. Open them in a notebook editor, select a Python kernel, and run cells with **Shift + Enter** or **Run All**. **Ctrl + S** saves the notebook. See the group guide for the Anaconda/Jupyter and VS Code setup options.

See [01_starter: first-time setup](01_starter/README.md#first-time-setup) for step-by-step instructions.

## Package source repositories

These third-party packages are directly imported by the Python examples. Follow the GitHub links and use **Star** to support their projects. Source links were checked against package metadata and upstream project pages; the repositories hosted elsewhere are labeled explicitly.

| Package | Import used in this repository | Project source |
| --- | --- | --- |
| Arrow | `arrow` | [GitHub](https://github.com/arrow-py/arrow) |
| Requests | `requests` | [GitHub](https://github.com/psf/requests) |
| python-dotenv | `dotenv` | [GitHub](https://github.com/theskumar/python-dotenv) |
| Matplotlib | `matplotlib.pyplot` | [GitHub](https://github.com/matplotlib/matplotlib) |
| cryptography | `cryptography.fernet` | [GitHub](https://github.com/pyca/cryptography) |
| Beautiful Soup | `bs4` | [Launchpad](https://code.launchpad.net/beautifulsoup) |
| Pillow | `PIL` | [GitHub](https://github.com/python-pillow/Pillow) |
| wget | `wget` | [PyPI and source archive](https://pypi.org/project/wget/) |
| schedule | `schedule` | [GitHub](https://github.com/dbader/schedule) |
| PyMuPDF | `pymupdf` | [GitHub](https://github.com/pymupdf/PyMuPDF) |
| Watchdog | `watchdog.events`, `watchdog.observers` | [GitHub](https://github.com/gorakhargosh/watchdog) |
| psutil | `psutil` | [GitHub](https://github.com/giampaolo/psutil) |
| NumPy | `numpy` | [GitHub](https://github.com/numpy/numpy) |
| pandas | `pandas` | [GitHub](https://github.com/pandas-dev/pandas) |
| scikit-learn | `sklearn.linear_model`, `sklearn.pipeline`, `sklearn.feature_extraction.text`, `sklearn.model_selection`, `sklearn.metrics.pairwise` | [GitHub](https://github.com/scikit-learn/scikit-learn) |
| Streamlit | `streamlit` | [GitHub](https://github.com/streamlit/streamlit) |
| Flask | `flask` | [GitHub](https://github.com/pallets/flask) |

Flask support packages: the [URL Shortener package guide](challenges/06_url_shortener/README.md#flask-packages-and-their-sources) links the official documentation and GitHub repositories for Flask, Werkzeug, Jinja2, MarkupSafe, Click, ItsDangerous, and Blinker. The supporting packages are framework dependencies rather than direct imports in the lesson code.

Notebook support: [ipykernel — GitHub](https://github.com/ipython/ipykernel) provides the Python kernel used to execute notebook cells. Install it in the selected notebook environment with `python -m pip install ipykernel` if needed; see the [Day 1 setup note](challenges/05_data_science/day_1/README.md#if-the-notebook-asks-for-ipykernel) and [official documentation](https://ipykernel.readthedocs.io/en/stable/). This is a notebook runtime dependency rather than an import in the lesson code.

Beautiful Soup's [official project page](https://www.crummy.com/software/BeautifulSoup/) links to Launchpad rather than GitHub. For `wget`, PyPI metadata still lists an unavailable Bitbucket homepage; the PyPI page provides the source archive, and no official GitHub repository was confirmed. These entries do not point to unofficial GitHub mirrors.

Modules such as `csv`, `json`, `pathlib`, `datetime`, `sqlite3`, `functools`, and `textwrap` belong to Python's standard library. Their Python implementation and bindings are in [CPython on GitHub](https://github.com/python/cpython); they are not additional pip dependencies. Local modules such as `recipes.flavors` are part of this repository.

Day 9 imports `schedule` without using it to schedule jobs; Day 8 uses it actively. Package links are also listed in the relevant lesson and challenge-group READMEs.

## Useful links for beginners

- [Visual Studio Marketplace](https://marketplace.visualstudio.com/) — find extensions for VS Code.
- [Python for Beginners](https://www.python.org/about/gettingstarted/) — an official starting point for learning Python.
- [Python variables](https://www.w3schools.com/python/python_variables.asp) — simple examples of creating variables and assigning values.
- [Python data types](https://www.w3schools.com/python/python_datatypes.asp) — an introduction to types such as `str`, `int`, `float`, and `bool`.
- [Python classes and objects](https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes) — official examples of classes, instances, methods, and class versus instance variables; use this section as a reference alongside the OOP lessons.
- [Python self parameter](https://www.w3schools.com/python/python_class_self.asp) — short examples showing how an instance method accesses its object's attributes through `self`.
- [Python __init__ method](https://www.w3schools.com/python/python_class_init.asp) — examples of giving each object its own initial values when it is created.
- [Python errors and exceptions](https://docs.python.org/3/tutorial/errors.html) — official examples of reading tracebacks, handling specific exceptions, raising errors, and defining custom exceptions.
- [Reading and writing files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) — an introduction to file modes, writing text, and closing files with `with` or `close()`.
- [Python virtual environments (`venv`)](https://docs.python.org/3/tutorial/venv.html) — an official introduction to creating and activating project environments and managing their packages.
- [Watchdog quickstart](https://python-watchdog.readthedocs.io/en/stable/quickstart.html) — observers and event handlers for monitoring folders, as used in Automation Day 3.
- [psutil documentation](https://psutil.io/) — system resource statistics used for the CPU, RAM, and disk dashboard in Automation Day 4.
- [Download Anaconda](https://www.anaconda.com/download) — Python distribution and notebook tools introduced in the data science section.
- [Project Jupyter](https://jupyter.org/) — tools for interactive notebooks containing notes, code, and outputs.
- [NumPy](https://numpy.org/) — numerical arrays and calculations used in Data Science Day 2.
- [pandas](https://pandas.pydata.org/) — tables and CSV export used in Data Science Day 2.
- [scikit-learn documentation](https://scikit-learn.org/stable/) — the library used for salary regression, comment classification, and book-description similarity in the data science section.
- [Streamlit](https://streamlit.io/) — the Python framework used for the salary predictor, comment classifier, and book recommendation apps in Data Science Days 4, 7, and 10.
- [Flask documentation](https://flask.palletsprojects.com/en/stable/) — routes, templates, and web app setup for the URL Shortener in section 16, days 46–52.
- [Flask hosting options](challenges/06_url_shortener/README.md#optional-hosting-references) — Render, PythonAnywhere, and Vercel references for sharing the app later, with a note about database storage.
- [Streamlit Community Cloud](https://docs.streamlit.io/deploy/streamlit-community-cloud) — hosting and sharing Streamlit apps from GitHub repositories.
- [Kaggle Datasets](https://www.kaggle.com/datasets) — datasets for future practice; the [official Kaggle CLI source](https://github.com/Kaggle/kaggle-cli) is also available on GitHub. Current lessons do not require this tool.
- [Python Playground](https://python-playground.com/) — a place to try small Python examples in the browser.
- [PEP 8: Style Guide for Python Code](https://peps.python.org/pep-0008/#introduction) — a reference for naming and formatting code; consult it gradually as you practise.
