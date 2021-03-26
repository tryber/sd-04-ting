import sys
from collections import deque


class Queue:
    def __init__(self):
        self.file_queue = deque([])

    def __len__(self):
        return len(self.file_queue)

    def enqueue(self, value):
        self.file_queue.append(value)

    def dequeue(self):
        try:
            removed = self.file_queue.popleft()
            return removed
        except IndexError:
            sys.stdout.write('Não há elementos\n')

    def search(self, index):
        if index < 0 or index > len(self.file_queue) - 1:
            raise IndexError

        return self.file_queue[index]
