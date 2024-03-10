import hashlib

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def shorten_url(self, original_url):
        hash_object = hashlib.sha1(original_url.encode())
        hex_dig = hash_object.hexdigest()[:6]
        short_url = "http://short.url/" + hex_dig
        self.url_mapping[short_url] = original_url
        return short_url

    def restore_url(self, short_url):
        return self.url_mapping.get(short_url, "URL not found")

shortener = URLShortener()
original_url = "https://www.example.com"
short_url = shortener.shorten_url(original_url)
print("Shortened URL:", short_url)
restored_url = shortener.restore_url(short_url)
print("Restored URL:", restored_url)
