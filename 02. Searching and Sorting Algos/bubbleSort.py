def sortingUsingBubbleSort(givenNums):
    for i in range(len(givenNums) - 1):
        isSwaped = False
        for j in range(len(givenNums) - i - 1): # running loop reduced by i as maximum element reached its correct position after every iteration
            if givenNums[j] > givenNums[j+1]:
                isSwaped = True
                givenNums[j], givenNums[j+1] = givenNums[j+1], givenNums[j] # swapping elements if greater element found
        print(givenNums)
        if not isSwaped:
            break
    return givenNums

print(sortingUsingBubbleSort([1, 3, 1, 4, 7, 2]))
print(sortingUsingBubbleSort([1, 2, 3, 4, 5]))