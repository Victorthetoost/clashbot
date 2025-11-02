# Recreating the Python virtual environment

Recommended workflow for sharing the project's Python environment via Git:

1. Don't commit the full virtual environment folder. It's large and platform-specific. Instead:
   - Add the venv folder (e.g., `.venv/`) to `.gitignore` (already done).
   - Commit `requirements.txt` which lists exact dependencies.

2. To create the environment locally (Windows PowerShell):

   Open PowerShell in the project root and run:

   . .\\setup_env.ps1

   Or manually:

   python -m venv .venv
   . .\\.venv\\Scripts\\Activate.ps1
   pip install -r requirements.txt

Optional: If you must provide an entire venv (not recommended):
 - Zip the `.venv` folder and add the zip to the repo or release. This increases repo size and may not work across OSes.
