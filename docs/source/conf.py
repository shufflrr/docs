import datetime

project = 'Shufflrr'
copyright = '2014-{}, Shufflrr'.format(
        datetime.datetime.now()
)
author = 'Shufflrr'

release = '0.0.1'

extensions = [
]

templates_path = ['_templates']

exclude_patterns = []

html_theme = 'default'

html_static_path = ['_static']

html_logo = 'img/logo.png'
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}
