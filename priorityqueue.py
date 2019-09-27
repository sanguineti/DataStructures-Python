import numpy as np
from huffmann_tree import HuffmannTree


class PriorityQueue:
    def __init__(self):
        self.nodes = np.empty(0, dtype=HuffmannTree)
        self.size = 0

    def swim(self, a, j):
        while j >= 1 and a[j].freq < a[(j-1)//2].freq:
            a[j], a[(j-1)//2] = a[(j-1)//2], a[j]
            j = (j-1) // 2

    def sink(self, a, j, n):
        while 2*j + 1 < n:
            k = 2*j + 1
            if k + 1 < n and a[k+1].freq < a[k].freq:
                k += 1
            if a[j].freq <= a[k].freq:
                break
            a[j], a[k] = a[k], a[j]
            j = k

    def add(self, node):
        j = self.size
        a = np.empty(j + 1, dtype=HuffmannTree)
        for i in range(j):
            a[i] = self.nodes[i]
        a[j] = node
        self.nodes = a
        self.swim(self.nodes, self.size)
        self.size += 1

    def get_minimum(self):
        if self.size == 0:
            raise Exception("Sorry, the Priority Queue is empty.")
        j = self.size
        a = np.copy(self.nodes)[0]
        self.nodes[0] = self.nodes[j - 1]
        self.nodes = self.nodes[:j-1]
        self.size -= 1
        self.sink(self.nodes, 0, self.size)
        return a

    def add_array(self, array):
        for node in array:
            self.add(node)
