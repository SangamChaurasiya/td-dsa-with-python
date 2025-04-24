import sys


def kadaneAlgorithm(givenNums):
    maxSum = -sys.maxsize - 1
    currSum = 0
    start = 0
    end = 0

    n = len(givenNums)
    while end < n:
        while currSum < 0:
            currSum -= givenNums[start]
            start += 1
        
        currSum += givenNums[end]
        end += 1

        maxSum = max(currSum, maxSum)

    return maxSum


matrix = [[3, 8, 9, 1, 3], [-4, -1, 1, 7, -6], [-2, -3, 8, 1, -1]]

n = len(matrix)
m = len(matrix[0])
ans = -sys.maxsize - 1

for i in range(m):
    temp = []
    for j in range(n):
        temp.append(matrix[j][i])

    ans = max(ans, kadaneAlgorithm(temp))
    # print(temp)
    # print(ans)

    for j in range(i+1, m):
        for k in range(n):
            temp[k] += matrix[k][j]

        ans = max(ans, kadaneAlgorithm(temp))
        # print(temp)
        # print(ans)

    print('--------------------------')

print(ans)
