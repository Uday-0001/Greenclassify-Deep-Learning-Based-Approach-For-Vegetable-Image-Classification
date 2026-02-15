# Setting Up Python 3.10 for TensorFlow

## Step 1: Download and Install Python 3.10

1. Go to: https://www.python.org/downloads/
2. Scroll down and find **Python 3.10.x** (latest 3.10 version)
3. Download the Windows installer
4. **IMPORTANT**: During installation, check "Add Python 3.10 to PATH"
5. Complete the installation

## Step 2: Create Virtual Environment with Python 3.10

After installing Python 3.10, open a **NEW** Command Prompt or PowerShell and run:

```powershell
cd C:\Users\amdga\Desktop\deeplearning\FLASK

# Remove old virtual environment
Remove-Item -Recurse -Force .venv

# Create new venv with Python 3.10 (adjust path if needed)
py -3.10 -m venv .venv

# Activate it
.venv\Scripts\Activate.ps1

# Install dependencies
pip install flask tensorflow numpy pillow

# Run the app
python app.py
```

## Step 3: Alternative - Use uv with Python 3.10

If you prefer using `uv`:

```powershell
# Delete old environment
Remove-Item -Recurse -Force .venv

# Create with Python 3.10
uv venv --python 3.10

# Activate
.venv\Scripts\Activate.ps1

# Install
uv pip install -r requirements.txt

# Run
python app.py
```

## Troubleshooting

- If `py -3.10` doesn't work, try `python3.10` or find the full path to Python 3.10
- You can check installed Python versions with: `py --list`
