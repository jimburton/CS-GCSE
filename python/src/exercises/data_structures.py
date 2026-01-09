class Stack:
    def __init__(self):
        self._data = []
        
    def push(self, item):
        self._data.append(item)
        
    def pop(self):
        if len(self._data) == 0:
            return None
        item = self._data[-1]
        self._data = self._data[:-1]
        return item
    
class Queue:
    def __init__(self):
        self._data = []
        
    def enqueue(self, item):
        self._data.append(item)
        
    def dequeue(self):
        if len(self._data) == 0:
            return None
        item = self._data[0]
        self._data = self._data[1:]
        return item

class PriorityQueue(Queue):
    
    def enqueue(self, pair):
        if not isinstance(pair, tuple):
            raise ValueError("Expecting a tuple, where the second element is an int")
        priority = pair[1]
        pos = -1
        for i,item in enumerate(self._data):
            if item[1] > priority:
                pos = i
                break
        if pos == -1:
            self._data.append(pair)
        else:
            self._data.insert(pos, pair)
        
    def dequeue(self):
        if len(self._data) == 0:
            return None
        item = self._data[0]
        self._data = self._data[1:]
        return item[0]
    
def test_stack():
    s = Stack()
    assert(s.pop() == None)
    s.push('a')
    assert(s.pop() == 'a')
    vals = ['a', 'b', 'c', 'd']
    [s.push(c) for c in vals]
    vals.reverse()
    for c in vals:
        assert(s.pop() == c)
        
def test_queue():
    s = Queue()
    assert(s.dequeue() is None)
    s.enqueue('a')
    assert(s.dequeue() == 'a')
    vals = ['a', 'b', 'c', 'd']
    [s.enqueue(c) for c in vals]
    for c in vals:
        assert(s.dequeue() == c)
