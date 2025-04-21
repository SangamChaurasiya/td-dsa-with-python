def threeSum(arr, target):
    temp = arr.copy()
    arr.sort()

    for k in range(len(arr)):
        tempTarget = target - arr[k] # removing the first element from the target sum

        start = k + 1 # starting the pointer for the second element
        end = len(arr) - 1

        while start < end:
            currSum = arr[start] + arr[end] # calculating the sum

            if currSum == tempTarget:
                ans = []
                for i in range(len(temp)):
                    if arr[start] == temp[i] or arr[end] == temp[i] or arr[k] == temp[i]:
                        ans.append(i)
                return ans # returning the indexes for the target sum elements
            
            elif currSum > tempTarget:
                end -= 1 # moving the end pointer, when the sum exceeds
            elif currSum < tempTarget:
                start += 1 # moving the start pointer, when the target exceeds
            
    return -1 # returning when no elements found

arr = [2, 1, 10, 5, 7]
target = 17

print(threeSum(arr, target))
