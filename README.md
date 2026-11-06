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
| [challenges](challenges/README.md) | Daily projects applying the previous sections, organised by day range. The challenge index lists groups, projects, and progress. In progress. |

Start with **01_starter**, the first folder in this project. Detailed explanations, running instructions, and expected output are documented in the corresponding lesson or challenge-group README files. New folders will be added to this overview as the course progresses.

After **11_exceptions**, work through all the groups in the [challenge index](challenges/README.md#challenge-groups) before continuing to the next numbered section (`12_...`). Follow the documented learning order even if your editor sorts the folders differently.

## Video-only topic: Virtual environments (`venv`)

`venv` creates an isolated Python environment for a project, allowing its packages and versions to be managed separately from other projects. This course topic contains one video with no downloadable exercise files.

## Supporting files

- [`.vscode/settings.json`](.vscode/settings.json) — project editor settings for Python, Black formatting, and automatic execution after **Ctrl + S**, using the Python available in the terminal.
- [`documentation.txt`](documentation.txt) — tutorial video names, maintained manually to keep track of my course progress.
- `challenges/**/DAY_*.md` — original challenge statements, maintained manually. Project explanations and progress are recorded in the corresponding README files.

## Quick start

Open the project root in VS Code with [Python 3](https://www.python.org/) and these extensions installed: [Python by Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-python.python), [Run on Save by pucelle](https://marketplace.visualstudio.com/items?itemName=pucelle.run-on-save), and [Black Formatter by Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter). Select your Python interpreter, edit a Python file, and save with **Ctrl + S** to format and run it in the terminal. Use **Shift + Alt + F** to format a file manually.

Run on Save launches the saved file with `python -u`, using the Python available in its terminal. For interactive scripts, click inside that terminal and submit each answer with **Enter**.

See [01_starter: first-time setup](01_starter/README.md#first-time-setup) for step-by-step instructions.

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
- [Python Playground](https://python-playground.com/) — a place to try small Python examples in the browser.
- [PEP 8: Style Guide for Python Code](https://peps.python.org/pep-0008/#introduction) — a reference for naming and formatting code; consult it gradually as you practise.
