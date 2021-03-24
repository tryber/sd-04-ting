class Queue:
    def __init__(self):
        self._list = list()

    def __len__(self):
        return len(self._list)

    def __iter__(self):
        return iter(self._list)

    def enqueue(self, value):
        if value in self._list:
            return False
        self._list.append(value)
        return value

    def dequeue(self):
        if len(self) == 0:
            return False
        return self._list.pop(0)

    def search(self, index):
        if index < 0:
            raise IndexError(f"o index {index} não existe")
        return self._list[index]
