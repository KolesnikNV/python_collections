class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def top(self):
        return self.items[0]

    def dequeue(self):
        item = self.items[0]
        self.items = self.items[1:]
        return item

    def enqueue(self, item):
        self.items.append(item)

    def get_item_index(self, item):
        for i in range(len(self.items)):
            if self.items[i] == item:
                return i


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def top(self):
        return self.items[-1] if not self.is_empty() else None

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def push(self, item):
        self.items.append(item)

    def get_item_index(self, item):
        for i in range(len(self.items)):
            if self.items[i] == item:
                return i


class LinkedList:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_value(self, value):
        self.value = value

    def set_next(self, next):
        self.next = next

    def insert_at_end(self, value):
        current = self

        while current.next is not None:
            current = current.next

        current.next = LinkedList(value)

    def insert_at_beginning(self, value):
        new_node = LinkedList(value)
        new_node.next = self.next
        self.value, new_node.value = new_node.value, self.value
        self.next = new_node

    def insert_after(self, value):
        new_node = LinkedList(value)
        new_node.next = self.next
        self.next = new_node

    def insert_before(self, value):
        new_node = LinkedList(self.value)
        new_node.next = self.next
        self.value = value
        self.next = new_node

    def delete(self):
        if self.next is not None:
            self.value = self.next.value
            self.next = self.next.next

    def find_value(self, value):
        current = self

        while current is not None:
            if current.value == value:
                return current

            current = current.next

        return None

    def print_list(self):
        current = self

        while current is not None:
            print(current.value, end=" -> ")
            current = current.next

        print("None")


class Node:
    def __init__(self, prev=None, value=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_value(self, value):
        self.value = value

    def set_next(self, next):
        self.next = next

    def set_prev(self, prev):
        self.prev = prev

    def insert_at_end(self, value):
        current = self
        while current.next is not None:
            current = current.next

        new_node = Node(prev=current, value=value)
        current.next = new_node

    def insert_at_beginning(self, value):
        new_node = Node(value=self.value, next=self.next, prev=self)

        if self.next:
            self.next.prev = new_node

        self.value = value
        self.next = new_node

    def insert_after(self, value):
        new_node = Node(prev=self, value=value, next=self.next)

        if self.next is not None:
            self.next.prev = new_node

        self.next = new_node

    def insert_before(self, value):
        new_node = Node(prev=self.prev, value=value, next=self)

        if self.prev is not None:
            self.prev.next = new_node

        self.prev = new_node

    def delete(self):
        if self.prev is not None:
            self.prev.next = self.next

        if self.next is not None:
            self.next.prev = self.prev

        self.prev = None
        self.next = None
        self.value = None

    def find_value(self, value):
        current = self

        while current is not None:
            if current.value == value:
                return current

            current = current.next

        return None

    def print_list(self):
        current = self

        while current is not None:
            print(current.value, end=" <-> ")
            current = current.next

        print("None")


class BinaryTree:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def get_value(self):
        return self.value

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_value(self, value):
        self.value = value

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinaryTree(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = BinaryTree(value)
            else:
                self.right.insert(value)

    def find(self, value):
        if value == self.value:
            return True
        elif value < self.value and self.left is not None:
            return self.left.find(value)
        elif value > self.value and self.right is not None:
            return self.right.find(value)
        return False

    def find_min(self):
        if self.left is None:
            return self.value
        return self.left.find_min()

    def delete(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)

        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value)

        else:
            if self.left is None:
                return self.right

            elif self.right is None:
                return self.left

            min_larger_value = self.right.find_min()
            self.value = min_larger_value
            self.right = self.right.delete(min_larger_value)

        return self

    def pre_order(self):
        print(self.value, end=" ")

        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def in_order(self):
        if self.left:
            self.left.in_order()

        print(self.value, end=" ")
        if self.right:
            self.right.in_order()

    def post_order(self):
        if self.left:
            self.left.post_order()

        if self.right:
            self.right.post_order()

        print(self.value, end=" ")

    def height(self):
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0

        return 1 + max(left_height, right_height)


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.adjacency_list:
            self.add_vertex(vertex1)
        if vertex2 not in self.adjacency_list:
            self.add_vertex(vertex2)

        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].remove(vertex2)
            self.adjacency_list[vertex2].remove(vertex1)

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:

            for adjacent in self.adjacency_list[vertex]:
                self.adjacency_list[adjacent].remove(vertex)

            del self.adjacency_list[vertex]

    def get_vertices(self):
        return list(self.adjacency_list.keys())

    def get_edges(self):
        edges = []
        for vertex in self.adjacency_list:
            for adjacent in self.adjacency_list[vertex]:
                if {vertex, adjacent} not in edges:
                    edges.append({vertex, adjacent})

        return edges

    def print_graph(self):
        for vertex, edges in self.adjacency_list.items():
            print(f"{vertex}: {', '.join(edges)}")
