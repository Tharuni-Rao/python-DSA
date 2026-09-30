class BoundedQueue:
    def __init__(self, capacity):
        self.arr = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = -1
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity

    def enqueue(self, value):
        if self.is_full():
            print(f"Queue overflow, cannot enqueue {value}")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.arr[self.rear] = value
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue underflow, cannot dequeue")
            return None
        value = self.arr[self.front]
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return value


queue = BoundedQueue(3)

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)

print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())
queue.dequeue()


from collections import deque

customers = deque()

customers.append("Ananya")
customers.append("Karan")
customers.append("Priya")

print("Front of queue:", customers[0])

while customers:
    print("Serving:", customers.popleft())


class CircularQueue:
    def __init__(self, capacity):
        self.arr = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = -1
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity

    def enqueue(self, value):
        if self.is_full():
            print("Queue overflow")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.arr[self.rear] = value
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue underflow")
            return None
        value = self.arr[self.front]
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return value


queue = CircularQueue(5)

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())

queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)

print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())


from collections import deque

class StackUsingQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, item):
        self.q2.append(item)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.popleft()

    def is_empty(self):
        return len(self.q1) == 0


stack = StackUsingQueues()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())
print(stack.pop())


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def insert_front(self, value):
        new_node = Node(value)
        new_node.next = self.front
        if self.front is not None:
            self.front.prev = new_node
        else:
            self.rear = new_node
        self.front = new_node

    def insert_rear(self, value):
        new_node = Node(value)
        new_node.prev = self.rear
        if self.rear is not None:
            self.rear.next = new_node
        else:
            self.front = new_node
        self.rear = new_node

    def display(self):
        current = self.front
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


deque = Deque()

deque.insert_rear(10)
deque.insert_rear(20)
deque.insert_front(5)
deque.insert_rear(30)

deque.display()


class PriorityQueue:
    def __init__(self):
        self.tasks = []

    def insert(self, name, priority):
        self.tasks.append((name, priority))

    def extract_max(self):
        max_index = 0
        for i in range(1, len(self.tasks)):
            if self.tasks[i][1] > self.tasks[max_index][1]:
                max_index = i
        return self.tasks.pop(max_index)

    def is_empty(self):
        return len(self.tasks) == 0


queue = PriorityQueue()

queue.insert("Sprained ankle", 2)
queue.insert("Chest pain", 9)
queue.insert("Minor cut", 1)
queue.insert("Broken arm", 6)

while not queue.is_empty():
    name, priority = queue.extract_max()
    print(f"Treating: {name} (priority {priority})")