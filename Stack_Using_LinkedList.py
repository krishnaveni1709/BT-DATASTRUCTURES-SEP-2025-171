class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop from an empty stack.")
            return None
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data

    def peek(self):
        if self.is_empty():
            print("Stack is empty. No top element.")
            return None
        return self.top.data
    def is_empty(self):
        return self.top is None
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
popped_data = stack.pop()
print("Popped:", popped_data)
top_element = stack.peek()
print("Top element:", top_element)
is_empty = stack.is_empty()
print("Is stack empty?", is_empty)
stack.display()
