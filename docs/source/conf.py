# -*- coding: utf-8 -*-
#
# ChainerCV documentation build configuration file, created by
# sphinx-quickstart on Fri Mar  3 16:38:20 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import inspect
import os
import pkg_resources
import sys


__version__ = pkg_resources.get_distribution('chainercv').version

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

rtd_version = os.environ.get('READTHEDOCS_VERSION')
if rtd_version == 'latest':
    tag = 'master'
else:
    tag = 'v{}'.format(__version__)
extlinks = {
    'blob':
        ('https://github.com/chainer/chainercv/blob/{}/%s'.format(tag), ''),
    'tree':
        ('https://github.com/chainer/chainercv/tree/{}/%s'.format(tag), ''),
}

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.autosummary',
              'sphinx.ext.doctest',
              'sphinx.ext.intersphinx',
              'sphinx.ext.mathjax',
              'sphinx.ext.napoleon',
              'sphinx.ext.linkcode']

try:
    import sphinxcontrib.spelling  # noqa
    extensions.append('sphinxcontrib.spelling')
except ImportError:
    pass

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'ChainerCV'
copyright = u'2017, Preferred Networks, inc.'
author = u'Preferred Networks, inc.'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'0.12.0'
# The full version, including alpha/beta/rc tags.
release = u'0.12.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# Napoleon settings
napoleon_use_ivar = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
if not on_rtd:
    html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_style = 'css/modified_theme.css'

if on_rtd:
    html_context = {
        'css_files': [
            'https://media.readthedocs.org/css/sphinx_rtd_theme.css',
            'https://media.readthedocs.org/css/readthedocs-doc-embed.css',
            '_static/css/modified_theme.css',
        ],
    }


# -- Options for HTMLHelp output ------------------------------------------

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# Output file base name for HTML help builder.
htmlhelp_basename = 'ChainerCVdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {}
# The paper size ('letterpaper' or 'a4paper').
#
# 'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#
# 'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#
# 'preamble': '',

# Latex figure (float) alignment
#
# 'figure_align': 'htbp',

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'ChainerCV.tex', u'ChainerCV Documentation',
     u'Preferred Networks, inc.', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'chainercv', u'ChainerCV Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'ChainerCV', u'ChainerCV Documentation',
     author, 'ChainerCV', 'One line description of project.',
     'Miscellaneous'),
]


autosummary_generate = True

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('http://docs.scipy.org/doc/numpy/', None),
}

source_root = None


def _is_egg_directory(path):
    return (path.endswith('.egg') and
            os.path.isdir(os.path.join(path, 'EGG-INFO')))


def _is_git_root(path):
    return os.path.isdir(os.path.join(path, '.git'))


def _import_object_from_name(module_name, fullname):
    obj = sys.modules.get(module_name)
    if obj is None:
        return None
    for comp in fullname.split('.'):
        obj = getattr(obj, comp)
    return obj


_source_root = None


def _find_source_root(source_abs_path):
    # Note that READTHEDOCS* environment variable cannot be used, because they
    # are not set under docker environment.
    global _source_root
    if _source_root is None:
        dir = os.path.dirname(source_abs_path)
        while True:
            if _is_egg_directory(dir) or _is_git_root(dir):
                # Reached the root directory
                _source_root = dir
                break

            dir_ = os.path.dirname(dir)
            if len(dir_) == len(dir):
                raise RuntimeError('Couldn\'t parse root directory from '
                                   'source file: {}'.format(source_abs_path))
            dir = dir_
    return _source_root


def _get_source_relative_path(source_abs_path):
    return os.path.relpath(source_abs_path, _find_source_root(source_abs_path))


def _get_sourcefile_and_linenumber(obj):
    # Retrieve the original function wrapped by contextlib.contextmanager
    if callable(obj):
        closure = getattr(obj, '__closure__', None)
        if closure is not None:
            obj = closure[0].cell_contents

    # Get the source file name and line number at which obj is defined.
    try:
        filename = inspect.getsourcefile(obj)
    except TypeError:
        # obj is not a module, class, function, ..etc.
        return None, None

    # inspect can return None for cython objects
    if filename is None:
        return None, None

    # Get the source line number
    _, linenum = inspect.getsourcelines(obj)

    return filename, linenum


def linkcode_resolve(domain, info):
    if domain != 'py' or not info['module']:
        return None

    # Import the object from module path
    obj = _import_object_from_name(info['module'], info['fullname'])

    # If it's not defined in the internal module, return None.
    mod = inspect.getmodule(obj)
    if mod is None:
        return None
    if not (mod.__name__ == 'chainercv'
            or mod.__name__.startswith('chainercv.')):
        return None

    # Retrieve source file name and line number
    filename, linenum = _get_sourcefile_and_linenumber(obj)
    if filename is None or linenum is None:
        return None

    filename = os.path.realpath(filename)
    relpath = _get_source_relative_path(filename)

    return 'https://github.com/chainer/chainercv/blob/{}/{}#L{}'.format(
        tag, relpath, linenum)
