"""
Script to run the AI-Proposal Engine POC
This will execute the main demonstration
"""

import subprocess
import sys
import os
from pathlib import Path

def run_poc():
    """
    Run the POC demonstration
    """
    print("Starting AI-Proposal Engine POC...")
    print()

    # Change to the poc_implementation directory
    poc_dir = Path(__file__).parent / "poc_implementation"
    os.chdir(poc_dir)

    # Run the main demo
    try:
        # First run the test to verify components
        print("Testing POC components...")
        result = subprocess.run([sys.executable, "test_poc.py"], capture_output=True, text=True)

        if result.returncode == 0:
            print("All POC components are working correctly!")
            print(result.stdout)
        else:
            print("POC component test failed:")
            print(result.stderr)
            return False

        print("\n" + "="*60)
        print("RUNNING POC DEMONSTRATION")
        print("="*60)

        # Now run the main demonstration
        result = subprocess.run([sys.executable, "main.py"], capture_output=True, text=True)

        if result.returncode == 0:
            print("POC demonstration completed successfully!")
            print(result.stdout)
        else:
            print("POC demonstration failed:")
            print(result.stderr)
            return False

        return True

    except Exception as e:
        print(f"Error running POC: {e}")
        import traceback
        traceback.print_exc()
        return False

def install_dependencies():
    """
    Install required dependencies for the POC
    """
    print("Installing required dependencies...")

    try:
        # Use the requirements file
        result = subprocess.run([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ], capture_output=True, text=True, cwd=Path(__file__).parent / "poc_implementation")

        if result.returncode == 0:
            print("Dependencies installed successfully!")
            return True
        else:
            print("Dependency installation failed:")
            print(result.stderr)
            print("\nTrying to install key packages individually...")

            # Try installing key packages individually
            packages = ["llamaindex", "python-docx", "pymupdf", "docxtpl"]
            for pkg in packages:
                try:
                    subprocess.run([sys.executable, "-m", "pip", "install", pkg], check=True)
                    print(f"Installed {pkg}")
                except subprocess.CalledProcessError:
                    print(f"Could not install {pkg}")

            return True  # Continue even if some packages fail

    except Exception as e:
        print(f"Error installing dependencies: {e}")
        return False

def main():
    """
    Main function to run the complete POC
    """
    print("AI-Proposal Engine POC Setup and Execution")
    print("="*50)

    # Install dependencies
    deps_ok = install_dependencies()
    if not deps_ok:
        print("Could not install dependencies. POC may not work properly.")
        # Continue anyway since some packages might have installed

    # Run the POC
    poc_success = run_poc()

    print("\n" + "="*50)
    if poc_success:
        print("AI-Proposal Engine POC completed successfully!")
        print("\nNext Steps:")
        print("   1. Add your engineering documents to ./data/input/")
        print("   2. Customize the proposal template in ./templates/")
        print("   3. Modify the proposal_engine_poc.py with your specific requirements")
        print("   4. Run the full implementation with real data")
    else:
        print("AI-Proposal Engine POC encountered errors.")
        print("   Check the error messages above and try again.")

    print("="*50)

if __name__ == "__main__":
    main()