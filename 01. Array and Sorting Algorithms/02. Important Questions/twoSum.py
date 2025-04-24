def twoSum(arr, target):
    temp = arr.copy()
    arr.sort()

    start = 0
    end = len(arr) - 1

    while start < end:
        currSum = arr[start] + arr[end] # calculating the sum
        if currSum == target:
            ans = []
            for i in range(len(temp)):
                if arr[start] == temp[i] or arr[end] == temp[i]:
                    ans.append(i)
            return ans # returning the indexes for the target sum elements
        
        if currSum > target:
            end -= 1 # moving the end pointer, when sum exceeds the target
        if currSum < target:
            start += 1 # moving the start pointer, when sum less than the target
        
    return -1 # returning when no elements found

arr = [2, 1, 10, 5, 7]
target = 17

print(twoSum(arr, target))
