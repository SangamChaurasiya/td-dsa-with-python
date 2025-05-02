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

        print()
        
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

    def deleteAtHead(self):
        if self.head is None:
            print("List is empty.")
            return
        self.head = self.head.next

    def deleteAtTail(self):
        if self.head is None:
            print("List is empty.")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next

        temp.next = None

    def deletion(self, k):
        if k < 0:
            print("Invalid position.")
            return

        if self.head is None:
            print("List is empty.")
            return

        if k == 0:
            self.deleteAtHead()
            return

        temp = self.head
        count = 0

        while temp is not None and count < k - 1:
            temp = temp.next
            count += 1

        if temp is None or temp.next is None:
            print("Position out of range.")
            return

        temp.next = temp.next.next   

    # # Method 1: Using two LL 
    # newHead = None
    # def reverse(self, curr):
    #     if curr.next == None:
    #         self.newHead = Node(curr.val)
    #         self.head = self.newHead
    #         return
        
    #     self.reverse(curr.next)

    #     temp = self.newHead
    #     while temp.next != None:
    #         temp = temp.next

    #     temp.next = Node(curr.val)

    # Method 2: Using single LL
    def reverse(self):
        prev = None
        curr = self.head

        while curr != None:
            nextNode = curr.next # pointing to the next node
            curr.next = prev # assigning next node to the prev
            prev = curr # assigning prev to curr
            curr = nextNode

        self.head = prev

linkedList = LinkedList()

linkedList.insertionAtTail(1)
linkedList.insertionAtTail(2)
linkedList.insertionAtTail(3)
linkedList.insertionAtHead(0)

# LL before reverse
linkedList.printLinkedList()

# # Method 1: Calling reverse() using 2 LLs
# linkedList.reverse(linkedList.head)

# method 2: Calling rverse() using single LL
linkedList.reverse()

# LL after reverse
linkedList.printLinkedList()
