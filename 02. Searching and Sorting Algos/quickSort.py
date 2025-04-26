def partition(myList, left, right):
    i = left
    j = right - 1
    pivot = myList[right]

    while i < j:
        while i < right and myList[i] < pivot:
            i += 1

        while j > left and myList[j] > pivot:
            j -= 1

        if i < j:
            myList[i], myList[j] = myList[j], myList[i]

    if myList[i] > pivot:
        myList[i], myList[right] = myList[right], myList[i]
    
    return i

def sortingUsingQuickSort(myList, left, right):
    if left < right:
        partitionPos = partition(myList, left, right)
        sortingUsingQuickSort(myList, left, partitionPos-1)
        sortingUsingQuickSort(myList, partitionPos+1, right)
    return myList


print(sortingUsingQuickSort([1, 4, 3, 2, 1], 0, 4))
