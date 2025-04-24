import sys


def getNum(num):
    if num == '0':
        return 1
    return -1


def flipBitsInStr(givenStr):
    ans = 0

    for i in givenStr:
        if i == '1':
            ans += 1 # calculating how much 1 we have

    maxSum = -sys.maxsize - 1
    currSum = 0
    start = 0
    end = 0

    n = len(givenStr)

    while end < n:
        while currSum < 0:
            currSum -= getNum(givenStr[start])
            start += 1

        currSum += getNum(givenStr[end])
        end += 1

        maxSum = max(maxSum, currSum) # calculating how much more 1's we can make

    return ans + maxSum # returning the maximum count of 1's after flipping the bits


givenStr = "1101000"
print(flipBitsInStr(givenStr))