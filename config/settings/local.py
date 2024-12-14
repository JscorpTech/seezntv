from config.settings.common import *  # noqa
from config.settings.common import ALLOWED_HOSTS, INSTALLED_APPS, REST_FRAMEWORK, MIDDLEWARE

INSTALLED_APPS += [
    "django_extensions",
    "silk",
]

ALLOWED_HOSTS += ["127.0.0.1", "192.168.100.26"]

REST_FRAMEWORK["DEFAULT_THROTTLE_RATES"] = {
    "user": "60/min",
}
MIDDLEWARE += [
    "silk.middleware.SilkyMiddleware",
]

SILKY_AUTHORISATION = True
SILKY_INTERCEPT_FUNC = lambda request: request.path.startswith("/api")
