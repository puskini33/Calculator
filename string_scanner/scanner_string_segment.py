class ScannedStringSegment(object):

    def __init__(self, token, index, start, end):
        self.token = token
        self.index = index
        self.start_string = start
        self.end_string = end

    def __repr__(self):
        return f'ScannedStringSegment({self.token}, {self.index}, {self.start_string}, {self.end_string})'
