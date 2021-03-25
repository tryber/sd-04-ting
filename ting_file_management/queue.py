class Queue:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        if value in self._data:
            return False
        self._data.append(value)
        return value

    def dequeue(self):
        if len(self) == 0:
            return False
        return self._data.pop(0)

    def search(self, index):
        if index < 0:
            raise IndexError
        return self._data[index]

    def __iter__(self):
        return iter(self._data)
