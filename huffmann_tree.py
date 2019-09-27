class HuffmannTree:
    def __init__(self, char, freq, izq=None, der=None):
        self.char = char
        self.freq = freq
        self.izq = izq
        self.der = der

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.freq == other.freq

    def __lt__(self, other):
        return self.freq < other.freq

    def __gt__(self, other):
        return self.freq > other.freq

    def __ge__(self, other):
        return self.__gt__ or self.__eq__

    def __le__(self, other):
        return self.__lt__ or self.__eq__

    def get_min(self, other):
        if self <= other: 
            return self 
        return other

    def get_max(self, other):
        if self >= other:
            return other  
        return self
