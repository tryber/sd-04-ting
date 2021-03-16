class Queue:
    def __init__(self):
        self.elements = list()

    def __len__(self):
        return len(self.elements)

    def enqueue(self, value):
        self.elements.insert(len(self.elements), value)

    def dequeue(self):
        return self.elements.pop(0)

    def search(self, index):
        if index < 0 or index > (len(self.elements) - 1):
            raise IndexError
        else:
            return self.elements[index]
