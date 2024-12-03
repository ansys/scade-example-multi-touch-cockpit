"""Sphinx documentation configuration file."""
from datetime import datetime
import pathlib
import os
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
version_file = source_dir / "../../VERSION"
with open(str(version_file), "r") as file:
    __version__ = file.read().splitlines()[0]
release = version = __version__

# Project information
project = "ansys-scade-example-multi-touch-cockpit"
copyright = f"(c) {datetime.now().year} ANSYS, Inc. All rights reserved"
author = "ANSYS, Inc."
release = version = __version__

# Select desired logo, theme, and declare the html title
html_theme = "ansys_sphinx_theme"
html_short_title = html_title = "Ansys SCADE Multi-touch Cockpit Example"

# multi-version documentation
cname = os.getenv("DOCUMENTATION_CNAME", "multi-touch-cockpit.example.scade.docs.pyansys.com")
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
    "logo": "pyansys",
}

# Sphinx extensions
extensions = [
    # "sphinx.ext.autodoc",
    # "sphinx.ext.autosummary",
    # "autoapi.extension",
    # "sphinx_autodoc_typehints",
    # "numpydoc",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_jinja",
    # "sphinx_gallery.gen_gallery",# scade-example-multi-touch-cockpit examples
]

add_module_names = False

# autoclass_content: keep default
# autodoc_class_signature: can't be used with enums
# autodoc_class_signature = 'separated'

# sphinx_gallery_conf = {
#     "examples_dirs": "../examples",   # path to your example scripts
#     "gallery_dirs": "examples",  # path where the gallery generated output will be saved
# }

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

# numpydoc configuration
numpydoc_show_class_members = False
numpydoc_xref_param_type = True

# Consider enabling numpydoc validation. See:
# https://numpydoc.readthedocs.io/en/latest/validation.html#
numpydoc_validate = True
numpydoc_validation_checks = {
    "GL06",  # Found unknown section
    "GL07",  # Sections are in the wrong order.
    # Disabled the docstring validation as most of the methods doesn't have the docstring
    # TODO: Add docstring and enable GL08 validation
    # "GL08",  # The object does not have a docstring
    "GL09",  # Deprecation warning should precede extended summary
    "GL10",  # reST directives {directives} must be followed by two colons
    "SS01",  # No summary found
    "SS02",  # Summary does not start with a capital letter
    "SS03",  # Summary does not end with a period
    "SS04",  # Summary contains heading whitespaces
    # "SS05", # Summary must start with infinitive verb, not third person
    "RT02",  # The first line of the Returns section should contain only the
    # type, unless multiple values are being returned"
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
linkcheck_ignore = [
    "https://github.com/ansys/scade-example-multi-touch-cockpit",
    "https://github.com/ansys/scade-example-multi-touch-cockpit/actions/workflows/ci_cd.yml",
    "https://pypi.org/project/ansys-scade-example-multi-touch-cockpit",
    # The link below takes a long time to check
    "https://www.ansys.com/products/embedded-software/ansys-scade-suite",
    "https://www.ansys.com/*"
]

# suppress warnings about fa-build while building the documentation-pdf
suppress_warnings = [
    "design.fa-build",
]


# additional logos for the latex coverpage
LaTeXBuilder.supported_image_types = ["image/png", "image/pdf", "image/svg+xml"]
latex_additional_files = [watermark, ansys_logo_white, ansys_logo_white_cropped]
latex_elements = {"preamble": latex.generate_preamble(html_title)}