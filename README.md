# CC-WSL-Image-Paste

A Windows utility that automatically converts Windows screenshot paths to WSL paths and pastes them using a hotkey (Alt+V). Perfect for quickly sharing screenshots with Claude Code running in WSL.

## Features

- Monitors Windows Screenshots folder
- Converts Windows paths to WSL format for Claude Code compatibility
- Global hotkey (Alt+V) to paste latest screenshot path
- Runs silently in background with `pythonw.exe`
- Easy startup management

## Requirements

- Windows 10/11
- WSL (Windows Subsystem for Linux)
- Python 3.7+

## Installing Python on Windows

1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. **Important:** Check "Add Python to PATH" during installation
4. Verify installation by opening Command Prompt and typing:
   ```
   python --version
   ```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Parham125/CC-WSL-Image-Paste.git
   cd CC-WSL-Image-Paste
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running Manually

To run the application:
```bash
python main.py
```

To run in background (no console window):
```bash
pythonw main.py
```

### Managing Windows Startup

Use the `startup_helper.py` script to automatically run CC-WSL-Image-Paste on Windows startup.

#### Add to Startup

```bash
python startup_helper.py add
```

This creates a shortcut in your Windows startup folder that runs the script silently using `pythonw.exe`.

#### Remove from Startup

```bash
python startup_helper.py remove
```

#### Check Startup Status

```bash
python startup_helper.py status
```

### Using the Hotkey

Once running:
1. Take a screenshot using Windows (Win+Shift+S or Win+PrtScn)
2. Press **Alt+V** to paste the WSL path of the latest screenshot
3. The path will be automatically typed where your cursor is

Example pasted path:
```
/mnt/c/Users/YourUsername/Pictures/Screenshots/Screenshot_2025-10-08.png
```

### Use Case: Claude Code Screenshots

This tool is particularly useful when working with Claude Code in WSL. When you want to share a screenshot with Claude Code:
1. Take a Windows screenshot (Win+Shift+S)
2. In your WSL terminal running Claude Code, press **Alt+V**
3. The WSL-formatted path is instantly pasted, ready for Claude Code to read the image

## How It Works

1. Monitors your Windows Screenshots folder (`C:\Users\{username}\Pictures\Screenshots`)
2. When you press Alt+V, it finds the most recently created screenshot
3. Converts the Windows path to WSL format (`C:\` → `/mnt/c/`)
4. Pastes the path at your cursor position

## Troubleshooting

### Screenshots folder not found
Make sure you have a Screenshots folder at `C:\Users\{YourUsername}\Pictures\Screenshots`. Take at least one screenshot using Windows Snipping Tool or Win+Shift+S to create it.

### Hotkey not working
- Make sure the application is running (check Task Manager for `pythonw.exe`)
- Try running `python main.py` (with console) to see error messages
- Restart the application

### Python not found
- Reinstall Python and make sure "Add Python to PATH" is checked
- Restart your terminal/command prompt after installation

### Startup shortcut issues
- Run Command Prompt or PowerShell as Administrator
- Make sure you're in the project directory when running `startup_helper.py`
- Check that `main.py` exists in the same folder
