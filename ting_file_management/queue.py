import sys


class Queue:
    FIRST_ELEMENT = 0

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        if value in self._data:
            return False
        self._data.append(value)
        print(self._data)

    def dequeue(self):
        if len(self._data) == 0:
            return print("Não há elementos", file=sys.stdout)
        if self._data:
            return self._data.pop(self.FIRST_ELEMENT)
        return None

    def search(self, index):
        if index < 0:
            raise IndexError
        return self._data[index]

    def __iter__(self):
        return iter(self._data)
