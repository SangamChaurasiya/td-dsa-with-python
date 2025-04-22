def dnfAlgorithm(givenNums):
    n = len(givenNums)
    
    low = 0
    mid = 0
    high = n - 1
    
    while mid < high:
        if givenNums[mid] == 0:
            givenNums[low], givenNums[mid] = givenNums[mid], givenNums[low]
            low += 1
            mid += 1
        elif givenNums[mid] == 1:
            mid += 1
        else:
            givenNums[mid], givenNums[high] = givenNums[high], givenNums[mid]
            high -= 1
    return givenNums


givenNums = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 2, 1, 2, 2, 2, 2, 2]
print(dnfAlgorithm(givenNums))
