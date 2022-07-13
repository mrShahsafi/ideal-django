settings_list = [
    '__init__.py', 'base.py', 'dev.py', 'prod.py',
    'drf_settings.py', 'addresses.py', 'cors_setting.py',
    'key.py.conf', 'local.py.conf'
]


init_content = '''
from os import getenv

env = getenv("DJANGO_ENV", default="development")

if env == "production":
    print("You Are in the Production Mode.")
    from .prod import *
elif env == "development":
    print("Warning! You Are in the Development Mode.\nDo Not use in any server.")
    from .dev import *
'''

dev_content = '''
from .base import *

# import socket  # only if you haven't already imported this

DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]

try:
    from .local import *
except Exception:
    pass

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }
#
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DB_NAME", default="yuruma"),
        "USER": os.getenv("DB_USER", default="yurumauser"),
        "PASSWORD": os.getenv("DB_PASS", default="2187481"),
        "PORT": "5432",
    }
}

INSTALLED_APPS += [
    "debug_toolbar",
    #    'django_extensions'
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

"""
    These commented config  will use \
        when you are running the project on Docker. 
"""
# hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
# INTERNAL_IPS = [ip[:-1] + "1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]

INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
'''

prod_content = '''
from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DB_NAME", default="db"),
        "USER": os.getenv("DB_USER", default="root"),
        "PASSWORD": os.getenv("DB_PASS", default="root-password"),
        "HOST": "postgres",
        "PORT": "5432",
    }
}


'''

drf_content = '''
from datetime import timedelta
from .base import SITE_NAME

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PARSER_CLASSES": (
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.MultiPartParser",
        "rest_framework.parsers.FileUploadParser",
    ),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ),
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_PAGINATION_CLASS": "core.pagination.CustomPagination",
    "PAGE_SIZE": 9,
    # "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.AcceptHeaderVersioning", # when we active versioning the swagger ui brakes!= ""
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "EXCEPTION_HANDLER": "core.errors.custom_exception_handler",
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
}

REGISTRATION = {
    "TOKEN_EXPIRE": 1200,  # 20 Minuets
    "REFRESH_LINK_LIMIT": 1200,  # 20 Minuets
}

FORGOT_PASSWORD = {
    "TOKEN_EXPIRE": timedelta(minutes=30),
    "RESEND_TOKEN_AVAILABLE_AT": timedelta(minutes=2),
}

# REMEMBERED_USER_ACCESS_LIFETIME = datetime.timedelta(days=50)
SPECTACULAR_SETTINGS = {
    "TITLE": f"{SITE_NAME} Project API",
    "DESCRIPTION": "Finding and reserving homes",
    "VERSION": "1.0.0",
    # OTHER SETTINGS
}
'''

local_content = '''
# Remove .conf

# email configuration informations must remains here
#    because of the security reasons,

EMAIL_USE_TLS = bool
EMAIL_HOST = ''
EMAIL_PORT = int
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = ''
'''
