# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from datetime import datetime
import warnings

import numpy as np
import networkx as nx
import sphinx_gallery  # noqa: F401
from sphinx_gallery.sorting import ExampleTitleSortKey, ExplicitOrder

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

sys.path.insert(0, os.path.abspath("../"))

import pywhy_graphs  # noqa: E402

curdir = os.path.dirname(__file__)
sys.path.append(os.path.abspath(os.path.join(curdir, "..")))
sys.path.append(os.path.abspath(os.path.join(curdir, "..", "pywhy_graphs")))

# -- Project information -----------------------------------------------------

project = "pywhy-graphs"
copyright = f"{datetime.today().year}, Adam Li"
author = "Adam Li"
version = pywhy_graphs.__version__

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = "5.0"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx_issues",
    "sphinx.ext.viewcode",
    # "nbsphinx",  # enables building Jupyter notebooks and rendering
    "sphinx.ext.mathjax",
    "sphinx_gallery.gen_gallery",
    "sphinxcontrib.bibtex",
    "sphinx_copybutton",
    # 'sphinx.ext.napoleon',
    "numpydoc",
    # "IPython.sphinxext.ipython_console_highlighting",
]

# configure sphinx-copybutton
copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_prompt_is_regexp = True

# -- Warnings management -----------------------------------------------------
def setup(app):
    # Ignore .ipynb files
    app.registry.source_suffix.pop(".ipynb", None)

warnings.filterwarnings(
    "ignore", category=UserWarning
)

# generate autosummary even if no references
# -- sphinx.ext.autosummary
autosummary_generate = True
autodoc_default_options = {
    "inherited-members": False,
    "private-members": False,
}
autodoc_inherit_docstrings = False
# autodoc_typehints = "signature"

# -- numpydoc
# Below is needed to prevent errors
numpydoc_xref_param_type = False
numpydoc_show_inherited_class_members = False
numpydoc_show_class_members = False
numpydoc_class_members_toctree = False
numpydoc_attributes_as_param_list = True
numpydoc_use_blockquotes = True
numpydoc_validate = False

numpydoc_xref_ignore = {
    # words
    "instance",
    "instances",
    "of",
    "default",
    "shape",
    "or",
    "with",
    "length",
    "pair",
    "matplotlib",
    "optional",
    "kwargs",
    "in",
    "dtype",
    "object",
    "self.verbose",
    "py",
    "the",
    "functions",
    "lambda",
    "container",
    "iterator",
    "keyword",
    "arguments",
    "no",
    "attributes",
    "dictionary",
    "pywhy_nx.MixedEdgeGraph",
    # pywhy-graphs
    "causal",
    "Node",
    "circular",
    "endpoint",
    "TsNode",
    "tsdict",
    "TimeSeriesGraph",
    "TimeSeriesDiGraph",
    # networkx
    "node",
    "nodes",
    "graph",
    "directed",
    "bidirected",
    "undirected",
    "single",
    "G.name",
    "n in G",
    "nx.MixedEdgeGraph",
    "MixedEdgeGraph",
    "collection",
    "u",
    "v",
    "EdgeView",
    "AdjacencyView",
    "DegreeView",
    "Graph",
    "sets",
    "value",
    'edges is None', 'nodes is None', 'G = nx.DiGraph(D)',
    # shapes
    "n_times",
    "obj",
    "arrays",
    "lists",
    "func",
    "n_nodes",
    "n_estimated_nodes",
    "n_samples",
    "n_variables",
    # graphviz
    "graphviz",
    "Digraph",
}
numpydoc_xref_aliases = {
    # Networkx
    "nx.Graph": "networkx.Graph",
    "nx.DiGraph": "networkx.DiGraph",
    "Graph": "networkx.Graph",
    "DiGraph": "networkx.DiGraph",
    "nx.MultiDiGraph": "networkx.MultiDiGraph",
    "NetworkXError": "networkx.NetworkXError",
    "pgmpy.models.BayesianNetwork": "pgmpy.models.BayesianNetwork",
    "ArrayLike": "numpy.typing.ArrayLike",
    # pywhy-graphs
    "ADMG": "pywhy_graphs.ADMG",
    "PAG": "pywhy_graphs.PAG",
    "CPDAG": "pywhy_graphs.CPDAG",
    "pywhy_nx.MixedEdgeGraph": "pywhy_graphs.networkx.MixedEdgeGraph",
    "TimeSeriesGraph": "pywhy_graphs.classes.timeseries.TimeSeriesGraph",
    "TimeSeriesDiGraph": "pywhy_graphs.classes.timeseries.TimeSeriesDiGraph",
    "TimeSeriesMixedEdgeGraph": "pywhy_graphs.classes.timeseries.TimeSeriesMixedEdgeGraph",
    # joblib
    "joblib.Parallel": "joblib.Parallel",
    # pandas
    "pd.DataFrame": "pandas.DataFrame",
    "pandas.DataFrame": "pandas.DataFrame",
    "column": "pandas.DataFrame.columns",
}


default_role = "literal"

