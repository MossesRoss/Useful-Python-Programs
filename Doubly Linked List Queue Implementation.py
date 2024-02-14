class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.head = None
        self.last = None

    def enqueue(self, data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last.next.prev = self.last
            self.last = self.last.next

    def dequeue(self):
        if self.head is None:
            return None
        temp = self.head.data
        self.head = self.head.next
        self.head.prev = None
        return temp

    def first(self):
        return self.head.data if self.head else None

    def size(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def isEmpty(self):
        return self.head is None

    def printqueue(self):
        if self.head:
            print("queue elements:")
            temp = self.head
            while temp:
                print(temp.data, end="->")
                temp = temp.next
            print()


if __name__ == "__main__":
    queue = Queue()

    print("Queue operations:")

    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)

    queue.printqueue()

    print("First element:", queue.first())
    print("Size:", queue.size())

    queue.dequeue()
    queue.dequeue()

    print("After dequeueing twice:")
    queue.printqueue()

    print("Empty:", queue.isEmpty())
