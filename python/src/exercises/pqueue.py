class PriorityQueue:
    """Class for priority queues."""

    def __init__(self):
        """Constructor for priority queues."""
        self._data = []

    def enqueue(self, item: object, priority: int) -> None:
        """Insert a new item with the given priority into the queue."""
        index = 0
        found = False
        for (i,(_element, p)) in enumerate(self._data):
            if p >= priority:
                index = i
                found = True
                break
        if not found:
            index = len(self._data)
        self._data.insert(index, (item, priority))

    def dequeue(self):
        """Remove the first item from the queue."""
        if len(self._data) > 0:
            (item,_) = self._data[0]
            self._data = self._data[1:]
            return item

    def length(self):
        """Return the length of the queue."""
        return len(self._data)

    def __str__(self):
        """String representation of the queue."""
        return str(self._data)

    def __repr__(self):
        """String representation for debugging."""
        return str(self._data)
