def merge(myList, left, middle, right):
    length1 = middle - left + 1
    length2 = right - middle

    leftSeg = [0] * length1
    rightSeg = [0] * length2

    for i in range(length1):
        leftSeg[i] = myList[left + i]

    for i in range(length2):
        rightSeg[i] = myList[middle + i + 1]

    i = 0
    j = 0
    currIndex = left

    while i < length1 and j < length2:
        if leftSeg[i] < rightSeg[j]:
            myList[currIndex] = leftSeg[i]
            i += 1
        else:
            myList[currIndex] = rightSeg[j]
            j += 1
        currIndex += 1
    
    while i < length1:
        myList[currIndex] = leftSeg[i]
        i += 1
        currIndex += 1
    
    while j < length2:
        myList[currIndex] = rightSeg[j]
        j += 1
        currIndex += 1



def sortingUsingMergeSort(myList, left, right):
    if left < right:
        middle = (left + right) // 2

        sortingUsingMergeSort(myList, left, middle)
        sortingUsingMergeSort(myList, middle+1, right)
        merge(myList, left, middle, right)

    return myList


print(sortingUsingMergeSort([1, 4, 3, 2, 1], 0, 4))