# Day 1: Introduction to Python Notebooks

This is the first lesson in `05_data_science`, following [04_automation](../../04_automation/README.md).

Day 1 introduces Python notebooks with Markdown notes and two small code examples.

[Data Science overview](../README.md) · [Challenge index](../../README.md) · [Main project overview](../../../README.md#folder-overview)

## Current files

The lesson files are kept together in `challenges/05_data_science/day_1`:

| File | Purpose |
| --- | --- |
| [day_1.ipynb](day_1.ipynb) | A notebook with an introductory Markdown cell, a `print()` example, and a loop example. |
| [DAY_1.md](DAY_1.md) | A locally authored task description based on the notebook, because no original task statement was supplied. |
| [README.md](README.md) | Setup instructions, the lesson explanation, and reference links. |

The notebook is an introduction to the tools; it does not yet use a dataset or import data science packages.

## Anaconda and Jupyter

[Anaconda Distribution](https://www.anaconda.com/download) provides Python, environment/package management tools, and notebook applications such as Jupyter Notebook and JupyterLab.

[Project Jupyter](https://jupyter.org/) provides tools for interactive computing. A notebook (`.ipynb`) can contain Markdown notes, executable code cells, and saved outputs. A Python kernel is the process that executes the code cells.

Anaconda is one setup option. You can also run this notebook in VS Code with an existing Python environment and the Jupyter extension.

## Running the notebook in VS Code

1. Use the Microsoft Python and [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) extensions.
2. Open `challenges/05_data_science/day_1/day_1.ipynb` in the notebook editor.
3. Choose a Python environment using **Select Kernel** at the top right. The selected environment needs `ipykernel`; follow VS Code's installation prompt if it is missing.
4. Click inside a code cell, such as the one containing `print("hitesh")`, and press **Shift + Enter** or click its play button. Work from top to bottom. Use **Run All** at the top to execute the whole notebook.
5. Read the result directly below the code cell in the notebook. This output appears there, rather than in the terminal used for `.py` scripts.
6. Save with **Ctrl + S** to keep the notebook and its displayed outputs.

**Ctrl + S saves; Shift + Enter runs the selected cell.** The existing Run on Save configuration is for `.py` scripts. There is no `day_1.py` to launch with `python -u` in this lesson.

If using Anaconda's Jupyter Notebook or JupyterLab interface instead, open the same `.ipynb` file and run its cells there.

## If the notebook asks for ipykernel

`ipykernel` provides the Python kernel used to execute notebook cells. It is needed in the Python environment selected in the notebook, even if that environment can already run regular `.py` scripts.

If VS Code reports that running cells requires `ipykernel`, install it using the selected environment's Python:

```powershell
python -m pip install ipykernel
```

Then select the same environment with **Select Kernel** and run a cell using **Shift + Enter**. If the prompt remains after installation, close and reopen the notebook. `pip` is the installer used by the command; `ipykernel` is the package being installed.

For this project, it was installed and its imports verified in the system Python 3.15 environment. Anaconda environments have their own packages, so selecting a different environment may require installing it there too.

## Day 1 explained

The first cell is Markdown, containing a welcome heading and a place for notes. It is explanatory text rather than Python code.

The first code cell uses `print("hitesh")` and displays:

```text
hitesh
```

The second code cell loops through `range(5)`, which produces `0`, `1`, `2`, `3`, and `4`. Its f-string includes the current value of `i`:

```text
this value is 0
this value is 1
this value is 2
this value is 3
this value is 4
```

The supplied notebook already contains saved outputs. Seeing them does not mean its cells ran in the current session. Run the cells to reproduce them; notebook state belongs to the selected kernel, and restarting the kernel resets that state.

This lesson does not read or generate separate data files. Outputs appear below their cells and can be stored inside the notebook when saved.

## Task description provenance

`DAY_1.md` was authored locally from the supplied notebook at the repository owner's request. It is marked accordingly. Preserve that statement during later documentation updates, and keep explanations and progress in README files.

## Useful links for beginners

- [Download Anaconda](https://www.anaconda.com/download): the distribution introduced in this section.
- [Project Jupyter](https://jupyter.org/): the notebook tools' official website.
- [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks): opening notebooks, selecting kernels, running cells, and saving outputs.
- [Running code in Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Running%20Code.html): cell execution and kernel basics.
- [IPython Kernel documentation](https://ipykernel.readthedocs.io/en/stable/): documentation for `ipykernel`.
- [ipykernel — GitHub](https://github.com/ipython/ipykernel): the official Python kernel source repository, available to star.
