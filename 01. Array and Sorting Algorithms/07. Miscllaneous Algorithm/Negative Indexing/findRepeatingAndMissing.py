def findRepeatingAndMissingUsingNegativeIndexing(givenNums):
    repeating = -1
    missing = -1

    totalSum = (len(givenNums) * (len(givenNums) + 1)) // 2 # Calculating the total sum for the array
    currSum = 0

    for i in range(len(givenNums)):
        if givenNums[abs(givenNums[i]) - 1] < 0: # if element is negative then element is repeated
            repeating = abs(givenNums[i])
        givenNums[abs(givenNums[i]) - 1] *= -1 # setting every element to negative 

        currSum += abs(givenNums[i]) # calculating sum of the elements

    missing = totalSum - (currSum - repeating) # finding the missing element

    print(repeating, " ", missing)


givenNums = [1, 2, 1, 4, 5]
findRepeatingAndMissingUsingNegativeIndexing(givenNums) # repeating = 1 missing = 3
