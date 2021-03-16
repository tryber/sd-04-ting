# Iniciando o projeto TING
class Queue:
    FIRST_ELEMENT = 0

    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        return self._data.pop(self.FIRST_ELEMENT)

    def search(self, index):
        if index < 0:
            raise IndexError('list index out of range')

        return self._data[index]
