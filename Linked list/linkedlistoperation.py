class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def insert_at_position(self, value, position):
        if position == 0:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        for _ in range(position - 1):
            if current is None:
                return
            current = current.next

        if current is None:
            return

        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node

    def search(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


linked_list = LinkedList()
linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(40)

linked_list.insert_at_position(30, 2)
linked_list.display()

print("Search for 30:", linked_list.search(30))


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


first = Node(10)
second = Node(20)
third = Node(30)

first.next = second
second.next = third

current = first
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

        

    def insert_at_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


linked_list = LinkedList()
linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_front(5)




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, value):
        new_node = Node(value)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def display_forward(self):
        current = self.head
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


linked_list = DoublyLinkedList()
linked_list.insert_at_front(30)
linked_list.insert_at_front(20)
linked_list.insert_at_front(10)

linked_list.display_forward()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def display(self):
        if self.head is None:
            print("Empty list")
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(back to start)")


linked_list = CircularLinkedList()
linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)

linked_list.display()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def has_cycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
c.next = a

print("Contains cycle:", has_cycle(a))


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_list(head):
    previous = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous


def display(head):
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

print("Original: ", end="")
display(head)

head = reverse_list(head)

print("Reversed: ", end="")
display(head)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge_sorted_lists(list1, list2):
    dummy = Node(0)
    tail = dummy

    while list1 is not None and list2 is not None:
        if list1.data <= list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 if list1 is not None else list2
    return dummy.next


def display(head):
    while head is not None:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


list1 = Node(1)
list1.next = Node(3)
list1.next.next = Node(5)

list2 = Node(2)
list2.next = Node(4)
list2.next.next = Node(6)

merged = merge_sorted_lists(list1, list2)
display(merged)




linked_list.display()
