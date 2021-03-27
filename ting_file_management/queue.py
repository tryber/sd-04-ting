class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.fila = list()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.fila)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self.fila.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        if len(self.fila) == 0:
            return None
        if self.fila:
            return self.fila.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
        if index not in range(len(self.fila)):
            raise IndexError("Posição inválida")
        return self.fila[index]
