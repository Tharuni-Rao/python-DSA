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