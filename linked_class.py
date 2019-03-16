from myiterator import MyIterator


class FDS:
    def __init__(self):
        self.array = []

    def enqueue(self, item):
        self.array.insert(0, item)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.array.pop()

    def pop(self):
        if self.is_empty():
            return None
        return self.array.pop()

    def push(self, item):
        return self.array.append(item)

    def peak(self):
        if self.is_empty():
            return None
        else:
            return self.array[-1]

    def size(self):
        return len(self.array)

    def is_empty(self):
        return self.size() == 0

    def __iter__(self):
        return MyIterator(self.array)


class ListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)
