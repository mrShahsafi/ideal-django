files_list = [
    '__init__.py', 'urls.py', 'admin.py', 'apps.py',
    'signals.py', 'managers.py'
]

modules_list = [
    'models', 'tests', 'serializers',
    'views', 'logics', 'utils', 'management', 'mixins', 'migrations'
]

apps_content = (
    lambda app_name="core": f"""
from django.apps import AppConfig


class {app_name.capitalize()}Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "{app_name}"
    """
)
