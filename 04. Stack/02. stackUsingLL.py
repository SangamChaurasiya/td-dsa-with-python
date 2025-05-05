class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node("head") # Creating dummy node for the Stack
        self.size = 0

    def printStack(self):
        count = 0
        temp = self.head.next

        while count < self.size:
            print(temp.val, end="->")
            temp = temp.next
            count += 1
        
        print()

    def getSize(self):
        return self.size # Returning the size of the Stack
    
    def isEmpty(self):
        if self.size == 0:
            return True
        
        return False
    
    def peek(self):
        if self.isEmpty():
            print("The Stack is empty.")
            return
        
        return self.head.next.val # Returning the top most element of the Stack
    
    def push(self, val):
        temp = Node(val) # Creating new node
        temp.next = self.head.next # Assigning new element next to the head
        self.head.next = temp # Assigning head next to the new node
        self.size += 1 # Increasing the size of Stack

    def pop(self):
        if self.isEmpty():
            print("The Stack is empty.")
            return
        
        removed = self.head.next
        self.head.next = self.head.next.next # Assigning next element as head
        self.size -= 1 # Decreasing the size of Stack
        return removed.val # Returning removed element
    

myStack = Stack()

print(myStack.isEmpty())
print(myStack.pop())
print(myStack.peek())

myStack.push(10)
myStack.push(20)
myStack.push(30)

myStack.printStack()

print(myStack.isEmpty())
print(myStack.getSize())
print(myStack.peek())

print(myStack.pop())
myStack.printStack()