# Tell myst-parser to assign header anchors for h1-h3.
# myst_heading_anchors = 3
# suppress_warnings = ["myst.header"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build",
    "Thumbs.db",
    "**.ipynb_checkpoints",
    # "auto_examples/*.rst",
    # "auto_examples/index.rst",
    # "auto_examples/mixededge/index.rst",
    # "auto_examples/mixededge/*.rst",
]

source_suffix = [".rst", ".md"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "neps": ("https://numpy.org/neps", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference", None),
    "networkx": ("https://networkx.org/documentation/latest/", None),
    "nx-guides": ("https://networkx.org/nx-guides/", None),
    "matplotlib": ("https://matplotlib.org/stable", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable", None),
    "sklearn": ("https://scikit-learn.org/stable", None),
    "joblib": ("https://joblib.readthedocs.io/en/latest", None),
    "pygraphviz": ("https://pygraphviz.github.io/documentation/stable/", None),
    "graphviz": ("https://graphviz.readthedocs.io/en/stable/", None),
    "sphinx-gallery": ("https://sphinx-gallery.github.io/stable/", None),
}
intersphinx_timeout = 5

# sphinxcontrib-bibtex
bibtex_bibfiles = ["./references.bib"]
bibtex_style = "unsrt"
bibtex_footbibliography_header = ""

# The master toctree document.
master_doc = "index"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# Clean up sidebar: Do not show "Source" link
# html_show_sourcelink = False
# html_copy_source = False

html_theme = "pydata_sphinx_theme"

html_title = f"pywhy-graphs v{version}"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
templates_path = ["_templates"]
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
html_favicon = "_static/favicon_url.ico"

html_theme_options = {
    "icon_links": [
        dict(
            name="GitHub",
            url="https://github.com/py-why/pywhy-graphs",
            icon="fab fa-github-square",
        ),
    ],
    "use_edit_page_button": False,
    "navigation_with_keys": False,
    "show_toc_level": 1,
    "navbar_end": ["version-switcher", "navbar-icon-links"],
}

scrapers = ("matplotlib",)

sphinx_gallery_conf = {
    # Modules for which function level galleries are created.  In
    # this case sphinx_gallery and numpy in a tuple of strings.
    "doc_module": "pywhy_graphs",
    # Insert links to documentation of objects in the examples
    "reference_url": {
        "pywhy_graphs": None,
    },
    "backreferences_dir": "./generated",
    "plot_gallery": "True",  # Avoid annoying Unicode/bool default warning
    "examples_dirs": ["../examples"],
    "gallery_dirs": ["auto_examples"],
    "within_subsection_order": ExampleTitleSortKey,
    "subsection_order": ExplicitOrder(
        [
            "../examples/mixededge",
            "../examples/intro",
            "../examples/visualization",
        ]
    ),
    # "filename_pattern": "^((?!sgskip).)*$",
    "filename_pattern": r"\.py",
    "matplotlib_animations": True,
    "compress_images": ("images", "thumbnails"),
    "image_scrapers": scrapers,
    'show_memory': not sys.platform.startswith(('win', 'darwin')),
}

# Add pygraphviz png scraper, if available
try:
    from pygraphviz.scraper import PNGScraper

    sphinx_gallery_conf["image_scrapers"] += (PNGScraper(),)
except ImportError:
    pass

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    "index": ["search-field.html"],
    "install": [],
    "tutorial": [],
    "auto_examples/index": [],
}

html_context = {
    "versions_dropdown": {
        "dev": "v0.1 (devel)",
    },
}

# Enable/Disable nitpicky mode - which ensures that all references in the docs
# resolve.

nitpicky = True
nitpick_ignore = [
    ("py:obj", "nx.MixedEdgeGraph"),
    ("py:obj", "networkx.MixedEdgeGraph"),
    ("py:obj", "pywhy_graphs.networkx.MixedEdgeGraph"),
    ("py:obj", "pywhy_nx.MixedEdgeGraph"),
    ("py:class", "pywhy_nx.classes.timeseries.TimeSeriesGraph"),
    ("py:class", "pywhy_nx.classes.timeseries.TimeSeriesDiGraph"),
    ("py:class", "pywhy_nx.classes.timeseries.TimeSeriesMixedEdgeGraph"),
    ("py:class", "pywhy_nx.classes.timeseries.StationaryTimeSeriesGraph"),
    ("py:class", "pywhy_nx.classes.timeseries.StationaryTimeSeriesDiGraph"),
    ("py:class", "pywhy_nx.classes.timeseries.StationaryTimeSeriesMixedEdgeGraph"),
    ("py:class", "pywhy_graphs.classes.timeseries.base.tsdict"),
    ("py:class", "networkx.classes.mixededge.MixedEdgeGraph"),
]
nitpick_ignore_regex = [
    ('py:obj', r'pywhy_graphs.*timeseries.*'),
    ('py:obj', r"networkx*"),
]


# -- Other extension configuration -------------------------------------------

linkcheck_request_headers = dict(
    user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
)  # noqa: E501
linkcheck_anchors = False  # saves a bit of time
linkcheck_timeout = 15  # some can be quite slow
linkcheck_ignore = [
    "https://github.com/{group}/{project}/pull/",  # sphinx-issues will render this properly
]