class Queue:
    def __init__(self):
        self.fila = list()

    def __len__(self):
        return len(self.fila)

    def enqueue(self, value):
        self.fila.append(value)

    def dequeue(self):
        if len(self.fila) == 0:
            return None
        if self.fila:
            return self.fila.pop(0)
            
    def search(self, index):
        if index not in range(len(self.fila)):
            raise IndexError('Posição inválida')
        return self.fila[index]