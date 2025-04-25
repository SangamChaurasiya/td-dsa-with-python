def sortingUsingInsertionSort(givenNums):
    for i in range(1, len(givenNums)):
        j = i-1
        key = givenNums[i] # storing element for the insertion

        while j >= 0 and givenNums[j] > key: # checking if greater element found
            givenNums[j+1] = givenNums[j] # moving jth element to the right
            j -= 1
        
        givenNums[j+1] = key # storing key element at its correct position
    
    return givenNums


print(sortingUsingInsertionSort([1, 4, 3, 2, 1]))