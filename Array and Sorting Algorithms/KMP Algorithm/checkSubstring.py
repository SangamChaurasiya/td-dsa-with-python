def computeLPS(s, lps):
    n = len(s)

    i = 1
    temp = 0

    while i < n:
        if s[i] == s[temp]:
            temp += 1
            lps[i] = temp
            i += 1
        else:
            if temp != 0:
                temp = lps[temp-1]
            else:
                lps[i] = 0
                i += 1


def checkSubstringUsingKMPAlgo(a, b):
    n = len(a)
    m = len(b)
    lps = [0] * m

    computeLPS(b, lps) # computing the LPS to track the substring

    i = 0
    j = 0

    while i < n:
        if a[i] == b[j]:
            i += 1
            j += 1
        if j == m:
            print("b is the substr.")
            return
        elif i < n and a[i] != b[j]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    print("b is not the substr.")


a = "abcabcabe"
b = "abcabe"

checkSubstringUsingKMPAlgo(a, b)
