
class LineScanner(object):
    
    def __init__(self, filename): 
        self.filename = filename
    
    def __iter__(self):
        with open(self.filename) as f:
            for line in f:
                yield line
    
