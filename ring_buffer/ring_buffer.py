class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.oldestItem = None
        self.storage = []

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
            self.oldestItem = len(self.storage) - 1
            return
        self.oldestItem += 1
        if self.oldestItem >= self.capacity:
            self.oldestItem = 0
        self.storage[self.oldestItem] = item

    def get(self):
        return list(self.storage)