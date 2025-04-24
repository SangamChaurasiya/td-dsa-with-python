# Approach 1 : Duplicate Array (TC : O(N), SC : O(N))


# Approach 2 : Reapeated Rotation (TC : O(N * d), SC : O(1))


# Approach 3 : Using Juggling Algorithm (TC : O(N), SC : O(1))
from math import gcd


def rightRotationUsingJugglingAlgo(arr, d):
    n = len(arr)

    gcdVal = gcd(n, d%n) # calculating gcd array

    for i in range(gcdVal):
        temp = arr[i]
        j = i
        while True:
            k = (j - d) % n # performing right rotation

            if k == i:
                break

            arr[j] = arr[k]
            j = k
        arr[j] = temp

    return arr


arr = [1, 2, 3, 4, 5]
print(rightRotationUsingJugglingAlgo(arr, 2))
