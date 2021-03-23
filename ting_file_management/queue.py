class Queue:
    FIRST_ELEMENT = 0

    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        if value not in self._data:
            self._data.append(value)

    def dequeue(self):
        if self._data:
            return self._data.pop(self.FIRST_ELEMENT)
        return None

    def search(self, index):
        if self._data and index < len(self) and index >= 0:
            return self._data[index]
        else:
            raise IndexError("index nao existe")

# deque = Queue()
# # elements_1 = [6, 7, 8, 9, 10]
# # for elem in elements_1:
# #     deque.enqueue(elem)
# deque.enqueue(42)
# deque.enqueue(43)
# deque.enqueue(44)
# print(deque.search(0))
