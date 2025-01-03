import os
from pathlib import Path
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.github",
    "django_extensions",
    "debug_toolbar",
    "users.apps.UsersConfig",
    "products.apps.ProductsConfig",
    "orders.apps.OrdersConfig",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    # Add the account middleware Allauth:
    "allauth.account.middleware.AccountMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "store.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "products.context_processors.baskets",
            ],
        },
    },
]

WSGI_APPLICATION = "store.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# SQLite
# Разкомментировать, если используется SQLite
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

PG_SERVICE_FILE_PATH = os.path.join(BASE_DIR, ".pg_service.conf")


# POSTGRESQL
# Закомментировать, если используется SQLite
if os.getenv("DOCKER_RUNTIME"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "HOST": os.environ.get("DOCKER_DB_HOST"),
            "NAME": os.environ.get("DOCKER_DB_NAME"),
            "USER": os.environ.get("DOCKER_DB_USER"),
            "PASSWORD": os.environ.get("DOCKER_DB_PASS"),
        }
    }

else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("DATABASES_NAME"),
            "USER": os.environ.get("DATABASES_USER"),
            "PASSWORD": os.environ.get("DATABASES_PASSWORD"),
            "HOST": os.environ.get("DATABASES_HOST"),
            "PORT": os.environ.get("DATABASES_PORT"),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"


if DEBUG:
    STATICFILES_DIRS = [
        BASE_DIR / "static",
    ]
else:
    STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"
LOGIN_REDIRECT_URL = "/"

#  OAuth settings
# LOGIN_URL = "/users/login/"
LOGIN_URL = "/admin/login/"

# Email settings
if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
else:
    EMAIL_HOST = os.environ.get("EMAIL_HOST")
    EMAIL_PORT = os.environ.get("EMAIL_PORT")
    EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
    EMAIL_USE_SSL = os.environ.get("EMAIL_USE_SSL")

# allauth
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by email
    "allauth.account.auth_backends.AuthenticationBackend",
]

SITE_ID = 1

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    "github": {
        "SCOPE": [
            "user",
        ],
    }
}

# Redis
REDIS_HOST = (
    "redis" if os.environ.get("DOCKER_RUNTIME") else os.environ.get("REDIS_HOST")
)
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": f"redis://{REDIS_HOST}:6379",
    }
}

# Celery settings
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_BROKER_URL = f"redis://{REDIS_HOST}:6379"
CELERY_RESULT_BACKEND = f"redis://{REDIS_HOST}:6379"

# My settings:
# Вкл/Выкл Celery
CELERY_SWITCH = True
# Отсылать письмо на email c проверочной ссылкой
EMAIL_VERIFICATION = False
# ссылка на корневую страницу
DOMAIN_NAME = os.environ.get("DOMAIN_NAME")
