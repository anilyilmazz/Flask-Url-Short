from hashlib import blake2b

def short_url(url, digest_size=4):
    return blake2b(url.encode("utf-8"), digest_size=digest_size).hexdigest()