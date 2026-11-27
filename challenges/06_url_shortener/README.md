# URL Shortener with Flask

This project corresponds to **Udemy section 16, days 46–52**. It follows [05_data_science](../05_data_science/README.md) and is kept as one application in `06_url_shortener`, rather than separate daily folders. The repository owner plans one commit for the whole project when it is ready.

**Status: tutorial project documented.** The course continues with [Threads and Concurrency](../../12_threads_concurrency/README.md), Udemy section 17.

[Challenge index](../README.md) · [Main project overview](../../README.md#folder-overview)

## What the app does

Enter a long URL to create a six-character short code. The home page lists saved URLs, their short codes, and visit counts. Following a short link redirects to the original address and increments its counter. A Delete button removes the saved entry. An unknown code displays a 404 page.

Use a complete address such as `https://example.com/python`. The current tutorial app does not validate URL schemes or retry a randomly generated code if it collides with an existing one.

## Files and source

```text
06_url_shortener/
├── app.py
├── models.py
├── requirements.txt
├── README.md
├── database.db          # created automatically when the app starts
└── templates/
    ├── index.html
    └── 404.html
```

- `app.py` creates the Flask app, defines routes, generates short codes, and starts the server.
- `models.py` handles SQLite table creation, inserts, lookups, visit counts, and deletion.
- `templates/index.html` is the HTML/Jinja page containing the form and results table. It loads Tailwind CSS from a CDN for styling.
- `templates/404.html` is the page for missing short codes.
- `requirements.txt` preserves the package versions supplied with the tutorial.

The files were copied from the instructor's [06_url_shortner source folder](https://github.com/hiteshchoudhary/python-udemy/tree/main/challenges/06_url_shortner). The local folder uses the spelling `06_url_shortener`. The source's `.DS_Store`, `__pycache__`, and existing database were not needed; the app creates its own database.

## Install Flask

Use the same Python environment for package installation, VS Code, and running the script. From the repository root:

```powershell
python -m pip install Flask
python -c "from flask import Flask; print('Flask import works')"
```

This installs Flask and resolves its dependencies. The local fix was verified with Python 3.15 and Flask 3.1.3. `requirements.txt` remains the instructor's original pinned snapshot, including Flask 3.1.1; it is not a lock file for the current local environment. The installation above is the procedure verified here and does not force older dependency versions onto the existing course environment.

If Pylance still shows `Import "flask" could not be resolved`, run **Python: Select Interpreter** and select the environment where Flask was installed. Compare it with the path printed by `python -c "import sys; print(sys.executable)"` in the terminal. Use **Developer: Reload Window** if the warning remains after selecting the correct interpreter.

`random`, `string`, `sqlite3`, and `pathlib` are part of Python's standard library and need no separate installation.

## Run the app

From the repository root:

```powershell
python "challenges/06_url_shortener/app.py"
```

With the existing Run on Save configuration, opening `app.py` and pressing **Ctrl + S** also starts it through the regular Python terminal command. This Flask app does not use the Data Science Streamlit task.

Open **http://localhost:8000/** in the browser. Keep the terminal running and stop it with **Ctrl + C** when finished. If an earlier instance is still running, stop it before starting another copy. The tutorial starts Flask in debug mode on port `8000` and binds to `0.0.0.0`; use `localhost` to open it on this computer.

Try the following:

1. Submit `https://example.com/python` in the form.
2. Follow the generated short link.
3. Refresh the home page to see the increased visit count.
4. Delete the entry and check that it disappears.

The supplied HTML currently displays `http://localhost:5000/` as its short-link text, while `app.py` runs on port `8000`. Its actual `href` is relative, so clicking the link from the app uses the correct current port. When manually typing a short URL, use `http://localhost:8000/<short_code>`.

## Routes and database

| Route | Method | Purpose |
| --- | --- | --- |
| `/` | GET | Display the form and saved URLs. |
| `/` | POST | Save a new short code, then redirect to the home page. |
| `/<short_code>` | GET | Count the visit and redirect, or display a 404 page. |
| `/delete/<short_code>` | POST | Remove a saved URL and return to the home page. |
| `/about` | GET | Display the tutorial's sample text response. |

`init_db()` runs when the app module is imported and creates the `urls` table if needed. Its fields are `id`, `original_url`, `short_code`, and `visit_count`. The short code has a uniqueness constraint, and SQL values are passed through placeholders.

The local adjustment in `models.py` uses `Path(__file__).resolve().parent / "database.db"`. This keeps the database inside `06_url_shortener` even when the app is launched from the repository root. Saved links remain available after restarting the app.

This project's generated `database.db` is ignored by Git. After cloning, running the app creates a new empty database automatically. Saved URLs and visit counts stay local; they are not included in commits. The ignore rule applies only to `challenges/06_url_shortener/database.db`, not to databases in other projects.

## Flask compared with Streamlit

The earlier Streamlit lessons build their interface with calls such as `st.text_input()` and `st.table()`. Here, Flask handles HTTP requests and renders the HTML/Jinja templates in `templates/`. Python functions handle the routes, while HTML describes the browser form and table.

## Optional hosting references

These references are for sharing the app with others later. The project currently documents local execution; no hosted deployment has been configured.

- [Deploy Flask on Render](https://render.com/docs/deploy-flask): connect a GitHub repository, deploy the application, and automatically deploy later pushes to the linked branch.
- [Flask on PythonAnywhere](https://help.pythonanywhere.com/pages/Flask/): upload an existing Flask application and configure its Python environment and WSGI entry point.
- [Flask on Vercel](https://vercel.com/docs/frameworks/backend/flask): Vercel also supports Flask applications.

Plan database storage before publishing this SQLite-based app. For example, Render's default filesystem loses local file changes across restarts and deployments; its [persistent disk guide](https://render.com/docs/disks) explains durable storage and mount paths. The current `database.db` path is set up for local use, so deployment may need a storage-path adjustment or a hosted database. Ignoring the database in Git does not provide persistent hosting storage.

## Flask packages and their sources

The tutorial's `requirements.txt` lists Flask and six supporting packages. The application imports Flask directly; its dependencies provide the other framework features below. Installing Flask normally installs its required dependencies automatically, so these links are learning references rather than seven separate installation steps.

| Package | Role | Official website and documentation | GitHub repository |
| --- | --- | --- | --- |
| Flask | Web application framework: routes, requests, redirects, and template rendering. | [Flask documentation](https://flask.palletsprojects.com/en/stable/) | [pallets/flask](https://github.com/pallets/flask) |
| Werkzeug | HTTP and WSGI utilities used by Flask, including request/response handling and the development server. | [Werkzeug documentation](https://werkzeug.palletsprojects.com/en/stable/) | [pallets/werkzeug](https://github.com/pallets/werkzeug) |
| Jinja2 | Template engine that renders the HTML pages and their dynamic values. | [Jinja documentation](https://jinja.palletsprojects.com/en/stable/) | [pallets/jinja](https://github.com/pallets/jinja) |
| MarkupSafe | HTML escaping and safe-markup support used by Jinja. | [MarkupSafe documentation](https://markupsafe.palletsprojects.com/en/stable/) | [pallets/markupsafe](https://github.com/pallets/markupsafe) |
| Click | Command-line tools, including Flask's CLI commands. | [Click documentation](https://click.palletsprojects.com/en/stable/) | [pallets/click](https://github.com/pallets/click) |
| ItsDangerous | Data signing, used by Flask for features such as signed session cookies. Signing does not encrypt the contents. | [ItsDangerous documentation](https://itsdangerous.palletsprojects.com/en/stable/) | [pallets/itsdangerous](https://github.com/pallets/itsdangerous) |
| Blinker | Signals that let application components subscribe to events. | [Blinker documentation](https://blinker.readthedocs.io/en/stable/) | [pallets-eco/blinker](https://github.com/pallets-eco/blinker) |

The current URL Shortener does not explicitly use session cookies or register signal handlers. These packages are included through Flask's dependency chain, even when a small app does not use every feature. Use **Star** on the GitHub repositories to support their projects.

## Other useful links

- [Flask installation](https://flask.palletsprojects.com/en/stable/installation/): Python environments and installation instructions.
- [Original course project](https://github.com/hiteshchoudhary/python-udemy/tree/main/challenges/06_url_shortner): instructor's files used as the starting point.
