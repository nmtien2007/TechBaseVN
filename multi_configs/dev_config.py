DATABASE_BACKEND = "django"
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'TechBaseVN',
		'USER': 'root',
		'PASSWORD': '12345678',
		'HOST': '127.0.0.1',
		'PORT': '3306',
		'CONN_MAX_AGE': 3600,
		'OPTIONS': {'charset': 'utf8mb4'},
	},
    'tech_base_vn_master': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'TechBaseVN',
        'USER': 'root',
        'PASSWORD': '12345678',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'CONN_MAX_AGE': 3600,
        'OPTIONS': {'charset': 'utf8mb4'},
    },
    'tech_base_vn_slave': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'TechBaseVN',
        'USER': 'root',
        'PASSWORD': '12345678',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'CONN_MAX_AGE': 3600,
        'OPTIONS': {'charset': 'utf8mb4'},
    },
}

CACHE_SERVERS = {
	"default": {
		"type": "django.core.cache.backends.memcached.MemcachedCache",
		"host": "127.0.0.1:11211",
	}
}

ISS = "http://localhost:8000"

SECRET_KEY = "QTl0bCZmfdshjEhed6646y2tT5xlh0I2s59UAPFuZQ6D2X9nzPBJT80UMv3P2EFxsbV3f11lRxkd2er0a5gP01L9tetqq0yqO6ES"

EXPIRED_TIME_TOKEN = 8 * 60