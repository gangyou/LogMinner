
class LineScanner(object):
    
    def __init__(self, *filenames): 
        self.filenames = filenames
        self.count = 0
        self.lines_number = 0
    
    def __iter__(self):
        for filename in self.filenames:
            with open(filename) as f:
                for line in f:
                    if self.count % 1000 == 0: print str(self.count) + " lines passed."
                    self.count += 1
                    yield line
    
    def lines_count(self):
        print "counting lines..."
        count = 0
        for filename in self.filenames:
            with open(filename, 'rb') as f:
                while True:
                    b = f.read(8192*1024)
                    if not b: break
                    count += b.count("\n")
        print "total {0} lines".format(count)
        return count
