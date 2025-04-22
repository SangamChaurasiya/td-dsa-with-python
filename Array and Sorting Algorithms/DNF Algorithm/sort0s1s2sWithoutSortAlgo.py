def dnfAlgorithm(givenNums):
    n = len(givenNums)
    
    low = 0
    mid = 0
    high = n - 1
    
    while mid < high:
        if givenNums[mid] == 0:
            givenNums[low], givenNums[mid] = givenNums[mid], givenNums[low] # swapping low and mid element when mid element is 0
            low += 1
            mid += 1
        elif givenNums[mid] == 1: # moving mid pointer when mid element is 1
            mid += 1
        else:
            givenNums[mid], givenNums[high] = givenNums[high], givenNums[mid] # swapping mid and high element when mid element is 2
            high -= 1
    return givenNums


givenNums = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 2, 1, 2, 2, 2, 2, 2]
print(dnfAlgorithm(givenNums))
