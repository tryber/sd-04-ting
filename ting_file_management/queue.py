class Queue:
    def __init__(self):
        self.queue = list()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        if value in self.queue:
            return None
        self.queue.append(value)
        return True

    def dequeue(self):
        if not self.queue:
            return None
        return self.queue.pop(0)

    def search(self, index):
        if index < 0:
            raise IndexError
        return self.queue[index]
