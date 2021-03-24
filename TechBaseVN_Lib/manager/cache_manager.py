from django.core.cache import cache

CACHE_KEY_FUNC_GET_USER_INFOS_BY_IDS = {
	'cache_prefix': 'user_infos_by_ids.%s',
	'expiry_time': 10 * 60,
	'cache_key_converter': lambda prefix, user_ids: prefix % user_ids
}

def simple_cache_data(cache_key_converter, cache_prefix, expiry_time=60):
	def _cache_data(func):
		def _func(*args, **kwargs):
			cache_key = cache_key_converter(cache_prefix, *args)
			data = cache.get(cache_key)
			force_query = kwargs.get("force_query", False)
			if force_query or not data:
				data = func(*args)
				cache.set(cache_key, data, expiry_time)
			return data
		return _func
	return _cache_data
