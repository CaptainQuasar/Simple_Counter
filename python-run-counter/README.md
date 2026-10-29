# Python Overlay Run Counter

A lightweight, frameless, semi-transparent overlay counter built with Python and Tkinter. It is designed to sit above games or applications running in borderless windowed mode.

## Features

- Always on top
- Borderless and translucent
- Draggable by clicking and dragging the background or title
- Left-click the number to increment
- Right-click the number to decrement (not below zero)
- Reset button to start over

## Requirements

- Python 3
- Tkinter (included with most standard Python installations)

## Run

From a terminal in this folder:

```powershell
python counter.py
```

On Windows, you can also double-click `run.bat`.

## Publish to GitHub

1. Create a new, empty repository on GitHub. Do not initialize it with a README, license, or `.gitignore`.
2. Open PowerShell in this folder and run:

   ```powershell
   git init
   git add counter.py run.bat .gitignore README.md
   git commit -m "Initial commit: Python overlay run counter"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/python-run-counter.git
   git push -u origin main
   ```

Replace `YOUR_USERNAME` with your GitHub username. Git must be installed, and you must have permission to push to the repository.
