class BoundedStack:
    def __init__(self, capacity):
        self.arr = []
        self.capacity = capacity

    def is_empty(self):
        return len(self.arr) == 0

    def is_full(self):
        return len(self.arr) == self.capacity

    def push(self, value):
        if self.is_full():
            print(f"Stack overflow, cannot push {value}")
            return
        self.arr.append(value)

    def pop(self):
        if self.is_empty():
            print("Stack underflow, cannot pop")
            return None
        return self.arr.pop()


stack = BoundedStack(3)

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

print("Popped:", stack.pop())
print("Popped:", stack.pop())
print("Popped:", stack.pop())
stack.pop()

plates = []

plates.append(1)
plates.append(2)
plates.append(3)

print("Top of stack:", plates[-1])

while plates:
    print("Popped:", plates.pop())


class ArrayStack:
    def __init__(self, capacity=100):
        self.arr = [None] * capacity
        self.capacity = capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, value):
        if self.is_full():
            print("Stack overflow")
            return
        self.top += 1
        self.arr[self.top] = value

    def pop(self):
        if self.is_empty():
            print("Stack underflow")
            return None
        value = self.arr[self.top]
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.arr[self.top]

    def size(self):
        return self.top + 1


stack = ArrayStack()

stack.push(5)
stack.push(15)
stack.push(25)

print("Current size:", stack.size())
print("Top element:", stack.peek())

stack.pop()
print("Size after pop:", stack.size())
print("Top element now:", stack.peek())

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedStack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            print("Stack underflow")
            return None
        value = self.head.data
        self.head = self.head.next
        return value

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.head.data


stack = LinkedStack()

stack.push(7)
stack.push(14)
stack.push(21)

print("Top element:", stack.peek())

print("Popped:", stack.pop())
print("Popped:", stack.pop())
print("Popped:", stack.pop())
stack.pop()


def is_balanced(expression):
    brackets = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for c in expression:
        if c in '([{':
            brackets.append(c)
        elif c in ')]}':
            if not brackets:
                return False
            top = brackets.pop()
            if top != pairs[c]:
                return False

    return len(brackets) == 0


expr1 = "{a, (b, [c, d])}"
expr2 = "{a, (b, [c, d)])}"

print(f"{expr1} is balanced:", is_balanced(expr1))
print(f"{expr2} is balanced:", is_balanced(expr2))


def evaluate_postfix(expression):
    values = []
    tokens = expression.split()

    for token in tokens:
        if token in ('+', '-', '*', '/'):
            right = values.pop()
            left = values.pop()

            if token == '+':
                values.append(left + right)
            elif token == '-':
                values.append(left - right)
            elif token == '*':
                values.append(left * right)
            elif token == '/':
                values.append(left / right)
        else:
            values.append(int(token))

    return values[-1]


expression = "5 3 4 * +"
print(f"{expression} =", evaluate_postfix(expression))


def next_greater_element(arr):
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])

    return result


arr = [4, 5, 2, 25, 7, 8]
print(next_greater_element(arr))


def factorial(n):
    print(f"Entering factorial({n})")

    if n == 0:
        print("Base case reached, returning 1")
        return 1

    result = n * factorial(n - 1)
    print(f"Returning from factorial({n}), result: {result}")
    return result


answer = factorial(4)
print("Final answer:", answer)



