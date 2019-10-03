class LinkedListNode:
    def __init__(self, v, s=None):
        self.value = v
        self.next = s

    def __repr__(self):
        return repr(self.value)
