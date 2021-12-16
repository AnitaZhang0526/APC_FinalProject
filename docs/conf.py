# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../Code'))


# -- Project information -----------------------------------------------------

project = 'XRD/FTIR Analysis Tool Suite'
copyright = '2021, Shashank Gupta, Jordan Hamel, Alex Pirola, Arjun Prihar, Agnes Robang, Anita Zhang'
author = 'Shashank Gupta, Jordan Hamel, Alex Pirola, Arjun Prihar, Agnes Robang, Anita Zhang'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# extensions
extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages']

# teamplate paths
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Turn off prepending module names
add_module_names = False
# Sort members by type
autodoc_member_order = 'groupwise'
# Document __init__, __repr__, and __str__ methods
def skip(app, what, name, obj, would_skip, options):
    if name in ("__init__", "__repr__", "__str__"):
        return False
    return would_skip
def setup(app):
    app.connect("autodoc-skip-member", skip)

# -- Options for HTML output -------------------------------------------------
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'
master_doc = 'index'

# -- Extension configuration -------------------------------------------------
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

#-- Options for PFD LaTex output -------------------------------------------------
latex_engine = 'pdflatex'
latex_elements = {
    'papersize': 'a4paper',
    'releasename':"Shashank Gupta, Jordan Hamel, Alex Pirola, Arjun Prihar, Agnes Robang, Anita Zhang",
    'fontpkg': '\\usepackage{amsmath,amsfonts,amssymb,amsthm}',
    'figure_align':'htbp',
    'pointsize': '10pt',
    'sphinxsetup': \
        'hmargin={0.7in,0.7in}, \
        vmargin={1in,1in}, \
        verbatimwithframe=true, \
        TitleColor={rgb}{0,0,0}, \
        HeaderFamily=\\rmfamily\\bfseries'}
