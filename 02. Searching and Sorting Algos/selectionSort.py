def sortingUsingSelectionSort(givenNums):
    for i in range(len(givenNums)):
        minIndex = i 
        for j in range(i+1, len(givenNums)):
            if givenNums[j] < givenNums[minIndex]: # Getting the minimum element index
                minIndex = j # setting minimum element index
        givenNums[i], givenNums[minIndex] = givenNums[minIndex], givenNums[i] # swapping minimum element with the current element
    return givenNums


print(sortingUsingSelectionSort([2, 4, 5, 1, 3, 0])) # [0, 1, 2, 3, 4, 5]
