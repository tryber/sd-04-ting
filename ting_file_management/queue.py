class Queue:
    def __init__(self):
        self._queue = list()

    def __len__(self):
        return len(self._queue)

    def enqueue(self, value):
        if value in self._queue:
            return None

        self._queue.append(value)
        return True

    def dequeue(self):
        if not self._queue:
            return None

        return self._queue.pop(0)

    def search(self, index):
        if 0 <= index < len(self):
            return self._queue[index]
        raise IndexError(f"o index {index} não existe")

    def __iter__(self):
        return iter(self._queue)
