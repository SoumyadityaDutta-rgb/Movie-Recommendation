# Movie Recommendation — README

Project overview

This repository contains a small movie recommendation project. It includes a Jupyter notebook (`Movie_recommender.ipynb`), a helper script (`movie.py`), and a dataset (`tmdb_movies_valid.csv`). The notebook demonstrates data processing and recommendation logic; `movie.py` contains supporting code used by the project.

Table of contents

- **Project:** short description and goals
- **Files:** what each file is for
- **Prerequisites:** Python and environment setup
- **Installation:** step-by-step setup commands (PowerShell)
- **Usage:** how to run the notebook and script
- **Data:** dataset location and format notes
- **Contributing:** guidelines for contributors
- **Troubleshooting:** common issues and fixes
- **License:** license applied to this repo

Files in this repo

- `Movie_recommender.ipynb`: main Jupyter notebook demonstrating the recommendation workflow.
- `movie.py`: helper script and functions used by the notebook (inspect before running to confirm behavior).
-- `tmdb_movies_valid.csv`: dataset with movie information used by the project.
-- `requirements.txt`: Python dependencies (the file was renamed from the misspelled `requiremnts.txt`).

Prerequisites

- Python 3.8+ installed and available on `PATH`.
- PowerShell (this repo assumes Windows PowerShell v5.1; commands below are for PowerShell).
- Optional: `virtualenv` or use `venv` to create an isolated environment.

Installation (PowerShell commands)

1. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Note: This repository includes a corrected `requirements.txt`. If you previously used `requiremnts.txt`, the file was renamed.

Running the project

- Open the notebook in Jupyter:

```powershell
jupyter notebook Movie_recommender.ipynb
```

- To run the helper script (Streamlit app `movie.py`):

```powershell
# Option A: Run with Streamlit (recommended for the interactive UI)
streamlit run movie.py

# Option B: Run directly with Python (only if the script is intended to run as a plain script)
python movie.py
```

movie.py notes and usage

- `movie.py` uses Streamlit and expects the files `movie_list.pkl` and `similarity.pkl` to be present in the same folder. It also attempts to fetch posters from TheMovieDB (TMDB) using an API key.
- To provide a TMDB API key temporarily in PowerShell:

```powershell
$env:TMDB_API_KEY = 'YOUR_TMDB_API_KEY'
```

- By default `movie.py` has an `API_KEY = ""` placeholder inside the `fetch_poster` function. You can either set it in the file or modify the code to read from the `TMDB_API_KEY` environment variable:

```python
import os
API_KEY = os.getenv('TMDB_API_KEY', '')
```

- Note: `movie.py` contains `time.sleep(20)` inside the recommendation loop which adds a 20-second delay per poster fetch; you may want to reduce or remove it for faster responses.

Run helper script after confirming the `.pkl` files and API key are available.

Data

- The dataset `tmdb_movies_valid.csv` contains the movie records used by the notebook. Confirm column names and encoding before processing large batches.
- If you replace or refresh the dataset, keep a backup copy and update the notebook paths accordingly.

Contributing

- Fork the repository and create a feature branch for changes.
- Open a pull request describing the change and include reproducible steps where useful.
- If you add dependencies, update `requirements.txt` and the README install instructions.

Troubleshooting

- If package install fails, ensure you have internet access and upgraded `pip`.
- If Jupyter does not open, try `python -m notebook` or `jupyter lab` if installed.
- On Windows, paths with spaces (like those in OneDrive) can cause issues. Use quoted paths if needed, e.g.: `jupyter notebook "Movie_recommender.ipynb"`.

License

This repository includes a `LICENSE` file with the MIT license. The `LICENSE` file contains placeholders which have been set to `2025` and `Your Name` — please update them to the correct year and author.

Quick helper script

If you want a small helper script to create a virtual environment and install dependencies, I previously added `run.ps1`. I have removed that file per your request. You can recreate it or use the manual commands shown earlier in the README.

Contact

If you want help improving documentation, tests, or packaging for this project, open an issue or contact the repository owner.
