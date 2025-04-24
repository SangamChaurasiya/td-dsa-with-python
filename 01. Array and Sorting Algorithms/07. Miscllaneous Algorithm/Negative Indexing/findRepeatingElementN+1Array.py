# NOTE: You are not alllowed to chnage in the given array and in the constant space so we cannot use negative indexing algorithm here

# NOTE: We will be using "Floyd's Tortoise and Hare algorithm (Cycle Finding Algorithm)".
def findRepeatingElement(givenNums):
    slow = givenNums[0]
    fast = givenNums[givenNums[0]]

    while slow != fast:
        slow = givenNums[slow]
        fast = givenNums[givenNums[fast]]

    slow = 0

    while slow != fast:
        slow = givenNums[slow]
        fast = givenNums[fast]

    return slow


givenNums = [1, 2, 3, 4, 5, 3]
print(findRepeatingElement(givenNums)) # repeating = 3
