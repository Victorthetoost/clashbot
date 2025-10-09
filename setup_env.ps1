# PowerShell helper to create and activate a Python venv and install dependencies.
# Usage (in project root):
#   .\setup_env.ps1
#
# This will:
#   - create a .venv folder using the current Python executable
#   - activate the venv for the current session
#   - install packages from requirements.txt if present

Write-Host "Creating virtual environment in .venv..."
python -m venv .venv

Write-Host "Activating .venv..."
. .\.venv\Scripts\Activate.ps1

if (Test-Path requirements.txt) {
    Write-Host "Installing from requirements.txt..."
    pip install -r requirements.txt
} else {
    Write-Host "No requirements.txt found. Activate .venv with: . .\\.venv\\Scripts\\Activate.ps1"
}