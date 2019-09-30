import sys
import os
import bsp_docs_sphinx_theme

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.5.2'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinxprettysearchresults',
    'rst2pdf.pdfbuilder',
    'recommonmark'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

source_suffix = ['.rst']
master_doc = 'index'

project = u'Gyro'
copyright = u'2019, Perfect Sense, Inc.'
author = u'Perfect Sense'
release = u'0.99.0'
language = None

exclude_patterns = [
    '_build', 
    'Thumbs.db', 
    '.DS_Store', 
    'node_modules',
    'requirements.txt',
    'training',
    'inbox',
    'demo',
    'html'
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'collapse_navigation': True,
    #'display_version': False,
    'navigation_depth': 3,
    'logo_only': True
}

#html_context = {
#    "display_github": True,
#    "github_user": "perfectsense", # Username
#    "github_repo": "gyro", # Repo name
#    "github_version": "master", # Version
#    "conf_py_path": "/docs/", # Path in the checkout to the docs root
#}

html_theme_path = [bsp_docs_sphinx_theme.get_html_theme_path()]
html_static_path = ['_static']

html_logo = 'images/gyro-small-white.png'
html_css_files = [
    'css/gyro.css',
]

rst_prolog = """
.. include:: /substitutions.tsr
"""

html_show_sourcelink = False
html_show_sphinx = False

todo_include_todos = False

pdf_documents = [
 ('guides/gyro-user-guide',
     u'GyroUserGuide',
     u'Gyro User Guide',
     u'jeremy@brightspot.com'
 ),
 ('guides/writing-a-provider',
     u'GyroWritingAProvider',
     u'Gyro - Writing a Provider',
     u'jeremy@brightspot.com'
 )
]

# A comma-separated list of custom stylesheets. Example:
pdf_stylesheets = ['letter','main','opensans']

# A list of folders to search for stylesheets. Example:
pdf_style_path = ['.', '_styles']

#pdf_compressed = False
pdf_font_path = ['fonts']
pdf_language = "en_US"
#pdf_fit_mode = "shrink"
pdf_break_level = 1
pdf_breakside = 'any'
#pdf_inline_footnotes = True
pdf_verbosity = 0
pdf_use_index = True
#pdf_use_modindex = True
pdf_use_coverpage = True
pdf_cover_template = 'custom.tmpl'
#pdf_appendices = []
#pdf_splittables = False
#pdf_default_dpi = 72
#pdf_extensions = ['vectorpdf']
#pdf_page_template = 'cutePage'
#pdf_use_toc = True
pdf_toc_depth = 3
pdf_use_numbered_links = True
pdf_fit_background_mode = 'scale'
