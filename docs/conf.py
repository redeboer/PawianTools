"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

import os
import shutil
import subprocess


# -- Copy example notebooks ---------------------------------------------------
print("Copy example notebook and data files")
PATH_SOURCE = "../examples"
PATH_TARGET = "usage"
FILES_TO_COPY = [
    "ASCII_Data.ipynb",
    "QA_Histograms.ipynb",
]
shutil.rmtree(PATH_TARGET, ignore_errors=True)
os.makedirs(PATH_TARGET, exist_ok=True)
for file_to_copy in FILES_TO_COPY:
    path_from = os.path.join(PATH_SOURCE, file_to_copy)
    path_to = os.path.join(PATH_TARGET, file_to_copy)
    print("  copy", path_from, "to", path_to)
    shutil.copyfile(path_from, path_to, follow_symlinks=True)

# -- Generate API skeleton ----------------------------------------------------
shutil.rmtree("api", ignore_errors=True)
subprocess.call(
    "sphinx-apidoc "
    "--force "
    "--no-toc "
    "--templatedir _templates "
    "--separate "
    "-o api/ ../src/; ",
    shell=True,
)


# -- Project information -----------------------------------------------------
project = "pyPawianTools"
copyright = "2020, RUB EP1"
author = "Meike Küßner, Remco de Boer"


# -- Include constructors ----------------------------------------------------
def skip(app, what, name, obj, would_skip, options):
    if name == "__init__":
        return False
    return would_skip


def setup(app):
    app.connect("autodoc-skip-member", skip)


# -- General configuration ---------------------------------------------------
source_suffix = [
    ".rst",
    ".ipynb",
    ".md",
]

# The master toctree document.
master_doc = "index"

extensions = [
    "nbsphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.ifconfig",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
]
exclude_patterns = [
    "**.ipynb_checkpoints",
    "*build",
    "README.md",
    "tests",
]

# General sphinx settings
add_module_names = False
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
    "special-members": "__call__, __eq__",
}
html_copy_source = False  # do not copy rst files
html_show_copyright = False
html_show_sourcelink = False
html_show_sphinx = False
html_theme = "sphinx_rtd_theme"
pygments_style = "sphinx"
todo_include_todos = False
viewcode_follow_imported_members = True

# Cross-referencing configuration
default_role = "py:obj"
primary_domain = "py"
nitpicky = True  # warn if cross-references are missing
nitpick_ignore: list = []

# Intersphinx settings
intersphinx_mapping = {
    "matplotlib": ("https://matplotlib.org/", None),
    "numpy": ("https://docs.scipy.org/doc/numpy/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
    "python": ("https://docs.python.org/3", None),
}

# Settings for autosectionlabel
autosectionlabel_prefix_document = True

# Settings for linkcheck
linkcheck_anchors = False
linkcheck_ignore = [
    "https://gitlab.ep1.rub.de/redeboer/pyPawianTools/badges/master/coverage.svg",
    "https://gitlab.ep1.rub.de/redeboer/pyPawianTools/badges/master/pipeline.svg",
    "https://gitlab.ep1.rub.de/redeboer/pyPawianTools/pipelines",
]

# Settings for nbsphinx
if "NBSPHINX_EXECUTE" in os.environ:
    print("\033[93;1mWill run Jupyter notebooks!\033[0m")
    nbsphinx_execute = "always"
else:
    nbsphinx_execute = "never"
nbsphinx_timeout = -1
nbsphinx_execute_arguments = [
    "--InlineBackend.figure_formats={'svg', 'pdf'}",
    "--InlineBackend.rc={'figure.dpi': 96}",
]
