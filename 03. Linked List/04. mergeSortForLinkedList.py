class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


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

    def middle(self, head):
        if head == None:
            return head
        
        slow = head
        fast = head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow
    
    def merge(self, head, toMergeHead):
        headA = head # Left part head
        headB = toMergeHead # Right part head

        temp = Node(0) # First Node
        tail = temp # First Tail

        while True:
            if headA == None:
                tail.next = headB # if reached the last node of the left part then assign next to the right
                break

            if headB == None:
                tail.next = headA # if reached the last node of the right part then assign next to the left
                break

            if headA.val < headB.val: 
                tail.next = headA # If left value less than right value then move next to left
                headA = headA.next # Moving to the next of the left
            else:
                tail.next = headB # If right value less than left value then move next to right
                headB = headB.next # Moving to the next of the right

            tail = tail.next # moving next to the tail

        return temp.next # returning the head of the sorted LL
    
    def mergeSort(self, head):
        if head == None or head.next == None:
            return head
        
        middle = self.middle(head) # Finding the middle part
        nextToMiddle = middle.next # Getting the next after the middle

        middle.next = None
        

        # Finding left and right part
        left = self.mergeSort(head)
        right = self.mergeSort(nextToMiddle)

        sortedLinkedList = self.merge(left, right) # Merging the left and right part

        return sortedLinkedList
        
    
linkedList = LinkedList()

linkedList.insertionAtTail(0)
linkedList.insertionAtTail(1)
linkedList.insertionAtTail(5)
linkedList.insertionAtTail(8)
linkedList.insertionAtTail(6)
linkedList.insertionAtTail(2)
linkedList.insertionAtTail(3)
linkedList.insertionAtTail(7)

linkedList.printLinkedList() # printing the LL before the Merge Sort

linkedList.head = linkedList.mergeSort(linkedList.head) # performing the Merge Sort on the LL

linkedList.printLinkedList() # printing the LL after the Merge Sort
