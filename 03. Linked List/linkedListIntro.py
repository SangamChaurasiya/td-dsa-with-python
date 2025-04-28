class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# # Linked List implementation without using the LinkedList class-
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)

# print(head.val) # 1
# print(head.next.val) # 2
# print(head.next.next.val) # 3
# print(head.next.next.next.val) # None type has no 'val' attribute


class LinkedList:
    head = None # setting the head

    # Printing the Linked List
    def printLinkedList(self):
        temp = self.head

        while temp != None:
            print(temp.val, end="->") # printing the values
            temp = temp.next # moving to the next node
        
    # Inserting new Node at the end
    def insertionAtTail(self, value):
        temp = self.head

        if temp == None:
            self.head = Node(value) # Inserting element at the start when no head found
            return

        while temp.next != None:
            temp = temp.next # moving to the next node

        temp.next = Node(value) # Adding the new node at the end of LL

    # Inserting new Node at the start of LL
    def insertionAtHead(self, value):
        temp = Node(value) # Creating new Node
        temp.next = self.head #  Assigning head as the next of the new node
        self.head = temp # Reassigning the head

    # Inserting new Node at the kth position
    def insertion(self, value, k):
        if k == 0:
            self.insertionAtHead(value) # if k is 0 then inserting the new element at the head
            return
        
        count = 2 # setting the count to 2 as we know if we have elements in the LL
        temp = self.head

        while temp is not None and count < k:
            count += 1
            temp = temp.next # moving to the new node

        if temp is None:
            print("Insertion operation cannot be done as reached at the end of the LL.")
            return
        rest = temp.next # storing rest nodes after finding the nodes after the kth nodes
        temp.next = Node(value) # storing new node to the kth position
        temp.next.next = rest # assigning new node next to the rest of the nodes


linkedList = LinkedList()

linkedList.insertionAtTail(1)
linkedList.insertionAtTail(2)
linkedList.insertionAtTail(3)
linkedList.insertionAtHead(0)
linkedList.insertion(-1, 5)
linkedList.printLinkedList()
