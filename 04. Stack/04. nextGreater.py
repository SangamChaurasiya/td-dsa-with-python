class Node:
    def __init__(self, val, idx):
        self.val = val
        self.next = None
        self.index = idx


class Stack:
    def __init__(self):
        self.head = Node("head", -1) # Creating dummy node for the Stack
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
    
    def push(self, val, idx):
        temp = Node(val, idx) # Creating new node
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
        return removed # Returning removed element


def findNextGreater(givenNums):
    ans = [-1] * len(givenNums)

    myStack = Stack()

    for i in range(len(givenNums)):
        if myStack.isEmpty() or  givenNums[i] < myStack.peek(): # When lower element found add element in the Stack
            myStack.push(givenNums[i], i)
        else:
            while myStack.isEmpty() == False and givenNums[i] > myStack.peek(): # When greater element found remove thelower element from the Stack
                removed = myStack.pop()
                ans[removed.index] = givenNums[i]

            myStack.push(givenNums[i], i)
            
    return ans # Returning the next greater element array

print(findNextGreater([5, 2, 1, 6, 8]))
