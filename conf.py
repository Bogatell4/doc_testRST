# Configuration file for the Sphinx documentation builder.


import sys
import os

# -- Project information -----------------------------------------------------

project = 'TFM Thesis documentation'
author = 'Sergi Bogatell'
release = '0.1'
version = '0.1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.imgconverter',
]


templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
numfig = True
html_theme = 'alabaster'
html_static_path = ['_static']

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'figure_align': 'htbp',
}

latex_documents = [
    ('index', 'YourProjectName.tex', 'Your Project Name Documentation',
     'Sergi Bogatell', 'manual'),
]