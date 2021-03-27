class Queue:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        solution = self.data[0]
        del self.data[0]
        return solution

    def search(self, index):
        if len(self.data) - 1 < index or 0 > index:
            raise IndexError
        return self.data[index]
