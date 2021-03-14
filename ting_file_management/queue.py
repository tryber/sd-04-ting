class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._list = list()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self._list)

    def __iter__(self):
        return iter(self._list)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        if value in self._list:
            return False
        self._list.append(value)
        return value

    def dequeue(self):
        """Aqui irá sua implementação"""
        if len(self) == 0:
            return False
        return self._list.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
        if index < 0:
            raise IndexError(f"o index {index} não existe")
        return self._list[index]
