### Linting
    pip install pylint-django

pylint --load-plugins pylint_django --django-settings-module=your.app.settings [..other options..] <path_to_your_sources>

    pylint --load-plugins pylint_django --django-settings-module=upload_many.settings  ./upload_many

### Format
    pip install black

black /path/to/your/project

    black ./upload_many
