class Queue:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        '''add na fila'''
        self._data.append(value)

    def dequeue(self):
        '''remove da fila'''
        if len(self._data) == 0:
            return None
        value = self._data[0]
        del self._data[0]
        return value

    def search(self, index):
        '''buscar a partir do indice'''
        if len(self._data) > 0 and index > -1:
            return self._data[index]
        raise IndexError
        return
