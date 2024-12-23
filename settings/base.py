# Python
from pathlib import Path
import os

# Third-Party
from dotenv import dotenv_values
from loguru import logger


BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG = dotenv_values()
SECRET_KEY = CONFIG.get("SECRET_KEY")
DEBUG = CONFIG.get("DEBUG")
ALLOWED_HOSTS = [CONFIG.get("HOST_ADDR", "127.0.0.1")]

INSTALLED_APPS = [
    # Apps
    "clients.apps.ClientsConfig",
    "events.apps.EventsConfig",
    # Third-Party
    "corsheaders",
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

AUTH_USER_MODEL = "clients.Client"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "settings.urls"

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
            ],
        },
    },
]

WSGI_APPLICATION = "settings.wsgi.application"
ASGI_APPLICATION = "settings.asgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": CONFIG.get("DB_NAME"),
        "USER": CONFIG.get("DB_USER"),
        "PASSWORD": CONFIG.get("DB_PASS"),
        "HOST": CONFIG.get("DB_HOST"),
        "PORT": CONFIG.get("DB_PORT"),
    }
}

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

LANGUAGE_CODE = "ru-RU"

TIME_ZONE = "Asia/Almaty"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles/")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [CONFIG.get("HOST_ADDR", "http://127.0.0.1")]
CORS_ALLOW_METHODS = ["GET", "POST"]
CORS_EXPOSE_HEADERS = ["X-Telegram-Bot-Token"]
CORS_ALLOW_HEADERS = [
    "X-Telegram-Bot-Token",
    "Content-Type",
    "Authorization",
]

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": CONFIG.get("CACHE_REDIS"),
    }
}
VOLUME = os.path.join(BASE_DIR, "volume/")
logger.add(
    sink=f"{VOLUME}logs_{{time:YYYY-MM-DD}}.log",
    level="DEBUG" if DEBUG else "INFO",
    enqueue=True,
    format="{time} {level} {message}",
    colorize=True,
    retention="7 days",
    rotation="00:00",
    compression="zip",
)
