from config.env import env

CACHES = {
    "default": {
        "BACKEND": env("CACHE_BACKEND"),
        "LOCATION": env("REDIS_URL"),
        "TIMEOUT": env("CACHE_TIMEOUT"),
    },
}

CACHE_MIDDLEWARE_SECONDS = env("CACHE_TIMEOUT")


CACHEOPS_REDIS = env.str("REDIS_URL")
CACHEOPS_DEFAULTS = {
    "timeout": env.str("CACHE_TIMEOUT"),
}
CACHEOPS = {
    # !NOTE: api => "you app name"
    # "api.*": {
    #     "ops": "all",  # Barcha turdagi so'rovlarni keshga olish
    #     "timeout": 60 * 5,  # 5 daqiqa davomida saqlash
    # },
    # "accounts.*": {
    #     "ops": "all",  # Barcha turdagi so'rovlarni keshga olish
    #     "timeout": 60 * 5,  # 5 daqiqa davomida saqlash
    # },
}
CACHEOPS_DEGRADE_ON_FAILURE = True
CACHEOPS_ENABLED = env.bool("CACHE_ENABLED", False)
