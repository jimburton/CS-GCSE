import sys
import os
import subprocess

def check_environment():
    print("-" * 30)
    print("PYTHON INTERPRETER DIAGNOSTICS")
    print("-" * 30)
    
    # 1. Show exactly which executable IDLE is using
    print(f"1. IDLE is using this Python executable:\n   {sys.executable}\n")
    
    # 2. Show where it looks for packages (The Path)
    print(f"2. IDLE is looking for packages in these folders:")
    for path in sys.path:
        if path:
            print(f"   - {path}")
            
    # 3. Check if Flask is reachable from here
    print("\n3. Flask Status:")
    try:
        import flask
        print(f"   [SUCCESS] Flask is installed at: {flask.__file__}")
    except ImportError:
        print("   [ERROR] Flask is NOT installed for this specific Python version.")
        
    print("\n" + "-" * 30)
    print("HOW TO FIX THIS:")
    print("-" * 30)
    print(f"Copy and paste the following line into your Terminal or Command Prompt:")
    print(f'"{sys.executable}" -m pip install flask')
    print("-" * 30)

if __name__ == "__main__":
    check_environment()