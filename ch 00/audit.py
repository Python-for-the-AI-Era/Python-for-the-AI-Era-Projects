import sys
import platform
import subprocess
import argparse
from datetime import datetime
import importlib.util
import importlib.metadata

# --- UTILS & CONSTANTS ---
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def get_env_info():
    """
    TODO: Return a dictionary containing:
    - python_version, executable, is_venv, os_info
    """
    pass

def check_package(package_name, required_version):
    """
    TODO: Use importlib to check if package exists and compare versions.
    Return status: "OK", "MISSING", or "OUTDATED"
    """
    pass

def run_audit(fix=False):
    """
    Main logic to read requirements.txt, run checks, 
    print the table, and save to file.
    """
    print(f"\nPython Environment Report  [{datetime.now().strftime('%Y-%m-%d %H:%M')}]")
    print("─" * 48)
    
    # 1. Get and print System Info
    # 2. Parse requirements.txt
    # 3. Loop through and check packages
    # 4. Print Table (Standard Library formatting)
    # 5. Handle --fix (subprocess.run)
    # 6. Write to environment_report.txt
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python Environment Auditor")
    parser.add_argument("--fix", action="store_true", help="Install missing packages")
    parser.add_argument("--check-python", action="store_true", help="Verify Python version >= 3.11")
    
    args = parser.parse_args()
    run_audit(fix=args.fix)