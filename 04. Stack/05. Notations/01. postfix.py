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
    

# NOTE: Whenever we will find numbers then we will push inside the Stack and when we find operator then we will pop out those numbers and then apply that operator on those numbers then push back the result in the Stack repeat the same operation again until the number or operator found.
def evalPostfix(givenStr):
    ops = ['+', '-', '/', '*']

    myStack = Stack()

    for i in givenStr:
        if i in ops:
            second = myStack.pop() # Poping the top element
            first = myStack.pop() # Poping the top element

            myStack.push(eval(f"{first}{i}{second}")) # Pushing the result in the Stack
        else:
            myStack.push(i) # Pushing in the Stack if number found

    return myStack.pop()


# Postfix to Infix
def postfixToInfix(givenStr):
    ops = ['+', '-', '/', '*']

    myStack = Stack()

    for i in givenStr:
        if i in ops:
            second = myStack.pop() # Poping the top element
            first = myStack.pop() # Poping the top element

            myStack.push(f"({first}{i}{second})") # Pushing the result in the Stack
        else:
            myStack.push(i) # Pushing in the Stack if number found

    return myStack.pop() # This will return the infix form


print(evalPostfix('12+5-'))
infix = postfixToInfix('12+5-')
print(f"{infix} -> {eval(infix)}") # Evaluating the infix result


# Infix to Postfix
def getPriority(operation):
    if operation == "*" or operation == "/":
        return 1
    return 0

def infixToPostfix(givenStr):
    ans = ""
    ops = ['+', '-', '*', '/']

    myStack = Stack()
    for i in givenStr:
        if i in ops:
            while myStack.isEmpty() == False and getPriority(i) < getPriority(myStack.peek()): # If operator precedence is less than removing other operator
                ans += myStack.pop() # Adding removed operator in the answer

            myStack.push(i) # Othertwise adding new operator in the Stack
        else:
            ans += i # Adding number in the answer
    
    while myStack.isEmpty() == False:
        ans += myStack.pop() # Adding rest operators ad numbers in the answer

    return ans


print(infixToPostfix('1*2+3'))
