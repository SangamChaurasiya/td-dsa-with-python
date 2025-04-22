# # Method 1 : Using the sort() and find element(TC : O(nlogn), SC : O(1))
# def majorityElement(givenNums):

#     # Using the sort() method then iterate the elements to find the major element, hence the overall TC will be O(nlogn).
#     givenNums.sort() # sorting the array

#     maxCount = 0
#     count = 1
#     majorElement = givenNums[0]

#     for i in range(len(givenNums) - 1):
#         if givenNums[i] == givenNums[i+1]: 
#             count += 1 # if same element found then increase the counter
#         else:
#             if maxCount < count: # if counter exceeds the maxCount
#                 maxCount = count
#                 majorElement = givenNums[i]
#             count = 1 # Resetting the counter
#     if maxCount < count:
#         majorElement = givenNums[-1] # handling the last element
    
#     return majorElement


# print(majorityElement([1, 2, 3, 2, 2, 1, 1, 2]))


# Method 2: Using the Moore's VOting Algorithm (TC : O(n), SC : O(1))
def majorityElementUsingMooreAlgo(givenNums):
    majorElement = -1
    votes = 0

    for i in givenNums:
        if votes == 0:
            majorElement = i # setting the major element
            votes = 1
        else:
            if majorElement == i:
                votes += 1 # if same element found then increasing the votes
            else:
                votes -= 1 # else decreawsing the votes

    votes = 0
    for i in givenNums:
        if majorElement == i:
            votes += 1 # increasing the votes
    
    if votes > len(givenNums) // 2:
        return majorElement # returning the major element if element is more than n/2 times
    
    return -1 # return if no element is present more than n/2

print(majorityElementUsingMooreAlgo([1, 3, 2, 1, 1]))
