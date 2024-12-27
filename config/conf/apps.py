from config.env import env

APPS = [
    "cacheops",
    "rest_framework",
    "corsheaders",
    "django_filters",
    "rosetta",
    "django_redis",
    "rest_framework_simplejwt",
    "django_ckeditor_5",
    "drf_spectacular",
    "adminsortable2",
    "django_core",
    "click_up",
]


if env.str("PROJECT_ENV") == "debug":
    APPS += [
        "silk",
    ]
