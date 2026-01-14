"""
Setup script for the AI-Proposal Engine POC
Installs required dependencies for the POC implementation
"""

import subprocess
import sys

def install_dependencies():
    """Install required packages for the POC"""
    packages = [
        "llamaindex",
        "python-docx",
        "pymupdf",  # PyMuPDF
        "python-docx-template",
        "sentence-transformers",
        "torch",
        "numpy",
        "pandas",
        "camel-tools",  # For Arabic NLP
        "transformers",
        "arabic-reshaper",
        "python-bidi",
        "qdrant-client",
        "langchain",
        "langchain-community",
        "langgraph"
    ]
    
    for package in packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"Successfully installed {package}")
        except subprocess.CalledProcessError:
            print(f"Failed to install {package}")

if __name__ == "__main__":
    print("Setting up AI-Proposal Engine POC...")
    install_dependencies()
    print("Setup complete!")