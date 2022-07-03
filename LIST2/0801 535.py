class Codec:
    def __init__(self):
        
        self.dictionary_en = {}
        self.dictionary_de = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.dictionary_en:
            return self.dictionary_en[longUrl]

        li = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
        n = len(li)
        cur = ""
        while cur and cur in self.dictionary_de:
            ri = random.randint(0, n - 1)
            cur += li[ri]
        self.dictionary_en[longUrl] = cur
        self.dictionary_de[cur] = longUrl

        return "http://tinyurl.com/" + self.dictionary_en[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        pre = "http://tinyurl.com/"
        key = shortUrl[len(pre):]

        return self.dictionary_de[key]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# self.decode(self.encode(url))