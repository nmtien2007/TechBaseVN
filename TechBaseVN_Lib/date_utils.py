import time


def get_timestamp():
    return int(time.time())

def datetime_to_timestamp(dt):
    if dt is None:
        return None
    return int(time.mktime(dt.timetuple()))