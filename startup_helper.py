import os
import sys
import argparse
import winshell
from win32com.client import Dispatch

def get_startup_folder():
    return winshell.startup()

def get_script_path():
    return os.path.abspath("main.py")

def get_pythonw_path():
    python_dir=os.path.dirname(sys.executable)
    pythonw_path=os.path.join(python_dir,"pythonw.exe")
    if os.path.exists(pythonw_path):
        return pythonw_path
    return None

def create_shortcut():
    pythonw_path=get_pythonw_path()
    if not pythonw_path:
        print("Error: pythonw.exe not found in your Python installation")
        return False
    script_path=get_script_path()
    if not os.path.exists(script_path):
        print(f"Error: main.py not found at {script_path}")
        return False
    startup_folder=get_startup_folder()
    shortcut_path=os.path.join(startup_folder,"CC-WSL-Image-Paste.lnk")
    if os.path.exists(shortcut_path):
        print("Shortcut already exists in startup folder")
        return False
    shell=Dispatch('WScript.Shell')
    shortcut=shell.CreateShortCut(shortcut_path)
    shortcut.TargetPath=pythonw_path
    shortcut.Arguments=f'"{script_path}"'
    shortcut.WorkingDirectory=os.path.dirname(script_path)
    shortcut.IconLocation=pythonw_path
    shortcut.save()
    print(f"Successfully added to startup: {shortcut_path}")
    return True

def remove_shortcut():
    startup_folder=get_startup_folder()
    shortcut_path=os.path.join(startup_folder,"CC-WSL-Image-Paste.lnk")
    if not os.path.exists(shortcut_path):
        print("Shortcut not found in startup folder")
        return False
    os.remove(shortcut_path)
    print(f"Successfully removed from startup: {shortcut_path}")
    return True

def check_status():
    startup_folder=get_startup_folder()
    shortcut_path=os.path.join(startup_folder,"CC-WSL-Image-Paste.lnk")
    if os.path.exists(shortcut_path):
        print("Status: Enabled (will run on startup)")
        print(f"Shortcut location: {shortcut_path}")
    else:
        print("Status: Disabled (not in startup)")

def main():
    parser=argparse.ArgumentParser(description="Manage CC-WSL-Image-Paste Windows startup")
    subparsers=parser.add_subparsers(dest="command",help="Available commands")
    subparsers.add_parser("add",help="Add CC-WSL-Image-Paste to Windows startup")
    subparsers.add_parser("remove",help="Remove CC-WSL-Image-Paste from Windows startup")
    subparsers.add_parser("status",help="Check if CC-WSL-Image-Paste is in startup")
    args=parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)
    if args.command=="add":
        create_shortcut()
    elif args.command=="remove":
        remove_shortcut()
    elif args.command=="status":
        check_status()

if __name__=="__main__":
    main()
