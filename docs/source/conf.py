from django.utils import timezone

project = 'Shufflrr'
copyright = '2014-{}, Shufflrr'.format(
    timezone.now().year
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
