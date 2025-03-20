# filepath: c:\Users\sergi.bogatell\OneDrive - OPENCHIP\Desktop\doc_testRST\build.py

import os
import subprocess

def build_latexpdf():
    # Build the LaTeX files
    subprocess.run(['sphinx-build', '-b', 'latex', '.', '_build/latex'], check=True)
    
    # Change directory to _build/latex and run pdflatex
    os.chdir('_build/latex')
    subprocess.run(['pdflatex', 'YourProjectName.tex'], check=True)

if __name__ == '__main__':
    build_latexpdf()