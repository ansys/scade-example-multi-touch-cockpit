"""Sphinx documentation configuration file."""

from datetime import datetime
import os
import pathlib

from ansys_sphinx_theme import (
    ansys_favicon,
    ansys_logo_white,
    ansys_logo_white_cropped,
    get_version_match,
    latex,
    watermark,
)
from sphinx.builders.latex import LaTeXBuilder


source_dir = pathlib.Path(__file__).parent.resolve().absolute()
version_file = source_dir.parent.parent / "VERSION"
if not version_file.exists():
    raise FileNotFoundError(f"Could not find VERSION file in {version_file}")
__version__ = version_file.read_text(encoding="utf-8")

# Project information
project = "ansys-scade-example-multi-touch-cockpit"
copyright = f"(c) {datetime.now().year} ANSYS, Inc. All rights reserved"
author = "ANSYS, Inc."
release = version = __version__

# Select desired logo, theme, and declare the html title
html_theme = "ansys_sphinx_theme"
html_short_title = html_title = "Ansys SCADE Multi-touch Cockpit Example"

# multi-version documentation
cname = os.getenv(
    "DOCUMENTATION_CNAME", "multi-touch-cockpit.example.scade.docs.pyansys.com"
)
"""The canonical name of the webpage hosting the documentation."""

# specify the location of your github repo
html_theme_options = {
    "github_url": "https://github.com/ansys/scade-example-multi-touch-cockpit",
    "show_prev_next": False,
    "show_breadcrumbs": True,
    "additional_breadcrumbs": [
        ("SCADE Examples", "https://examples.scade.docs.pyansys.com/"),
    ],
    "switcher": {
        "json_url": f"https://{cname}/versions.json",
        "version_match": get_version_match(version),
    },
    "check_switcher": False,
    "logo": "ansys",
}

# Sphinx extensions
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_jinja",
]

add_module_names = False

# Intersphinx mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/3.11", None),
    # kept here as an example
    # "scipy": ("https://docs.scipy.org/doc/scipy/reference", None),
    # "numpy": ("https://numpy.org/devdocs", None),
    # "matplotlib": ("https://matplotlib.org/stable", None),
    # "pandas": ("https://pandas.pydata.org/pandas-docs/stable", None),
    # "pyvista": ("https://docs.pyvista.org/", None),
    # "grpc": ("https://grpc.github.io/grpc/python/", None),
}

# Favicon
html_favicon = ansys_favicon

# static path
html_static_path = ["_static"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"


# TODO: remove ignore links after public release
# https://github.com/ansys/scade-example-multi-touch-cockpit/issues/15
linkcheck_ignore = [
    "https://github.com/ansys/scade-example-multi-touch-cockpit",
    "https://github.com/ansys/scade-example-multi-touch-cockpit/actions/workflows/ci_cd.yml",
    "https://pypi.org/project/ansys-scade-example-multi-touch-cockpit",
    # The link below takes a long time to check
    "https://www.ansys.com/products/embedded-software/ansys-scade-suite",
    "https://www.ansys.com/*",
]

# suppress warnings about fa-build while building the documentation-pdf
suppress_warnings = [
    "design.fa-build",
]


# additional logos for the latex coverpage
LaTeXBuilder.supported_image_types = ["image/png", "image/pdf", "image/svg+xml"]
latex_additional_files = [watermark, ansys_logo_white, ansys_logo_white_cropped]
latex_elements = {"preamble": latex.generate_preamble(html_title)}
