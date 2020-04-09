import os
from reader.compressed import bzipped, gzipped

# We use extension_map to select a different opener from the imported classes
extension_map = {
    '.bz2': bzipped.opener,
    '.gzip': gzipped.opener, 
}

class Reader():
    def __init__(self, filename):
        extension = os.path.splitext(filename)[1]
        # In this case we check if extension is inside our dictionary to define a different open method, if not we use the generic open
        extension_map.get(extension, open)
        opener = extension_map.get(extension, open)
        self.f = opener(filename, 'rt')

    def close(self):
        self.f.close()

    def read(self):
        return self.f.read()