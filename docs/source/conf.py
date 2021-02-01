import datetime

project = 'Shufflrr'
copyright = '2014-{}, Shufflrr'.format(
        datetime.datetime.now().year
)
author = 'Shufflrr'

release = '0.0.1'

extensions = ['sphinx.ext.autosectionlabel']

templates_path = ['_templates']

exclude_patterns = []

html_theme = 'default'

html_static_path = ['_static']

rst_prolog = """
 .. include:: <s5defs.txt>

 """
 
html_css_files = ['css/s5defs-roles.css']

html_logo = 'img/logo.png'
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}

master_doc = 'index'