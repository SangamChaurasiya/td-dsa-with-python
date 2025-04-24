# # Method 1: Without Recursion

# def withoutRecursionBinarySearch(givenNums, target):
#     low = 0
#     high = len(givenNums) - 1
#     mid = (low + high) // 2

#     while mid > low and mid < high:
#         if givenNums[low] == target: # if first element matches with our target
#             return low
        
#         if givenNums[high] == target: # if last element matches with our target
#             return high
        
#         if givenNums[mid] == target: # if mid element matches with our target
#             return mid
#         elif givenNums[mid] < target: # moving low pointer if current element less than target
#             low = mid
#         else: # moving high pointer if current element greater than target
#             high = mid
#         mid = (low + high) // 2 # calculating mid index
    
#     return -1

# print(withoutRecursionBinarySearch([1, 2, 3, 4, 6], 4))


# Method 2: With Recursion
myList = [1, 2, 3, 4, 6]
target = 8

def withRecursionBinarySearch(low, high):
    global myList, target

    if high - low <= 1:
        if myList[low] == target: # if first element matches with our target
            return low
            
        if myList[high] == target: # if last element matches with our target
            return high

        return -1
        
    mid = (low + high) // 2 # calculating mid index

    if myList[mid] > target: # moving low pointer if current element less than target
        return withRecursionBinarySearch(low, mid)
    
    return withRecursionBinarySearch(mid, high) 
    
print(withRecursionBinarySearch(0, 4))
