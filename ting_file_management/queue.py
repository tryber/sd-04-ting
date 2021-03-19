class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._data = list()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self._data)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self._data.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        return self._data.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
        if len(self._data) > 0 and index > -1:
            return self._data[index]
        raise IndexError
        return
