# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
sys.path.insert(0, os.path.abspath('../../python'))
sys.path.insert(0, os.path.abspath('../../cpp'))

# compile .so for cython files
os.system("cd ../.. && python setup.py build_ext --inplace")

# run api-doc in terminal
os.system("sphinx-apidoc -fMT ../../python/pumapy -o files --templatedir=template")

# -- Project information -----------------------------------------------------

project = 'PuMA'
copyright = '2021, PuMA Team'
author = 'PuMA Team'

# The full version, including alpha/beta/rc tags
release = '3.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
              'sphinx.ext.autodoc',
              'sphinx.ext.autosummary',
              'sphinx.ext.mathjax',
              'sphinx.ext.viewcode',
              'nbsphinx',
              'nbsphinx_link',
              'recommonmark',
              'breathe',
              'exhale',
              ]

# to be able to add the README.md
from m2r import MdInclude
from recommonmark.transform import AutoStructify
def setup(app):
    config = {
        # 'url_resolver': lambda url: github_doc_root + url,
        'auto_toc_tree_section': 'Contents',
        'enable_eval_rst': True,
    }
    app.add_config_value('recommonmark_config', config, True)
    app.add_transform(AutoStructify)

    # from m2r to make `mdinclude` work
    app.add_config_value('no_underscore_emphasis', False, 'env')
    app.add_config_value('m2r_parse_relative_links', False, 'env')
    app.add_config_value('m2r_anonymous_references', False, 'env')
    app.add_config_value('m2r_disable_inline_math', False, 'env')
    app.add_directive('mdinclude', MdInclude)

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'files/pumapy.rst', '**.ipynb_checkpoints']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']
html_logo = "puma_logo.png"
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}


from unittest import mock
MOCK_MODULES = [
                'TexGen.Core', 'dolfin', 'numpy', 'matplotlib', 'pyvista', 'pyevtk', 'pyevtk.hl', 
                'skimage', 'skimage.transform', 'skimage.io', 'skimage.filters', 'skimage.morphology', 
                'scipy', 'scipy.optimize', 'scipy.sparse', 'scipy.sparse.linalg', 'scipy.ndimage', 'scipy.ndimage.filters', 
                ]

for module_name in MOCK_MODULES:
    sys.modules[module_name] = mock.Mock()


# -- Breathe - Exhale configuration -------------------------------------------------

breathe_projects = {
    "My Project": "./doxyoutput/xml"
}
breathe_default_project = "My Project"

# Setup the exhale extension
exhale_args = {
    # These arguments are required
    "containmentFolder":     "./cpp_api",
    "rootFileName":          "cpp_library_root.rst",
    "rootFileTitle":         "Documentation tree",
    "doxygenStripFromPath":  "..",
    # Suggested optional arguments
    "createTreeView":        True,
    # TIP: if using the sphinx-bootstrap-theme, you need
    # "treeViewIsBootstrap": True,
    "exhaleExecutesDoxygen": True,
    "exhaleDoxygenStdin":    "INPUT = ../../cpp"
}

# Tell sphinx what the primary language being documented is.
primary_domain = 'cpp'

# Tell sphinx what the pygments highlight language should be.
highlight_language = 'cpp'