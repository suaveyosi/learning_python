import socket
class Resolver():
    def __init__(self):
        self._cache = {}

    def __call__(self,host):
        # We check if we have already the host in our cache
        if host not in self._cache:
        # if not we add it
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

    # Clean cache
    def clean_cache(self):
        self._cache.clear()

    # Check if host is in cache
    def host_in_cache(self,host):
        return host in self._cache
