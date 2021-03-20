class Queue:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        if value in self._data:
            return False
        self._data.append(value)

    def dequeue(self):
        if len(self._data) == 0:
            return None
        value = self._data[0]
        del self._data[0]
        return value

    def search(self, index):
        if index < 0:
            raise IndexError
        return self._data[index]

    def __iter__(self):
        return iter(self._data)
