import sys


def largestSubarraySumInArray(givenNums):
    maxSum = -sys.maxsize - 1
    currSum = 0
    start = 0
    end = 0

    n = len(givenNums)

    while end < n:
        while currSum < 0:
            currSum -= givenNums[start] # removing last added number in the sum as it is making our sum less than 0
            start += 1 # moving our start pointer
        
        currSum += givenNums[end]
        end += 1 # moving our end pointer

        maxSum = max(maxSum, currSum) # getting the maximum sum
    
    return maxSum


givenNums = [1, 4, -3, 10, -20, 12]
# givenNums = [-1, -2, -3]
print(largestSubarraySumInArray(givenNums))
